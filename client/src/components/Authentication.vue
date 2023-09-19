<template>
  <div class="wrapper">
    <section class="login">
      <div class="title">
        Рады видеть вас снова
      </div>
      <div class="field">
        <label for="login">Логин</label>
        <input type="text" id="login" v-model="login">
      </div>
      <div class="field last" style="margin-top: 17px;">
        <label for="password">Пароль</label>
        <input type="text" id="password" v-model="password">
      </div>
      <div class="btn" @click="login_auth()">Войти</div>
    </section>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Authentication',
  data() {
    return {
      login: '',
      password: '',
    }
  },
  methods: {
    login_auth() {
      axios.post('http://localhost:8000/login', {
        login: this.login,
        password: this.password
      })
        .then((response) => {
          if (response.status == 200) {
            localStorage.setItem('token', response.data.token)
            localStorage.setItem('login', this.login)
            this.$emit('succes_auth', {
              auth: true
            })
          }
        })
        .catch((error) => {
          this.error_msg = "Не верный логин или пароль"
        });
    }
  }
}
</script>

<style>
@import url(../assets/style.css);
</style>
