<template>
  <div class="wrapper">
    <header>
      <Header_for_auth v-if="success_auth" />
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
          Ваша <span>🛒 </span><a href="">корзина</a>
        </div>
        <div class="basket">
          <div class="basket__box">
            <img src="../img/xyupoimi.png" alt="">
            <div class="basket__box-desc">
              <p>
                Геймпад проводной для
                Xbox 360 и ПК, белый
              </p>
              <span class="price">
                14999₽
              </span>
            </div>
          </div>
          <div class="basket__box">
            <img src="../img/xyupoimi.png" alt="">
            <div class="basket__box-desc">
              <p>
                Геймпад проводной для
                Xbox 360 и ПК, белый
              </p>
              <span class="price">
                14999₽
              </span>
            </div>
          </div>
          <div class="basket__box">
            <img src="../img/xyupoimi.png" alt="">
            <div class="basket__box-desc">
              <p>
                Геймпад проводной для
                Xbox 360 и ПК, белый
              </p>
              <span class="price">
                14999₽
              </span>
            </div>
          </div>
        </div>
      </section>
    </span>
    <span v-else>
      <Authentication v-if="show_auth == true" @succes_auth="go_home()" />
      <Registration v-if="show_reg == true" @succes_reg="go_home()" />
    </span>
    <!-- <section class="buyFriend">
      <div class="title">
        Посмотрите что уже есть у ваших <span>❤️</span><a href="">друзей </a>
      </div>
      <div class="products">
        <div class="product">
          <div class="friend">
            <img src="../img/header_logo.svg" alt="">
            <span class="name">Арсенчик</span>
            <div class="recomenduet"> рекомендует для вас:</div>
          </div>
          <div class="product-img">
            <img src="../img/product.png" alt="">
          </div>
          <div class="product-name">
            Воображариум УЖАСЫ
          </div>
          <span class="product-price">
            1500₽
          </span>
        </div>
        <div class="product">
          <div class="friend">
            <img src="../img/header_logo.svg" alt="">
            <span class="name">Арсенчик</span>
            <div class="recomenduet"> рекомендует для вас:</div>
          </div>
          <div class="product-img">
            <img src="../img/product.png" alt="">
          </div>
          <div class="product-name">
            Воображариум УЖАСЫ
          </div>
          <span class="product-price">
            1500₽
          </span>
        </div>
        <div class="product">
          <div class="friend">
            <img src="../img/header_logo.svg" alt="">
            <span class="name">Арсенчик</span>
            <div class="recomenduet"> рекомендует для вас:</div>
          </div>
          <div class="product-img">
            <img src="../img/product.png" alt="">
          </div>
          <div class="product-name">
            Воображариум УЖАСЫ
          </div>
          <span class="product-price">
            1500₽
          </span>
        </div>
      </div>
    </section>
    <section class="yourLike">
      <div class="title">
        Посмотрите что еще вам может понравиться:
      </div>
      <div class="products">
        <div class="product">
          <div class="product-img">
            <img src="../img/odelo.png" alt="">
          </div>
          <div class="product-name">
            Воображариум УЖАСЫ
          </div>
          <span class="product-price">
            1500₽
          </span>
        </div>
        <div class="product">
          <div class="product-img">
            <img src="../img/odelo.png" alt="">
          </div>
          <div class="product-name">
            Воображариум УЖАСЫ
          </div>
          <span class="product-price">
            1500₽
          </span>
        </div>
        <div class="product">
          <div class="product-img">
            <img src="../img/odelo.png" alt="">
          </div>
          <div class="product-name">
            Воображариум УЖАСЫ
          </div>
          <span class="product-price">
            1500₽
          </span>
        </div>
      </div>
    </section>


    <section class="notFound">
      <div class="title">
        Это проще чем кажется! Выполните три простых шага!
      </div>
      <form action="">
        <div class="block_name">
          <label for="name">Название товара:</label>
          <input id="name" type="text">
        </div>
        <div class="block_desc">
          <label for="desc">Описание товара</label>
          <textarea id="desc" type="text"></textarea>
        </div>
        <div class="block_img">
          <label for="desc">Фото(при наличии)</label>
          <input id="desc" type="file">
        </div>
        <p>Когда один из наших продавцов откликнется на ваш запрос, вам придет
          уведомление.</p>
        <button id="submit">👌🏻 Опубликовать</button>
      </form>
    </section>


    <footer>
      <div class="footer__inner">
        <div class="first_colomn">
          <a href=""><img src="../img/aple.svg" alt=""></a>
          <a href=""><img src="../img/qr.svg" alt=""></a>
        </div>
        <div class="second_colomn">
          <div class="first_colomn">
            <ul>
              <li><a href="">О нас </a></li>
              <li><a href="">Наши продавцы</a></li>
              <li><a href="">О товарах</a></li>
              <li><a href="">Пресса</a></li>
            </ul>
          </div>
          <div class="second_colomn">
            <ul>
              <li><a href="">Помощь </a></li>
              <li><a href="">Оплата</a></li>
              <li><a href="">Доставка</a></li>
              <li><a href="">Возврат</a></li>
            </ul>
          </div>
        </div>
        <div class="third_colomn">
          <a href=""><img src="../img/inst.svg" alt=""></a>
          <a href=""><img src="../img/twiter.svg" alt=""></a>
          <a href=""><img src="../img/facebook.svg" alt=""></a>
        </div>
      </div>
      <div class="foter_logo">
        <a href="">UMOM Market 2023</a>
      </div>
    </footer> -->
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
      success_auth: false,
      show_block: true
    }
  },
  async created() {
    await axios.get('http://localhost:8000/get_user_info', {
      headers: {
        token: localStorage.getItem('token')
      }
    })
      .then((response) => {
        console.log(response)
        if (response.status == 200) {
          this.success_auth == true
        }
      })
  },
  methods: {
    scrolle_to(anchor) {
      const el = document.getElementById(anchor);
      el.scrollIntoView({ behavior: "smooth", block: "end" })
    },
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
      this.show_block = true
      this.success_auth = true
      this.show_auth = false
      this.show_reg = false
    }
  }
}
</script>

<style>
@import url(../assets/style.css);

@import url(https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;800&display=swap);
</style>
