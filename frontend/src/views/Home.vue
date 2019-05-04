<template>
  <div class="main-container" style="height:100%">
    <b-navbar toggleable="lg" variant="info">
      <b-navbar-brand href="#">Home page</b-navbar-brand>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item href="#">Complaints</b-nav-item>
        <b-nav-item href="#">Open Calls</b-nav-item>
        <b-nav-item href="#">Login</b-nav-item>
        <b-nav-item href="#">Sign up</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <b-container class="h-100">
      <b-row style="height:40%">
        <b-col class="my-auto">
          <b-row>
            <b-col class="my-auto">
              <h1>Help us improve {{ city }}</h1>
            </b-col>
          </b-row>
          <b-row>
            <b-col class="w-25"></b-col>
            <b-col class="w-50">
              <template>
                <input
                  class="form-control"
                  type="text"
                  placeholder="Search"
                  aria-label="Search"
                />
              </template>
            </b-col>
            <b-col class="w-25"></b-col>
          </b-row>
        </b-col>
      </b-row>
      <b-row class="complaints-container" style="height:30%">
        <b-col cols="5">
          <h2>What people complain about?</h2>
        </b-col>
        <b-col cols="1"></b-col>
        <b-col cols="6">
          <b-row v-for="complaint in complaints" :key="complaint.id">
            <b-col>
              <ComplaintBrief :complaintid="complaint.id"></ComplaintBrief>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <span class="see-more">See more</span>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
      <b-row class="opencalls-container" style="height:30%">
        <b-col cols="5">
          <h2>What you can help with?</h2>
        </b-col>
        <b-col cols="1"></b-col>
        <b-col cols="6">
          <b-row>
            <b-col v-for="opencall in opencalls" :key="opencall.id">
              <OpenCallBrief :opencallid="opencall.id"></OpenCallBrief>
            </b-col>
            <!-- <b-col>
              <OpenCallBrief></OpenCallBrief>
            </b-col>
            <b-col>
              <OpenCallBrief></OpenCallBrief>
            </b-col>-->
          </b-row>
          <b-row>
            <b-col>
              <!-- <b-button>See more</b-button> -->
              <span class="see-more" href="#">See more</span>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
    </b-container>
    <!-- <el-container>
    <el-header>
      <h1>Sere mě {{ city }}</h1>
      <Navbar />
    </el-header>

    <el-main>
      <el-card shadow="always" v-for="complaint in complaints">Always</el-card>
    </el-main>
    </el-container>-->
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import ComplaintBrief from '@/components/Home/ComplaintBrief.vue'
import OpenCallBrief from '@/components/Home/OpenCallBrief.vue'

export default {
  components: {
    Navbar,
    ComplaintBrief,
    OpenCallBrief
  },
  props: ['city'],
  beforeCreate() {
    this.$store.dispatch('fetchComplaints')
  },
  computed: {
    complaints() {
      return this.$store.state['data'].complaints
    },
    opencalls() {
      return this.$store.state['data'].opencalls
    }
  }
}
</script>

<style>
.main-container {
  background-color: #eee;
}

.see-more {
  font-weight: bold;
  cursor: pointer;
}

h1 {
  font-size: 64px;
  font-weight: 800;
}

h2 {
  font-size: 48px;
  font-weight: 800;
  text-align: right;
}

h3 {
  font-size: 16px;
  font-weight: 600;
  text-align: left;
}
</style>
