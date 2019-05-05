<template>
  <span class="arrow-icon">
    <div
      v-on:click="upvote"
      :class="[
        complaint.is_upvote === null
          ? 'arrow-up-normal'
          : complaint.is_upvote
          ? 'arrow-up-active'
          : 'arrow-up-inactive',
        'arrow-up-icon'
      ]"
    />
    <div
      v-on:click="downvote"
      :class="[
        complaint.is_upvote === null
          ? 'arrow-down-normal'
          : complaint.is_upvote
          ? 'arrow-down-inactive'
          : 'arrow-down-active',
        'arrow-up-icon'
      ]"
    />
    <div v-on:click="downvote" :class="['arrow-down-icon']" />
    <div class="voting-label-up">{{ complaint.upvotes }}</div>
    <div class="voting-label-down">{{ complaint.downvotes }}</div>
  </span>
</template>

<script>
export default {
  name: 'VotingArrows',
  props: ['complaint', 'onUpvoteClick', 'onDownvoteClick'],
  methods: {
    upvote() {
      this.onUpvoteClick(this.complaint)
    },
    downvote() {
      this.onDownvoteClick(this.complaint)
    }
  }
}
</script>

<style scoped>
.arrow-icon {
  height: 67px;
  width: 35px;
  position: relative;
  float: left;
  margin: 20px;
}

.voting-label-up {
  top: 6px;
  left: 40px;
  position: absolute;
  font-weight: 800;
}

.voting-label-down {
  top: 36px;
  left: 40px;
  position: absolute;
  font-weight: 800;
}

.arrow-up-icon {
  width: 100%;
  height: 50%;
  background-repeat: no-repeat;
  top: 0;
  left: 0;
}

.arrow-down-icon {
  background-position: bottom;
  width: 100%;
  height: 50%;
}

.arrow-up-normal {
  background-image: url(/arrow_up.svg);
}
.arrow-down-normal {
  background-image: url(/arrow_down.svg);
}

.arrow-up-active {
  background-image: url(/arrow_up_active.svg);
}
.arrow-down-active {
  background-image: url(/arrow_down_active.svg);
}

.arrow-up-inactive {
  background-image: url(/arrow_up_inactive.svg);
}
.arrow-down-inactive {
  background-image: url(/arrow_down_inactive.svg);
}

.arrow-up-icon:hover {
  cursor: pointer;
}

.arrow-down-icon:hover {
  cursor: pointer;
}
</style>
