<template>
  <div style="margin: 10px">
    <!-- <span>I am open call brief, ahaha.</span> -->

    <b-col>
      <b-row style="height:100px">
        <b-col>
          <div class="image-opencall">Image goes here</div>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <h3>Title</h3>
        </b-col>
      </b-row>
    </b-col>
  </div>
</template>

<script>
export default {
  props: ['opencallid'],
  computed: {
    coopencallmplaint() {
      return this.$store.getters['getOpencallById'](this.opencallid)
    }
  }
}
</script>

<style scoped>
.image-opencall {
  background-color: white;
  border-radius: 10px;
  /* height: 100%; */
  height: 100px;
  /* width: 100px; */
}

h3 {
  font-size: 16px;
  font-weight: 600;
  text-align: left;
}
</style>
