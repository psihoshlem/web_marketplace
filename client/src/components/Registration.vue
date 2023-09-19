<template>
  <section class="auth">
    <div class="auth_block">
      <div class="title">Персональные данные</div>
      <div class="auth_data">
        <div class="data-img">
          <label for="avatar">Ваше фото:</label>
          <img id="avatar" src="assets/header_logo.svg" alt="">
        </div>
        <div class="data-pers">
          <div class="field">
            <label for="name">Имя</label>
            <input type="text" id="name" v-model="name">
          </div>
          <div class="field last">
            <label for="last_name">Фамилия</label>
            <input type="text" id="last_name" v-model="lastname">
          </div>
        </div>
        <div class="data-citi">
          <div class="field">
            <label for="login">Логин</label>
            <input type="text" id="login" v-model="login">
          </div>
          <div class="field last">
            <label for="addres">Адрес</label>
            <input type="text" id="addres" v-model="address">
          </div>
        </div>
      </div>
    </div>

    <div class="critery">
      <div class="title">
        Ваши критерии:
      </div>
      <div class="title__desc">
        По вашим критериям мы подберем подходящие для вас товары
      </div>
      <div class="critery-block">
        <div class="field">
          <label for="age">Возраст</label>
          <input type="text" id="login" v-model="age">
        </div>
        <div class="field">
          <label for="Rost">Рост</label>
          <input type="text" id="Rost" v-model="height">
        </div>
        <div class="field">
          <label for="typeLich">Тип личности</label>
          <input type="text" id="typeLich" v-model="personality_type">
        </div>
      </div>
      <div class="hobbi">
        <div class="title">Ваши интересы:</div>
        <textarea name="hobbi" id="" cols="30" rows="10"
          v-model="weight"></textarea>
      </div>
    </div>
    <div class="auth-btn" @click="register()">
      👌🏻 Сохранить
    </div>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Registration',
  data() {
    return {
      login: '',
      password: '',
      address: '',
      name: '',
      lastname: '',
      age: '',
      height: '',
      weight: '',
      personality_type: '',
      status_token: false
    }
  },
  // async created() {
  //   await axios.post('http://localhost:8000/signup', {
  //     login: this.login,
  //     password: this.password,
  //     address: this.address,
  //     name: this.name,
  //     lastname: this.lastname,
  //     age: this.age,
  //     height: this.height,
  //     weight: this.weight,
  //     personality_type: this.personality_type
  //   })
  //     .then((response) => {
  //       if (response.status == 200) {
  //         this.$router.push('/main')
  //         console.log("token ok")
  //       }
  //     })
  //     .catch((error) => {
  //       this.status_token = true
  //     });
  // },
  methods: {
    register() {
      axios.post('http://localhost:8000/signup', {
        login: this.login,
        password: this.password,
        address: this.address,
        name: this.name,
        lastname: this.lastname,
        age: this.age,
        height: this.height,
        weight: this.weight,
        personality_type: this.personality_type
      })
        .then((response) => {
          if (response.status == 200) {
            console.log(response)
            localStorage.setItem('token', response.data.token)
            localStorage.setItem('login', this.login)
            this.$emit('succes_reg', {
              reg: true
            })
          }
        })
        .catch((error) => {
          this.error_msg = "Что-то пошло не так"
        });
    },
    toggleShow() {
      this.showPassword = this.showPassword === "password" ? "text" : "password";
    },
    toggleShow_two() {
      this.showPassword_two = this.showPassword_two === "password" ? "text" : "password";
    },
    go_to_start() {
      this.$router.push('/')
    },
    validation_value() {
      if (this.password !== this.password_two) {
        this.error_msg = "Пароли не совпадают"
        return false
      }
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
