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
          {{ item_name }}
          {{ item_shop }}
        </div>
        <span style="font-size: 30px;"><svg xmlns="http://www.w3.org/2000/svg"
            width="27" height="25" viewBox="0 0 27 25" fill="none">
            <path
              d="M13.5 0L16.5309 9.32827H26.3393L18.4042 15.0935L21.4351 24.4217L13.5 18.6565L5.5649 24.4217L8.59584 15.0935L0.660737 9.32827H10.4691L13.5 0Z"
              fill="#F2C94C" />
          </svg> {{ item_rating }}</span>
        <img :src="'http://localhost:8000/getimage/'+item_img" alt="">
        <div class="to-buy">
          <div class="price-btn">
            + 🛒
            <span class="price">{{ item_price }} ₽</span>
          </div>
          <div class="to-buy_btn">
            Добавить в корзину
          </div>
        </div>
      </div>
      <div class="desc-block">
        <div class="title">Описание</div>
        <p>{{ item_description }}</p>
      </div>
      <div class="reviews">
        <div class="title">Отзывы</div>
        <div class="reviews-block" v-for="item in item_reviews">
          <div class="reviews-name">
            <img src="../img/header_logo.svg" alt="">
            <span>{{ item.user }}</span>
            <span class="rating_item">{{ item.rating }}</span> <svg
              xmlns="http://www.w3.org/2000/svg" width="27" height="25"
              viewBox="0 0 27 25" fill="none">
              <path
                d="M13.5 0L16.5309 9.32827H26.3393L18.4042 15.0935L21.4351 24.4217L13.5 18.6565L5.5649 24.4217L8.59584 15.0935L0.660737 9.32827H10.4691L13.5 0Z"
                fill="#F2C94C" />
            </svg>
          </div>
          <div class="reviews-text">
            {{ item.review }}
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      item_name: '',
      item_description: '',
      item_shop: '',
      item_reviews: '',
      item_rating: ''
    }
  },
  created() {
    axios.get('http://localhost:8000/get_product?id=' + this.$route.params.item_info, {
      headers: {
        token: localStorage.getItem('token')
      }
    })
      .then((response) => {
        this.item_reviews = response.data.reviews
        // console.log(response)
        this.item_description = response.data.description
        this.item_name = response.data.name
        this.item_shop = response.data.shop
        this.item_rating = response.data.rating
        this.item_img = response.data.img
        this.item_price = response.data.price
      })
  }
}
</script>
<style>
@import url(../assets/style.css);
</style>
