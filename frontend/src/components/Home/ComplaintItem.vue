<template>
  <div v-if="complaint" class="complaint-item">
    <b-col cols="2" class="voting">
      <VotingArrows
        :complaint="complaint"
        :onUpvoteClick="upvote"
        :onDownvoteClick="downvote"
      />
    </b-col>
    <b-col cols="10" class="complaint-details">
      <b-row>
        <b-col style="padding:0px">
          <div class="complaint-title">
            {{ complaint.title }}
            <svg style="width:40px; height:20px;">
              <circle cx="28" cy="8" r="8" fill="#68D89B"></circle>
            </svg>
          </div>
        </b-col>
        <!-- <b-col></b-col> -->
      </b-row>
      <b-row>
        <div class="complaint-description">{{ complaint.description }}</div>
      </b-row>
      <b-row>
        <div class="complaint-labels">
          <span
            v-bind:key="item.id"
            class="complaint-label"
            v-for="item in labels"
            >{{ item.name }}</span
          >
        </div>
      </b-row>
    </b-col>
    <!-- 
    <span class="complaint-details">
      <div class="complaint-title">{{ complaint.title }}</div>
      <div class="complaint-description">{{ complaint.description }}</div>
      <div class="complaint-labels">
        <span
          v-bind:key="item.id"
          class="complaint-label"
          v-for="item in labels"
          >{{ item.name }}</span
        >
      </div>
    </span>-->
  </div>
</template>

<script>
import VotingArrows from '@/components/VotingArrows.vue'

export default {
  name: 'ComplaintItem',
  props: ['complaint'],
  components: {
    VotingArrows
  },
  methods: {
    upvote(complaint) {
      console.log('upvoting: ', complaint)
    },
    downvote(complaint) {
      console.log('downvoting: ', complaint)
    }
  },
  computed: {
    labels() {
      return this.complaint.labels
    }
  }
}
</script>

<style scoped>
.complaint-item {
  width: 100%;
  background-color: white;
  margin: 8px 0px 8px 0px;
  border-radius: 8px;
  display: inline-block;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.25);
}

.complaint-details {
  display: inline-block;
  /* float: left; */
  margin: 20px;
}

.complaint-title {
  /* display: inline-block; */
  font-size: 20px;
  font-weight: 600;
  text-align: left;
  margin-bottom: 4px;
}

.complaint-description {
  font-size: 16px;
  font-weight: 400;
  text-align: left;
  margin-bottom: 6px;
}

.complaint-labels {
  float: left;
}

.complaint-label {
  background: #c4c4c4;
  border-radius: 13px;
  padding: 5px;
  min-width: 75px;
  height: 25px;
  margin: 3px;
  margin-right: 10px;
  line-height: 16px;
  display: inline-block;
  font-size: 12px;
  color: white;
}
</style>
