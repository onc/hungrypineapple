<template>
  <div class="complaint-brief-div">
    <b-row class="my-auto">
      <b-col cols="1" class="status my-auto">
        <svg style="width:20px; height:20px;">
          <circle cx="8" cy="8" r="8" fill="black"></circle>
        </svg>
      </b-col>
      <b-col cols="6" class="complaint-title my-auto">
        <h3>{{ complaint.title }}</h3>
      </b-col>
      <b-col cols="2" class="voting-buttons my-auto">Voting</b-col>
      <b-col cols="2" class="show-me-button my-auto">
        <b-button
          v-b-modal="`complaint-modal-${complaintid}`"
          variant="outline-secondary"
          size="sm"
          >Show</b-button
        >
        <b-modal :id="`complaint-modal-${complaintid}`" size="lg" hide-header>
          <ComplaintModal></ComplaintModal>
        </b-modal>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import ComplaintModal from '@/components/ComplaintModal.vue'

export default {
  components: {
    ComplaintModal
  },
  props: ['complaintid'],
  computed: {
    complaint() {
      return this.$store.getters['getComplaintById'](this.complaintid)
    }
  }
}
</script>

<style scoped>
.complaint-brief-div {
  margin: 10px;
  padding: 8px;
  background-color: white;
  height: 45px;
}

h3 {
  font-size: 16px;
  font-weight: 600;
  text-align: left;
}
</style>
