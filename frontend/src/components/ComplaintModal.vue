<template>
  <div>
    <span slot="modal-title"
      >{{ complaint.title }} – {{ city.name }} – {{ complaint.labels }}</span
    >
    <span class="labels">
      <Label v-for="label in complaint.labels" :key="label.id" :id="label.id" />
    </span>
    <div class="d-block text-center">
      <h3>Hello From This Modal!</h3>
    </div>
  </div>
</template>

<script>
import Label from '@/components/Label.vue'

export default {
  components: {
    Label
  },
  props: ['id'],
  computed: {
    complaint() {
      return this.$store.getters['getComplaintById'](this.id)
    },
    city() {
      return this.$store.getters['getCityById'](this.complaint.city)
    }
  },
  mounted() {
    console.log(this.complaint.labels)
  }
}
</script>

<style lang="scss" scoped></style>
