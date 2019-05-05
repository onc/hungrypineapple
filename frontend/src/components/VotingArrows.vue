<template>
<span class="arrow-icon">
  <div class="arrow-down-icon" />
  <div class="arrow-up-icon" />
  <div class="voting-label-up">
    {{ complaint.upvotes }}
  </div>
  <div class="voting-label-down">
    {{ complaint.downvotes }}
  </div>
</span>
</template>

<script>
export default {
  name: 'VotingArrows',
  props: ['complaint', 'onUpvoteClick', 'onDownvoteClick'],
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

.arrow-icon:hover {
    cursor: pointer;
}

.voting-label-up {
    top: 6px;
    left: 40px;
    position: absolute;
}

.voting-label-down {
    top: 36px;
    left: 40px;
    position: absolute;
}

.arrow-up-icon {
    background-image: url(/arrow_up.svg);
    width: 100%;
    height: 100%;
    background-repleat: no-repeat;
    top: 0;
    left: 0;
    position: absolute;
}

.arrow-down-icon {
    background-image: url(/arrow_down.svg);
    background-position: bottom;
    width: 100%;
    height: 100%;
}
</style>
