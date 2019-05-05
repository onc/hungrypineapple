<template>
  <div>
    <h2>Complaints</h2>
    <div :key="item.id" v-for="item in complaintsForUser">
      <ComplaintItem :complaint="item" />
    </div>
  </div>
</template>

<script>
import ComplaintItem from '@/components/Home/ComplaintItem.vue'

export default {
  name: 'Complaints',
  props: ['city'],
  components: {
    ComplaintItem
  },
  computed: {
    user() {
      return this.$store.getters['getUser']
    },
    complaintsForUser() {
      return this.$store.getters['getComplaintsForUser']
    }
  },
  watch: {
    user(newUser) {
      this.$store.dispatch('fetchComplaintsForUser', newUser)
    }
  },
  beforeMounted() {
    this.$store.dispatch('fetchComplaintsForUser', { id: 1 })
  }
}
</script>

<style scoped></style>
