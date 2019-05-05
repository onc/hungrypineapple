<template>
<div>
  <h2>Complaints</h2>
  {{ complaintsForUser }}
</div>
</template>

<script>
export default {
  name: 'complaints',
  data: function() {
    return {}
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

<style lang="scss" scoped></style>
