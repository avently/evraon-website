---
title: Password change
---
<form id="password_change_form">
<p>Enter your new password and the same new password one more time to confirm.
<br/>
The password should be 8 or more characters long:
</p>
<input class="md-input" style="background-color: var(--md-code-bg-color)" id="password" type="password" placeholder="Password" autocapitalize="none" autocorrect="off"  spellcheck="false" />
<input class="md-input" style="background-color: var(--md-code-bg-color)" id="password_confirm" type="password" placeholder="Confirm password" autocapitalize="none" autocorrect="off"  spellcheck="false" />
<br/>
<br/>
<button class="md-button md-button--primary" type="submit">Change password</button>


</form>
<p id="password_change_error" style="display: none;">Ensure your passwords are the same and conforms to a format</p>
<p id="password_change_success" style="display: none;">Password was changed successfully. You can login in the app with the new password.</p>



<script type="text/javascript">
  function ready() {
    initChangePassword()
  }

  document.addEventListener("DOMContentLoaded", ready)
</script>