import { createRouter, createWebHashHistory } from 'vue-router'
import ParteI from '../views/ParteI.vue'
import ParteII from '../views/ParteII.vue'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/parteI',
    name: 'parteI',
    component: ParteI 
  },
  {
    path: '/parteII',
    name: 'parteII',
    component: ParteII
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
