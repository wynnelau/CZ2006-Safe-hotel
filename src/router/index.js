import { createRouter, createWebHistory } from "vue-router";
import Home from '@/views/Home.vue'
import Filter from '@/views/Filter.vue'
import Recom from '@/views/Recom.vue'

const routes = [
  {
    path: "/",
    redirect: "/home"
  },
  {
    path: "/home",
    name: "home",
    component: Home
  },
  {
    path: "/search",
    name: "filter",
    component: Filter
  },
  {
    path: "/dailyRecommendations",
    name: "recommendation",
    component: Recom
  }
]

const router = createRouter({
  history: createWebHistory(), 
  routes
})

export default router