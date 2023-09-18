<template>
  <span v-if="status_token === true">\
    <div>
      <h3>Добрый день! Вы уже с нами?</h3>
      <router-link to="/auth">Войдите</router-link> или
      <router-link to="/reg">Зарегестрируйтесь</router-link>
    </div>
    <div>
      <input placeholder="чего бы хотели найти ебать">
      <div>
        <button>одежда</button><button>обувь</button><button>электроника</button>
      </div>
    </div>
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
  data() {
    return {
      status_token: false,
    }
  },
  async created() {
    await axios.post('http://127.0.0.1:8000/home', {
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
    scrolle_to(anchor) {
      const el = document.getElementById(anchor);
      el.scrollIntoView({ behavior: "smooth", block: "end" })
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

.header {
  min-height: 530px;
  padding-top: 30px;
  background-image: url('../img/bg_first_page.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

.container {
  max-width: 1200px;
  padding: 0 20px;
  margin: 0 auto;
}

.menu {
  display: flex;
  justify-content: space-between;
  margin-top: 15px;
}

.menu__about {
  display: flex;
  justify-content: row;
}

.about__link {
  padding: 15px;
  margin-left: 23px;
  background: #CEE0E0;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 15px;
  font-size: 16px;
  font-family: Roboto;
}

.menu__log {
  display: flex;
  justify-content: row;
}

.log__link {
  padding: 15px;
  margin-right: 35px;
  background: rgba(217, 217, 217, 0.6);
  border-radius: 15px;
  font-size: 16px;
  font-family: Roboto;

}

.header__content {
  display: flex;
  justify-content: space-between;
}

.content__img {
  margin-top: 70px;
  margin-left: 3px;
}

.content__txt {
  margin-top: 171px;
}

.txt__title {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 400;
  font-size: 60px;
  line-height: 70px;
  font-size: 60px;
  text-align: center;
  color: #fff;
}

.header__content .txt__desc {
  margin-left: 90px;
  width: 400px;
  font-family: 'Raleway';
  background: #302F36;
  border-radius: 15px;
  color: #a0a0a0;
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

.project__title {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 700;
  font-size: 50px;
  line-height: 59px;
  color: #000000;
}

.project__txt {
  margin-top: 50px;
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 300;
  font-size: 30px;
  line-height: 35px;
  color: #000000;
}

.project__txt br {
  margin-top: 30px;
}

.work {
  padding-top: 75px;
  min-height: 500px;
  background-color: #CFE1E4;
}

.work__title {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 700;
  font-size: 50px;
  line-height: 59px;
  color: #000000;
}

.work__desc {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 600;
  font-size: 30px;
  line-height: 35px;
  color: #000000;
}

.work__txt {
  margin-top: 30px;
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 300;
  font-size: 30px;
  line-height: 35px;
}

.about {
  min-height: 500px;
  background-color: #CFE1E4;
}

.about__title {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 700;
  font-size: 50px;
  line-height: 59px;
  color: #000000;
}

.about__txt {
  margin-top: 30px;
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 300;
  font-size: 30px;
  line-height: 35px;
}

footer {
  min-height: 250px;
  background: #394042;
}

footer .container {
  padding-top: 15px;
}

.social__title {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 600;
  font-size: 30px;
  line-height: 50px;
}

.social {
  margin-top: 20px;
  display: flex;
  justify-content: space-between;
  color: #c2bfbf;
  font-family: 'Roboto';
}

.social ul {
  display: flex;
  flex-direction: row;
  list-style: none;
  padding: 0;
}

.social li {
  margin: 0 20px;
}

.connect {
  display: flex;
  flex-direction: column;
}

.connect img {
  width: 59px;
  height: 48px;
}

.tru {
  font-family: 'Roboto';
  margin-top: 45px;
  color: #c2bfbf;
}
</style>
