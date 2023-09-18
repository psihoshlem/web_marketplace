<template>
  <span v-if="status_token === true">
    <div class="block_logo">
      <img src="../img/logo_page1.png" alt="Logo" class="logo_reg" @click="go_to_start" style="cursor: pointer;">
      <div class="name_logo">UMOM ПОИСК</div>
    </div>
    <p v-if="error_msg.length">
      {{ error_msg }}
    </p>
    <section class="reg_section">
      <form>
        <div class="container">
          <h1 class="reg_title">Вход</h1>
          <div class="input_box">
            <input type="text" placeholder="Введите логин" name="login" id="login" v-model="login" required>
            <div class="password">
              <input :type="showPassword" v-model="password" id="password-input" placeholder="Введите пароль" name="password">
              <a @click="toggleShow" class="password-control"></a>
            </div>
          </div>
          <div class="btn"></div><button type="button" class="registerbtn" @click="register">Войти</button>
        </div>
        <div class="container signin">
          <p>Ещё не зарегистрированы?</p>
          <router-link to="/reg">Регистрация</router-link>
        </div>
      </form>
    </section>
  </span>
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
  async created(){
    await axios.post('http://127.0.0.1:8000/home', {
      token:localStorage.getItem('token'),
    })
    .then((response) => {
      if (response.status == 200){
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
      if (this.validation_value()){
        axios.post('http://127.0.0.1:8000/login', {
          login: this.login,
          password: this.password
        })
        .then((response) => {
            if (response.status == 200){
                localStorage.setItem('token',response.data.token)
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
    go_to_start(){
      this.$router.push('/')
    },
    validation_value(){
      if (!this.password && !this.login){
        this.error_msg = "Укажите пароль и логин"
        return false
      }
      if (!this.login){
        this.error_msg = "Укажите логин"
        return false
      }
      if (!this.password){
        this.error_msg = "Укажите пароль"
        return false
      }
      if (this.password && this.login){
        return true
      }
    }
  }
}
</script>

<style>
@import url(https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;600;700&display=swap);
@import url(https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,500;0,700;1,400&display=swap);

.reg_section {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 3vh;
    background-color:#F5F5F5;
}

.block_logo{
    margin-top: 15px;
    display: flex;
    justify-content: center;
    max-width: 1200px;
}
.logo_reg{
    height: 100px;
    max-width: 50%;
    display: block;
    width: 100px;
}
.name_logo{
    margin-top: 35px;
    font-family: 'Ubuntu';
    font-style: normal;
    font-weight: 400;
    font-size: 35px;
    line-height: 40px;
    text-align: center;
    color: #000000;
    top:-50%;
}
.reg_section form{
    max-height: 980px;
    max-width: 580px;
    background-color:#fff;

}
.reg_section form .container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items:center;
}
.input_box #login{
    font-family: 'Raleway';
    font-style: normal;
    padding: 18px 60px;
    margin-top: 84px;
    background: #D9D9D9;
    border-radius: 10px;
    border:none;

}
.reg_title{
    margin-left: 170px;
    margin-right: 170px;
    margin-top: 63px;
    font-family: 'Raleway';
    font-style: normal;
    font-weight: 400;
    font-size: 40px;
    line-height: 47px;
    /* identical to box height */
    text-align: center;
    color: #000000;
}
.registerbtn {
    background-color:  #D4E6E7;
    color: black;
    font-family: 'Raleway';
    padding: 20px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 276px;
    opacity: 0.9;
    border-radius: 15px;
}
.registerbtn::after{
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), inset 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 15px;
}
.password{
    margin-top: 35px;
}
.reg_section .btn{
    margin-top: 60px;
}
#password-input{
    font-family: 'Raleway';
    font-style: normal;
    display: block;
    background: #D9D9D9;
    border-radius: 10px;
    padding: 18px 60px;
    border:none;
}
.container.signin{
    margin-top: 50px;
    margin-bottom: 50px;
    font-family: 'Raleway';
    font-style: normal;
    text-align: center;
    color: #000000;
}
.container.signin a{
    color:#000000;
    text-decoration: underline;
}
.password {
	position: relative;
}
.password-control {
	position: absolute;
	top: 11px;
	right: 6px;
	display: inline-block;
	width: 20px;
	height: 20px;
	background: url('../img/cl_psw.svg') 0 0 no-repeat;
}
.password-control.view {
	background: url('../img/up_psw.svg') 0 0 no-repeat;
}
</style>
