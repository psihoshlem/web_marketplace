<template>
  <div class="logo">
    <a href="" class="logo__link">Umom <span>MARKET</span></a>
    <div class="logo__link-desc">Подберем для вас все</div>
  </div>
  <div class="content">
    <div class="content__left">
      <div class="content__left-top">
        Добрый день
        <img src="../img/header_logo.svg" alt=""
          style="height: 48px; width: 48px;">
        <span>{{ name }}</span>
      </div>
      <p class="content__left-bottom">
        Сегодня дождливо. У вас уже есть<span>☂️</span><a href="">
          зонт?</a>
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
  data() {
    return {
      name: "111"
    }
  },
  created(){
    // console.log("header for auth")
    // console.log(localStorage.getItem('name'))
    this.name = localStorage.getItem('name')
  },
  methods: {
    get_login() {
      return localStorage.getItem('name')
    },
  }
}
</script>
