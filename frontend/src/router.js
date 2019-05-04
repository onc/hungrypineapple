import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Landing from "./views/Landing.vue";
import Complaints from "./views/Complaints.vue";
import Opencalls from "./views/Opencalls.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "landing",
      component: Landing
    },
    {
      path: "/city/:city",
      name: "home",
      component: Home,
      props: true
    },
    {
      path: "/complaints",
      name: "complaint-list",
      component: Complaints
    },
    {
      path: "/opencalls",
      name: "opencall-list",
      component: Opencalls
    }
  ]
});
