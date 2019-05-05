<template>
  <b-container id="modal">
    <b-row>
      <b-col cols="8">
        <b-row>
          <h2 slot="modal-title">
            {{ complaint.title }}
            <span class="city-name">– {{ complaint.city.name }}</span>
          </h2>
        </b-row>

        <b-row>
          <span class="labels">
            <Label
              v-for="label in complaint.labels"
              :key="label.id"
              :id="label.id"
            ></Label>
          </span>
        </b-row>

        <b-row>
          <div class="content">{{ complaint.description }}</div>
        </b-row>

        <b-row>
          <div class="content content-small">
            Posted {{ complaint.created_at | formatDate }}
          </div>
        </b-row>
      </b-col>

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
import Label from '@/components/Label.vue'
import Vue from 'vue'
import moment from 'moment'
Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('MM/DD/YYYY hh:mm')
  }
})

export default {
  components: {
    Label
  },
  props: ['id'],
  computed: {
    complaint() {
      return this.$store.getters['getComplaintById'](this.id)
    }
  },
  methods: {
    close() {
      this.$emit('modal-close')
    }
  }
}
</script>

<style scoped>
#modal {
  padding: 16px 34px;
}

h2 {
  text-align: left;
  font-weight: bold;
  font-style: normal;
  font-size: 32px;
  line-height: 44px;
}

span.city-name {
  font-weight: normal;
  color: #808080;
}

div.content {
  margin-top: 10px;
  font-style: normal;
  font-weight: normal;
  font-size: 14px;
  line-height: 19px;
  text-align: left !important;
}

div.content-small {
  font-size: 10px;
  line-height: 14px;
}
</style>
