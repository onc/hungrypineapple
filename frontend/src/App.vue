<template>
  <div id="app">
    <transition name="moveInUp">
      <router-view :key="$route.fullPath" />
    </transition>
  </div>
</template>

<script>
export default {
  name: 'app',
  beforeCreate() {
    this.$store.dispatch('fetchUser', 1)
    this.$store.dispatch('fetchCities')
    this.$store.dispatch('fetchComplaints')
    this.$store.dispatch('fetchOpencalls')
    this.$store.dispatch('fetchLabels')
    this.$store.dispatch('fetchComplaintsForUser', { id: 1 })
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Nunito+Sans');

#app {
  font-family: 'Nunito Sans', sans-serif;
  /* font-family: 'Avenir', Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 1000px;
  /* margin-top: 60px; */
}

body {
  background-color: #eee;
  color: #2c3e50;
}
</style>
