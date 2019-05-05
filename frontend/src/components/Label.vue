<template>
  <div>
    <span class="badge badge-pill badge-secondary">{{ label.name }}</span>
  </div>
</template>

<script>
export default {
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  computed: {
    label() {
      return this.$store.getters['getLabelById'](this.id)
    }
  }
}
</script>

<style lang="scss" scoped></style>
