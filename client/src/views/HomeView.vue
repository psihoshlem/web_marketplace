<template>
  <span v-if="status_token === true">
    <div class="header">
      <div class="container">
          <div class="menu">
            <div class="menu__about">
              <a @click="scrolle_to('work')" class="about__link">Как это работает?</a>
              <a @click="scrolle_to('about')" class="about__link">О нас</a>
              <a @click="scrolle_to('social')" class="about__link">Контакты</a>
            </div>
          <div class="menu__log">
            <router-link to="/auth" class="log__link">Войти</router-link>
            <router-link to="/reg" class="log__link">Регистрация</router-link>
          </div>
        </div>
        <div class="header__content">
          <a href="#!"><img src="../img/logo_page1.png" alt="" class="content__img"></a>
          <div class="content__txt">
            <h5 class="txt__title">Найди себе команду</h5>
            <div class="block__txt"><p class="txt__desc">Сервис поиска проектов</p></div>
          </div>
        </div>
      </div>
    </div>
    <div class="main">
      <section class="project">
        <div class="container">
          <h1 class="project__title">Начни свой путь вместе с другими энтузиастами</h1>
          <p class="project__txt">Если вы начинающий специалист, который ищет себе команду для совместной работы над проектом, то сервис от команды <b>UMOM CODING</b> отлично подойдет для вас.<br><br>
            Также сервис подойдет и для опытных специалистов, которые хотят найти себе коллег, с которыми можно создавать совместные проекты.</p>
        </div>
      </section>
      <section class="work" id="work">
        <div class="container">
          <h1 class="work__title">Как это работает?</h1>
          <h3 class="work__desc">Создай анкету и ищи, все просто!</h3>
          <p class="work__txt">ляляля</p>
        </div>
      </section>
      <section class="about" id="about">
        <div class="container">
          <h1 class="about__title">О нас</h1>
          <p class="about__txt">лялялляляля</p>
        </div>
      </section>
    </div>
    <footer id="social">
      <div class="container">
        <h1 class="social__title">Контакты</h1>
        <div class="social">
            <ul>
              <li><img src="../img/inst.svg" alt="">yng.ync</li>
              <li><img src="../img/tele.svg" alt="">vk.com/s3nks</li>
              <li><img src="../img/vk.svg" alt="">vk.com/s3nks</li>
            </ul>
          <div class="connect">
            <div class="phone">Номер: +7 (919) 659-00-40</div>
            <div class="mail">Mail: arsenkrytoypacan@mail.ru</div>
            <div class="adress">Адрес: Московский просп., 15, Чебоксары, Чувашская Респ., 428003</div>
          </div>
        </div>
        <div class="tru">Используя данный сайт, вы автоматически принимаете условия договор-оферты.<br> Регистрируюясь на сайте, вы принимаете <a href="#" class="line">Положение</a> и 
            <a href="#" class="line">Согласие на обработку персональных данных</a>
        </div>
      </div>
    </footer>
  </span>
</template>

<script>
import axios from 'axios';

import Registration from '@/components/Registration.vue'
import Authentication from '@/components/Authentication.vue'

export default {
  name: 'HomeView',
  components: {
    Registration,
    Authentication,
  },
  data(){
    return{
      status_token:false,
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
  methods:{
    scrolle_to(anchor){
      const el = document.getElementById(anchor);
      el.scrollIntoView({behavior: "smooth", block: "end"})
    }
  }
}
</script>

<style>
@import url(https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;600;700&display=swap);
@import url(https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,500;0,700;1,400&display=swap);

.wrapper {
	display: flex;
	flex-direction: column;
	min-height: 100%;
}

.main {
	flex: 1 0 auto;
}
.footer {
	flex: 0 0 auto;
}
.header{
    min-height: 530px;
    padding-top: 30px;
    background-image: url('../img/bg_first_page.jpg');
    background-size:cover;
    background-repeat: no-repeat;
    background-position:center;
}
.container{
	max-width: 1200px;
    padding: 0 20px;
    margin: 0 auto;
}
.menu{
    display: flex;
    justify-content:space-between;
    margin-top: 15px;
}
.menu__about{
    display: flex;
    justify-content: row;
}
.about__link{
    padding: 15px;
    margin-left: 23px;
    background: #CEE0E0;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 15px;
    font-size: 16px;
    font-family: Roboto;
}
.menu__log{
    display: flex;
    justify-content: row;
}
.log__link{
    padding: 15px;
    margin-right: 35px;
    background: rgba(217, 217, 217, 0.6);
    border-radius: 15px;
    font-size: 16px;
    font-family: Roboto;

}
.header__content{
    display: flex;
    justify-content: space-between;
}
.content__img{
    margin-top: 70px;
    margin-left: 3px;
}
.content__txt{
    margin-top: 171px;
}
.txt__title{
    font-family: 'Raleway';
    font-style: normal;
    font-weight: 400;
    font-size: 60px;
    line-height: 70px;
    font-size: 60px;
    text-align: center;
    color: #fff;
}

.header__content .txt__desc{
    margin-left: 90px;
    width: 400px;
    font-family: 'Raleway';
    background: #302F36;
    border-radius: 15px;
    color:#a0a0a0;
    font-style: normal;
    font-weight: 400;
    font-size: 30px;
    line-height: 35px;
    text-align: center;
}
.project {
    padding-top: 75px;
    min-height: 500px;
    background-color: #CFE1E4;
}
.project__title{
    font-family: 'Raleway';
    font-style: normal;
    font-weight: 700;
    font-size: 50px;
    line-height: 59px;
    color: #000000;
}
.project__txt{
    margin-top: 50px;
    font-family: 'Raleway';
    font-style: normal;
    font-weight: 300;
    font-size: 30px;
    line-height: 35px;
    color: #000000;
}
.project__txt br{
    margin-top: 30px;
}
.work{
    padding-top: 75px;
    min-height: 500px;
    background-color: #CFE1E4;
}
.work__title{
    font-family: 'Raleway';
    font-style: normal;
    font-weight: 700;
    font-size: 50px;
    line-height: 59px;
    color: #000000;
}
.work__desc{
    font-family: 'Raleway';
    font-style: normal;
    font-weight: 600;
    font-size: 30px;
    line-height: 35px;
    color: #000000;
}
.work__txt{
    margin-top: 30px;
    font-family: 'Raleway';
    font-style: normal;
    font-weight: 300;
    font-size: 30px;
    line-height: 35px;
}
.about{
    min-height: 500px;
    background-color: #CFE1E4;
}
.about__title{
    font-family: 'Raleway';
    font-style: normal;
    font-weight: 700;
    font-size: 50px;
    line-height: 59px;
    color: #000000;
}
.about__txt{
    margin-top: 30px;
    font-family: 'Raleway';
    font-style: normal;
    font-weight: 300;
    font-size: 30px;
    line-height: 35px;
}
footer{
    min-height: 250px;
    background: #394042;
}
footer .container{
    padding-top: 15px;
}
.social__title{
    font-family: 'Raleway';
    font-style: normal;
    font-weight: 600;
    font-size: 30px;
    line-height: 50px;
}
.social{
    margin-top: 20px;
    display: flex;
    justify-content: space-between;
    color:#c2bfbf;
    font-family: 'Roboto';
}
.social ul{
    display: flex;
    flex-direction: row;
    list-style: none;
    padding: 0;
}
.social li{
    margin: 0 20px;
}
.connect{
    display: flex;
    flex-direction: column;
}
.connect img{
    width: 59px;
    height: 48px;
}
.tru{
    font-family: 'Roboto';
    margin-top: 45px;
    color:#c2bfbf;
}
</style>
