<template>
<div>
  <h2>Complaints</h2>
  <div v-bind:key="item.id" v-for="item in complaintsForUser">
    <ComplaintItem :complaint="item" />
  </div>
</div>
</template>

<script>
import ComplaintItem from '@/components/Home/ComplaintItem.vue'

export default {
  name: 'complaints',
  data: function() {
    return {}
  },
  components: {
    ComplaintItem
  },
  computed: {
    user() {
      return this.$store.getters.getUser
    },
    complaintsForUser() {
      return this.$store.getters.getComplaintsForUser
    }
  },
  watch: {
    user(newUser) {
      this.$store.dispatch('fetchComplaintsForUser', newUser);
    },
  }
}
</script>

<style scoped></style>
