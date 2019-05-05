<template>
<div v-if="complaint" class="complaint-item">
  <VotingArrows :complaint="complaint"
                :onUpvoteClick="upvote"
                :onDownvoteClick="downvote"/>
  <span class="complaint-details">
    <div class="complaint-title">{{ complaint.title }}</div>
    <div class="complaint-description">{{ complaint.description }}</div>
    <div class="complaint-labels">
      <span v-bind:key="item.id" class="complaint-label" v-for="item in labels">{{ item.name }}</span>
    </div>
  </span>
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
      console.log('upvoting: ', complaint);
    },
    downvote(complaint) {
      console.log('downvoting: ', complaint);
    }
  },
  computed:  {
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
    margin: 8px 32px 8px 32px;
    border-radius: 8px;
    display: inline-block;
}

.complaint-details {
    display: inline-block;
    float: left;
    margin: 20px;
}

.complaint-title {
    font-size: 16px;
    font-weight: 600;
    text-align: left;
}

.complaint-description {
    font-size: 16px;
    font-weight: 400;
    text-align: left;
}

.complaint-labels {
    float: left;
}

.complaint-label {
    background: #C4C4C4;
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
