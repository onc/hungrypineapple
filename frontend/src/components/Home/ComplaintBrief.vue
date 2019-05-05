<template>
  <div class="complaint-brief-div">
    <b-row class="my-auto">
      <b-col cols="1" class="status my-auto">
        <svg style="width:20px; height:20px;">
          <circle cx="8" cy="8" r="8" fill="#68D89B"></circle>
        </svg>
      </b-col>
      <b-col cols="7" class="my-auto">
        <div class="complaint-title">{{ complaint.title }}</div>
      </b-col>
      <b-col cols="2">
        <div class="voting-overview"></div>
      </b-col>
      <b-col cols="2" class="show-me-button my-auto" style="padding-left:0px">
        <b-button
          v-b-modal="`complaint-modal-${complaintid}`"
          variant="outline-secondary"
          size="sm"
          >Show</b-button
        >
        <b-modal
          :id="`complaint-modal-${complaintid}`"
          size="lg"
          hide-header
          hide-footer
        >
          <ComplaintModal :id="complaintid"></ComplaintModal>
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
  border-radius: 8px;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.25);
}

.complaint-title {
  font-size: 16px;
  font-weight: 600;
  text-align: left;
  white-space: nowrap;
  width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
}

.voting-overview {
  width: 100%;
  height: 100%;
  background-image: url(/mock-voting.svg);
  padding-left: 8px;
  background-repeat: no-repeat;
  background-position: right;
}
</style>
