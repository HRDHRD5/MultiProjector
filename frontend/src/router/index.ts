import { createRouter, createWebHistory } from 'vue-router'
import Session from '@/views/Session.vue'
import SessionList from '@/views/SessionList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: SessionList,
    },
    {
      path: '/session/:session_id/',
      name: 'session',
      component: Session,
    },
  ],
})

export default router
