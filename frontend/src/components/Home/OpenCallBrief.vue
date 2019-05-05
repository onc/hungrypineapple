<template>
  <div class="full-height">
    <!-- <span>I am open call brief, ahaha.</span> -->

    <b-col class="full-height">
      <b-row style="height:65%">
        <b-col class="full-height">
          <div class="image-opencall">Image goes here</div>
        </b-col>
      </b-row>
      <b-row style="height:35%">
        <b-col>
          <div class="open-brief-title">{{ oppencall.title }}</div>
        </b-col>
      </b-row>
    </b-col>
  </div>
</template>

<script>
export default {
  props: ['opencallid'],
  computed: {
    oppencall() {
      return this.$store.getters['getOpencallById'](this.opencallid)
    }
  }
}
</script>

<style scoped>
.image-opencall {
  background-color: gray;
  background-image: url(/test.svg);
  background-repeat: no-repeat;
  background-size: cover;
  border-radius: 8px 8px 0px 0px;
  height: 100%;
  /* height: 100px; */
  /* width: 100px; */
}

.open-brief-title {
  font-size: 16px;
  font-weight: 600;
  text-align: left;
  padding: 8px;
  background-color: white;
  border-radius: 0px 0px 8px 8px;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.25);
  height: 100%;
}

.full-height {
  height: 100%;
}
</style>
