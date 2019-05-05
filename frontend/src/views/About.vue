<template>
  <div class="about">
    <h1>This is an about page</h1>
    <ComplaintFormModal />
  </div>
</template>

<script>
import ComplaintFormModal from '@/components/ComplaintFormModal.vue'

export default {
  name: 'About',
  components: {
    ComplaintFormModal
  }
}
</script>
