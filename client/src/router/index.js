import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MainPage from '../views/MainPage.vue'
import Registration from '../components/Registration.vue'
import Authentication from '../components/Authentication.vue'
import Profile from '../components/Profile.vue'

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
    path: "/main",
    name: "main",
    component: MainPage
  },
  {
    path: "/profile",
    name: "profile",
    component: Profile
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
