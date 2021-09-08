---
title: Смена пароля
---
<form id="password_change_form">
<p>Введите новый пароль и повторите его же для подтверждения.
<br/>
Пароль должен быть из 8 или более символов:
</p>
<input class="md-input" style="background-color: var(--md-code-bg-color)" id="password" type="password" placeholder="Пароль" autocapitalize="none" autocorrect="off"  spellcheck="false" />
<input class="md-input" style="background-color: var(--md-code-bg-color)" id="password_confirm" type="password" placeholder="Подтверждение пароля" autocapitalize="none" autocorrect="off"  spellcheck="false" />
<br/>
<br/>
<button class="md-button md-button--primary" type="submit">Изменить пароль</button>


</form>
<p id="password_change_error" style="display: none;">Убедитесь, что пароли совпадают и подходят под требования</p>
<p id="password_change_success" style="display: none;">Пароль успешно изменен. Можете войти в аккаунт с новым паролем.</p>



<script type="text/javascript">
  function ready() {
    initChangePassword()
  }

  document.addEventListener("DOMContentLoaded", ready)
</script>