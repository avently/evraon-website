---
title: Сброс пароля
---
<form id="password_reset_form">
<p>Если вы хотите сбросить пароль, введите email аккаунта. Будет отправлена ссылка для подтверждения:</p>
<input class="md-input" style="background-color: var(--md-code-bg-color)" id="email" type="email" placeholder="Email" autocapitalize="none" autocorrect="off"  spellcheck="false" />
<br/>
<br/>
<button class="md-button md-button--primary" type="submit">Сбросить пароль</button>


</form>
<p id="password_reset_success" style="display: none;">Подтверждение сброса пароля было отправлено. Проверьте вашу почту во входящих и в спаме. Как только вы перейдете по ссылке из письма вам будет предложено установить новый пароль.</p>



<script type="text/javascript">
  function ready() {
    initResetPassword()
  }

  document.addEventListener("DOMContentLoaded", ready)
</script>