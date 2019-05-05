<template>
  <span class="badge badge-pill badge-secondary">{{ label.name }}</span>
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

<style scoped>
.badge {
  background: #c4c4c4;
  border-radius: 13px;
  font-style: normal;
  font-weight: normal;
  font-size: 12px;
  line-height: 16px;
  margin: 6px 8px;
  margin-left: 0;
}
</style>
