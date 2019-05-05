<template>
  <div style="height:100%">
    <Navbar></Navbar>
    <b-container>
      <b-row style="height:30%; background-color:white">
        <b-col>
          <div class="card-title">Complaint</div>
        </b-col>
      </b-row>
      <div v-bind:key="item.id" v-for="item in complaintsForUser">
        <ComplaintItem :complaint="item" />
      </div>
    </b-container>
    <!-- <div style="height:30%; background-color:while"></div> -->
    <!-- <h2>Complaints</h2> -->
  </div>
</template>

<script>
import ComplaintItem from '@/components/Home/ComplaintItem.vue'
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'Complaints',
  props: ['city'],
  components: {
    ComplaintItem,
    Navbar
  },
  computed: {
    user() {
      return this.$store.getters.getUser
    },
    complaintsForUser() {
      return this.$store.getters.getComplaintsForUser
    }
  },
  watch: {
    user(newUser) {
      this.$store.dispatch('fetchComplaintsForUser', newUser)
    }
  }
}
</script>

<style scoped></style>
