<template>
  <div>
    <el-autocomplete
      class="inline-input"
      v-model="searchInput"
      :fetch-suggestions="querySearch"
      placeholder="City"
      :trigger-on-focus="false"
      @select="selectCity"
      @keyup.enter="selectCity"
      autofocus="true"
    ></el-autocomplete>
    <el-button @click="selectCity">Set</el-button>
  </div>
</template>

<script>
import Service from '@/services/Service.js'

export default {
  name: 'city-select',
  data() {
    return {
      cities: [],
      searchInput: ''
    }
  },
  created() {
    this.$store.dispatch('fetchUser', 1)
  },
  computed: {
    user() {
      return this.$store.getters['getUser']
    }
  },
  methods: {
    querySearch(queryString, cb) {
      var vals = this.cities
      var results = queryString
        ? vals.filter(this.createFilter(queryString))
        : vals
      // call callback function to return suggestions
      cb(results)
    },
    createFilter(queryString) {
      return v => {
        return v.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
      }
    },
    selectCity(e) {
      this.$store.dispatch('selectCity', { cityId: e.id, cityName: e.value })
      this.$router.push({
        name: 'home-city',
        params: { city: e.value.toLowerCase() }
      })
    }
  },
  mounted() {
    Service.getCities()
      .then(response => {
        response.data.forEach(e => {
          this.cities.push({ id: e.id, value: e.name })
        })
      })
      .catch(error => {
        console.log('error> ' + error.message)
      })
  }
}
</script>

<style>
.el-input__inner {
  width: 375px !important;
}

button.el-button {
  margin-left: 20px;
}
</style>
