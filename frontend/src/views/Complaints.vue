<template>
  <div style="height:100%">
    <Navbar></Navbar>
    <b-container>
      <b-row class="header-part" style="height:30%; background-color:white">
        <b-col style="padding:0.8em">
          <b-row>
            <div class="card-title">Complaints</div>
          </b-row>
          <b-row>
            <!-- <b-col cols="1"></b-col>
            <b-col cols="10">-->
            <b-col>
              <SearchField></SearchField>
            </b-col>
            <!-- </b-col>
            <b-col cols="1"></b-col>-->
          </b-row>
          <b-row style="padding:1em;">
            <b-col>
              <h3>Filters</h3>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-dropdown
                text="Category"
                variant="outline-dark"
                style="width:100%"
                class="shadow-box"
              >
                <b-dropdown-item href="#">An item</b-dropdown-item>
                <b-dropdown-item href="#">Another item</b-dropdown-item>
              </b-dropdown>
            </b-col>
            <b-col>
              <b-dropdown
                text="State"
                variant="outline-dark"
                style="width:100%"
                class="shadow-box"
              >
                <b-dropdown-item href="#">An item</b-dropdown-item>
                <b-dropdown-item href="#">Another item</b-dropdown-item>
              </b-dropdown>
            </b-col>
            <b-col>
              <b-dropdown
                text="Date"
                variant="outline-dark"
                style="width:100%"
                class="shadow-box"
              >
                <b-dropdown-item href="#">An item</b-dropdown-item>
                <b-dropdown-item href="#">Another item</b-dropdown-item>
              </b-dropdown>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
      <b-row style="height:10%;padding:20px;">
        <b-col cols="9"></b-col>
        <b-col style="padding-right:0em">
          <b-button class="bootstrap-botton-color"
            >Submit a new complaint</b-button
          >
        </b-col>
      </b-row>
      <b-row style="height:60%;">
        <b-col>
          <b-row style="padding:0em 0.8em 0em 0.8em">
            <b-col cols="9">
              <div class="category-title">Most discussed</div>
            </b-col>
            <b-col cols="3">
              <b-dropdown
                text="Order by popularity"
                variant="outline-dark"
                style="width:100%"
                class="shadow-box"
              >
                <b-dropdown-item href="#">An item</b-dropdown-item>
                <b-dropdown-item href="#">Another item</b-dropdown-item>
              </b-dropdown>
            </b-col>
          </b-row>
          <b-row v-bind:key="item.id" v-for="item in complaintsForUser">
            <b-col>
              <ComplaintItem :complaint="item" />
            </b-col>
          </b-row>
        </b-col>
      </b-row>
      <!-- <div v-bind:key="item.id" v-for="item in complaintsForUser">
        <ComplaintItem :complaint="item" />
      </div>-->
    </b-container>
    <!-- <div style="height:30%; background-color:while"></div> -->
    <!-- <h2>Complaints</h2> -->
  </div>
</template>

<script>
import ComplaintItem from '@/components/Home/ComplaintItem.vue'
import Navbar from '@/components/Navbar.vue'
import SearchField from '@/components/SearchField.vue'

export default {
  name: 'Complaints',
  props: ['city'],
  components: {
    ComplaintItem,
    Navbar,
    SearchField
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

<style scoped>
.header-part {
  /* margin: 10px; */
  margin-bottom: 10px;
  padding: 8px;
  background-color: white;
  /* height: 45px; */
  border-radius: 0px 0px 8px 8px;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.25);
}

.shadow-box {
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.25);
}
</style>
