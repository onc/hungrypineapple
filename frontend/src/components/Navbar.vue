<template>
  <b-navbar toggleable="lg" class="my-nav">
    <b-navbar-brand href="#" variant="info">Home page</b-navbar-brand>

    <!-- Right aligned nav items -->
    <b-navbar-nav class="ml-auto">
      <b-nav-item class="nav-text" href="/complaints">Complaints</b-nav-item>
      <b-nav-item class="nav-text" href="/opencalls">Open Calls</b-nav-item>
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
  }
}
</script>

<style scoped>
.my-nav {
  background-color: #ffa370;
}
</style>
