import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Complaints from './views/Complaints.vue'
import Opencalls from './views/Opencalls.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/city/:city',
      name: 'home-city',
      component: Home,
      props: true
    },
    {
      path: '/city/:city/complaints',
      name: 'complaints',
      component: Complaints,
      props: true
    },
    {
      path: '/city/:city/opencalls',
      name: 'opencalls',
      component: Opencalls,
      props: true
    }
  ]
})
