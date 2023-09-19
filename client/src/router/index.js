import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Registration from '../components/Registration.vue'
import Authentication from '../components/Authentication.vue'
import Profile from '../components/Profile.vue'
import card_product from '../components/card_product.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/auth',
    name: 'auth',
    component: Authentication
  },
  {
    path: '/reg',
    name: 'reg',
    component: Registration
  },
  {
    path: "/profile",
    name: "profile",
    component: Profile
  },
  {
    path: "/product:item_info",
    name: "product",
    component: card_product
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
