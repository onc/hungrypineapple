<template>
<b-container id="modal">
  <b-row>
    <b-col cols="8">
      <b-row>
        <h2 slot="modal-title">
          What's your complaint?
        </h2>
      </b-row>
    </b-col>
    
    <ComplaintForm :onSubmit="submit" :onReset="reset"/>
    
    <b-col cols="4">
      <b-row>
        <button type="button" class="close" @click="close">
          <span aria-hidden="true">&times;</span>
        </button>
      </b-row>
    </b-col>
  </b-row>
</b-container>
</template>

<script>
import ComplaintForm from '@/components/ComplaintForm.vue';

export default {
  name: 'ComplaintFormModal',
  props: ['onClose'],
  components: {
    ComplaintForm
  },
  methods: {
    close() {
      this.$emit('modal-close')
    },
    submit(evt, data) {
      this.$store.dispatch('createComplaint', data);
      this.onClose();
    },
    reset(evt) {
      this.onClose();
    }
  }
}
</script>
