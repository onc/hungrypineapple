<template>
  <div id="app">
    <router-view :key="$route.fullPath" />
  </div>
</template>

<script>
export default {
  name: 'app',
  components: {
  },
  beforeCreate() {
    this.$store.dispatch('fetchUser', 1)
  components: {},
  beforeCreate() {
    this.$store.dispatch('fetchCities')
    this.$store.dispatch('fetchComplaints')
    this.$store.dispatch('fetchLabels')
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
</style>
