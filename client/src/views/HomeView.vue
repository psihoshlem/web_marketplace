<template>
  <div class="wrapper">
    <header>
      <Header_for_auth v-if="auth" />
      <Header_for_not_auth v-else @auth="show_form_auth()"
        @reg="show_form_reg()" />
    </header>
    <span v-if="show_block == true">
      <div class="search__block">
        <input type="text" placeholder="Чтобы вы хотели бы найти?">
        <div class="search__list">
          <div class="search__list-item">
            👕 Одежда
          </div>
          <div class="search__list-item">
            👞 Обувь
          </div>
          <div class="search__list-item">
            💻 Электроника
          </div>
          <div class="search__list-item">
            🛋️ Для дома
          </div>
          <div class="search__list-item">
            📚 Книги
          </div>
          <div class="search__list-item">
            👶🏻 Для детей
          </div>
          <div class="search__list-item">
            🔨Услуги
          </div>
        </div>
      </div>
      <section class="yourBasket">
        <div class="title">
          Успейте купить <span>🛒 </span>
        </div>
        <div class="basket">
          <div class="basket__box" v-for="item in all_products"
            @click="go_to_product(item)">
            <img :src="'http://localhost:8000/getimage/'+item.img" alt="">
            <div class="basket__box-desc">
              <p>
                {{ item.name }}
              </p>
              <span class="price">
                {{ item.shop }}
              </span>
              <p class="price">
                999p.
              </p>
            </div>
          </div>
        </div>
      </section>
    </span>
    <span v-else>
      <Authentication v-if="show_auth == true" @succes_auth="go_home()" />
      <Registration v-if="show_reg == true" @succes_reg="go_home()" />
    </span>

  </div>
</template>

<script>
import axios from 'axios';

import Registration from '@/components/Registration.vue'
import Authentication from '@/components/Authentication.vue'
import Header_for_auth from '@/components/Header_for_auth.vue'
import Header_for_not_auth from '@/components/Header_for_not_auth.vue'

export default {
  name: 'HomeView',
  components: {
    Registration,
    Authentication,
    Header_for_auth,
    Header_for_not_auth,
  },
  data() {
    return {
      status_token: false,
      show_reg: false,
      show_auth: false,
      show_block: true,
      auth: false,
      success_auth: false,
      all_products: []
    }
  },
  async mounted() {
    if (localStorage.getItem('token') != null) {
      await axios.get('http://localhost:8000/get_all_products', {
        headers: {
          token: localStorage.getItem('token')
        }
      })
        .then((response) => {
          if (response.status == 200) {
            this.auth = true
          }
        })
    }
  },
  async created() {
    await axios.get('http://localhost:8000/get_all_products', {
      headers: {
        token: localStorage.getItem('token')
      }
    })
      .then((response) => {
        if (response.status == 200) {
          console.log(response.data)
          this.all_products = response.data
        }
      })
  },
  methods: {
    show_form_auth() {
      this.show_block = false
      this.show_reg = false
      this.show_auth = true
    },
    show_form_reg() {
      this.show_block = false
      this.show_auth = false
      this.show_reg = true
    },
    go_home() {
      this.auth = true
      this.show_block = true
      this.success_auth = true
      this.show_auth = false
      this.show_reg = false
    },
    go_to_product(item) {
      this.$router.push({ name: 'product', params: { item_info: item.id } })
    }
  }
}
</script>

<style>
@import url(../assets/style.css);

@import url(https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;800&display=swap);
</style>
