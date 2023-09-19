<template>
  <div class="wrapper">
    <section class="login">
      <div class="title">
        Рады видеть вас снова
      </div>
      <div class="field">
        <label for="login">Логин</label>
        <input type="text" id="login">
      </div>
      <div class="field last" style="margin-top: 17px;">
        <label for="password">Пароль</label>
        <input type="text" id="password">
      </div>
      <div class="btn">Войти</div>
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
      showPassword: "password",
      error_msg: '',
      status_token: false
    }
  },
  async created() {
    await axios.post('http://localhost:8000/auth', {
      token: localStorage.getItem('token'),
    })
      .then((response) => {
        if (response.status == 200) {
          this.$router.push('/main')
          console.log("token ok")
        }
      })
      .catch((error) => {
        this.status_token = true
      });
  },
  methods: {
    register() {
      if (this.validation_value()) {
        axios.post('http://127.0.0.1:8000/login', {
          login: this.login,
          password: this.password
        })
          .then((response) => {
            if (response.status == 200) {
              localStorage.setItem('token', response.data.token)
              localStorage.setItem('login', response.data.login)
              this.$router.push('/main')
            }
          })
          .catch((error) => {
            this.error_msg = "Не верный логин или пароль"
          });
      }
    },
    toggleShow() {
      this.showPassword = this.showPassword === "password" ? "text" : "password";
    },
    go_to_start() {
      this.$router.push('/')
    },
    validation_value() {
      if (!this.password && !this.login) {
        this.error_msg = "Укажите пароль и логин"
        return false
      }
      if (!this.login) {
        this.error_msg = "Укажите логин"
        return false
      }
      if (!this.password) {
        this.error_msg = "Укажите пароль"
        return false
      }
      if (this.password && this.login) {
        return true
      }
    }
  }
}
</script>

<style>
@import url(../assets/style.css);
</style>
