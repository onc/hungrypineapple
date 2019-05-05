<template>
  <el-autocomplete
    class="inline-input"
    v-model="searchInput"
    :fetch-suggestions="querySearch"
    placeholder="What city sere you?"
    :trigger-on-focus="false"
    @select="selectCity"
    @keyup.enter="selectCity"
  ></el-autocomplete>
</template>

<script>
import Service from '@/services/Service.js'

export default {
  name: 'city-select',
  props: {
    city: {
      type: String,
      required: false
    }
  },
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
        name: 'home',
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
