<template>
  <div>
    <span slot="modal-title"
      >{{ complaint.title }} – {{ complaint.city.id }}</span
    >
    <div class="d-block text-center">
      <h3>Hello From This Modal!</h3>
    </div>
  </div>
</template>

<script>
export default {
  props: ['id'],
  computed: {
    complaint() {
      return this.$store.getters['getComplaintById'](this.id)
    },
    city() {
      return this.$store.getters['getCityById'](this.complaint.city.id)
    }
  }
}
</script>

<style lang="scss" scoped></style>
