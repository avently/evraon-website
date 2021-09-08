---
title: Password reset
---
<form id="password_reset_form">
<p>If you want to reset the password type your account's email. Confirmation link will be sent to it:</p>
<input class="md-input" style="background-color: var(--md-code-bg-color)" id="email" type="email" placeholder="Email" autocapitalize="none" autocorrect="off"  spellcheck="false" />
<br/>
<br/>
<button class="md-button md-button--primary" type="submit">Reset password</button>


</form>
<p id="password_reset_success" style="display: none;">Password reset request was sent to specified email. Check your inbox and spam folders. Once you click on a link in the message you'll be able to choose a new password.</p>



<script type="text/javascript">
  function ready() {
    initResetPassword()
  }

  document.addEventListener("DOMContentLoaded", ready)
</script>