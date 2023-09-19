<template>
  <div class="wrapper">
    <section class="product">
      <div class="sendFriend">
        <span class="sendFriend-respect">👍🏻 Порекомендуйте</span>
        своим
        <span>❤️</span>
        <a href="">друзьям</a>!
      </div>
      <div class="product-block">
        <div class="product-title">
          Игровая консоль<strong> Xbox One Microsoft 500Gb</strong>
        </div>
        <img src="assets/i/xbox.png" alt="">
        <div class="category">
          <span>Xbox</span>
          <span>Игры</span>
          <span>Game</span>
          <span>Консоль</span>
        </div>
        <div class="to-buy">
          <div class="price-btn">
            + 🛒
            <span class="price">55999₽</span>
          </div>
          <div class="to-buy_btn">
            Добавить в корзину
          </div>
        </div>
      </div>
      <div class="desc-block">
        <div class="title">Описание</div>
        <p>Игровая приставка Microsoft Xbox Series X — устройство с впечатляющей
          конфигурацией, сочетающейся с лаконичным внешним видом.
          Высочайший уровень производительности этой модели позволяет получить
          картинку идеального качества при любой детализации графики
          МОЩНЕЙШЕЕ ЖЕЛЕЗОЭто самый крупный скачок в плане процессоров из всех
          поколений Xbox. Консоль в четыре раза мощнее своих
          предшественников благодаря процессору AMD Zen 2, 16 ГБ оперативной
          памяти, а также специально созданному графическому процессору
          AMD Navi. Один чип XSX может воспроизводить сразу четыре игровые сессии
          Xbox One S..</p>
      </div>
      <div class="feature">
        <div class="title">Характеристики:</div>
        <ul class="feature-list">
          <li>Объем встроенной памяти</li>
          <li>Графический процессор</li>
          <li>Процессор</li>
        </ul>
      </div>
      <div class="reviews">
        <div class="title">Отзывы</div>
        <div class="reviews-block">
          <div class="reviews-name">
            <img src="assets/header_logo.svg" alt="">
            <span>Алексей</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="27" height="25"
              viewBox="0 0 27 25" fill="none">
              <path
                d="M13.5 0L16.5309 9.32827H26.3393L18.4042 15.0935L21.4351 24.4217L13.5 18.6565L5.5649 24.4217L8.59584 15.0935L0.660737 9.32827H10.4691L13.5 0Z"
                fill="#F2C94C" />
            </svg>
          </div>
          <div class="reviews-text">
            Неплохо но плейстейшон лучше!
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
export default {
  data() {
    return {
      login: ''
    }
  },
  async mounted() {
    console.log(this.$route.params)
  }
}
</script>
<style>
@import url(../assets/style.css);
</style>
