<template>
  <div class="logo">
    <a href="" class="logo__link">Umom <span>MARKET</span></a>
    <div class="logo__link-desc">Подберем для вас все</div>
  </div>
  <div class="content">
    <div class="content__left">
      <div class="content__left-top">
        Добрый день
        <span>Вы уже с нами?</span>
      </div>
      <p class="content__left-bottom">
        <a @click="go_auth()">Войдите</a> или <a
          @click="go_reg()">зарегестрируйтесь</a>
      </p>
    </div>
    <div class="content__right">
      <div class="content__right-box">
        <div class="basket">🛒 <span>0</span></div>
        <div class="message">💬 <span>0</span></div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Authentication',
  data() {
    return {
      login: '',
      password: '',
      showPassword: "password",
      error_msg: '',
      status_token: false
    }
  },
  methods: {
    go_auth() {
      this.$emit('auth', {
        auth: true
      })
    },
    go_reg() {
      this.$emit('reg', {
        reg: true
      })
    },
  }
}
</script>
