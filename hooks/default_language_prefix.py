"""Expose the default language under a /<locale>/ prefix.

mkdocs-static-i18n v1 always builds the default language at the site root and
only prefixes the non-default languages (e.g. /ru/). This site has always been
served with the English version available at both / and /en/, and the content
contains absolute links like /en/docs/installation/.

This hook duplicates the freshly built default-language site into
<site_dir>/<default_locale>/ so that /en/... keeps working. Relative links,
assets and the search index stay valid because the whole tree is copied as-is.
The canonical and hreflang links are rewritten afterwards so that the /en/
pages point at themselves instead of the root pages.
"""

import re
import shutil
from pathlib import Path
from urllib.parse import urljoin

# Files that must only exist at the site root.
ROOT_ONLY = {"CNAME", "sitemap.xml", "sitemap.xml.gz"}

CANONICAL_RE = re.compile(r'(<link rel="canonical" href=")([^"]*)(")')
ALTERNATE_RE = re.compile(r'(<link rel="alternate" href=")([^"]*)(" hreflang=")([^"]*)(")')


def _page_url(rel_path: Path) -> str:
    """Return the root-relative URL of a built page (docs/index.html -> /docs/)."""
    if rel_path.name == "index.html":
        parent = rel_path.parent.as_posix()
        return "/" if parent == "." else f"/{parent}/"
    return f"/{rel_path.as_posix()}"


def _rewrite_links(path: Path, original_url: str, site_url: str, locale: str) -> None:
    html = path.read_text(encoding="utf-8")
    canonical = urljoin(site_url, f"{locale}{original_url}")

    def fix_canonical(match):
        return f"{match.group(1)}{canonical}{match.group(3)}"

    def fix_alternate(match):
        href, lang = match.group(2), match.group(4)
        if lang == locale:
            # The default-language copy of this page lives at /<locale><url>.
            resolved = f"/{locale}{original_url}"
        else:
            resolved = urljoin(original_url, href)
        return f"{match.group(1)}{resolved}{match.group(3)}{lang}{match.group(5)}"

    html = CANONICAL_RE.sub(fix_canonical, html)
    html = ALTERNATE_RE.sub(fix_alternate, html)
    path.write_text(html, encoding="utf-8")


def on_post_build(config):
    i18n = config.plugins.get("i18n")
    if i18n is None:
        return

    default_locale = i18n.default_language
    # The i18n plugin triggers a build per language; only act on the default one.
    if i18n.current_language != default_locale:
        return

    site_dir = Path(config.site_dir)
    target_dir = site_dir / default_locale
    locale_dirs = {lang.locale for lang in i18n.config.languages}
    site_url = config.site_url or "/"

    # Start from a clean copy so removed pages do not linger on rebuilds.
    shutil.rmtree(target_dir, ignore_errors=True)
    target_dir.mkdir(parents=True, exist_ok=True)
    for entry in site_dir.iterdir():
        # Never copy the localized builds (or the target itself) into the target.
        if entry.name in locale_dirs or entry.name in ROOT_ONLY:
            continue
        destination = target_dir / entry.name
        if entry.is_dir():
            shutil.copytree(entry, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(entry, destination)

    for html_path in target_dir.rglob("*.html"):
        _rewrite_links(
            html_path,
            _page_url(html_path.relative_to(target_dir)),
            site_url,
            default_locale,
        )
