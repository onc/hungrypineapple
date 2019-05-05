<template>
  <b-navbar toggleable="lg" class="my-nav">
    <b-navbar-brand
      variant="info"
      v-if="!['home', 'home-city'].includes($route.name)"
    >
      <router-link :to="{ path: `/city/${city}/` }">Home page</router-link>
    </b-navbar-brand>

    <!-- Right aligned nav items -->
    <b-navbar-nav class="ml-auto">
      <b-nav-item class="nav-text">
        <router-link :to="{ path: `/city/${city}/complaints` }"
          >Complaints</router-link
        >
      </b-nav-item>
      <b-nav-item class="nav-text">
        <router-link :to="{ path: `/city/${city}/opencalls` }" append
          >Open calls</router-link
        >
      </b-nav-item>
      <b-nav-item class="nav-text" href="#">Login</b-nav-item>
      <b-nav-item class="nav-text" href="#">Sign up</b-nav-item>
    </b-navbar-nav>
  </b-navbar>
</template>

<script>
//@select="handleSelect"
export default {
  data() {
    return {
      activeIndex: '1'
    }
  },
  computed: {
    city() {
      return this.$store.getters['getSelectedCity'].name.toLowerCase()
    }
  }
}
</script>

<style scoped>
.my-nav {
  background-color: #ffa370;
}

a {
  color: white;
}
</style>
