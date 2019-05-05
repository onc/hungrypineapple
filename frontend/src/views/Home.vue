<template>
  <div class="main-container" style="height:100%">
    <Navbar :city="city" />

    <b-modal
      v-model="showCitySelection"
      hide-footer="true"
      hide-header="true"
      cancel-disabled
      no-close-on-esc
      no-close-on-backdrop
      centered="true"
    >
      <h3 style="text-align:left; font-size: 26px">Choose your city:</h3>
      <CitySelection />
    </b-modal>

    <b-container class="h-100">
      <b-row style="height:35%">
        <b-col class="my-auto">
          <b-row>
            <b-col class="my-auto">
              <div class="main-title">
                Help us improve
                <a class="change-city" @submit="">{{
                  (city ? city : '…') | capitalize
                }}</a>
              </div>
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
      <b-row style="height:10%"></b-row>
      <b-row class="complaints-container" style="height:30%">
        <b-col cols="5" class="complaints-titles">
          <b-row>
            <b-col>
              <h2>What people complain about?</h2>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <h5>
                Don’t feel in Brno as in your city? Look what others are
                complaining about and help the change!
              </h5>
            </b-col>
          </b-row>
        </b-col>
        <b-col cols="1"></b-col>
        <b-col cols="6">
          <b-row v-for="(complaint, index) in complaints" :key="complaint.id">
            <b-col v-if="index < 3">
              <ComplaintBrief :complaintid="complaint.id"></ComplaintBrief>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <span class="see-more">
                <router-link :to="{ path: `/city/${city}/complaints` }"
                  >See more</router-link
                >
              </span>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
      <b-row class="opencalls-container" style="height:25%">
        <b-col cols="5">
          <b-row>
            <b-col>
              <h2>What you can help with?</h2>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <h5>
                Do you have special skills and want to help your city? Offer
                your help and improve the quality of everyone’s life!
              </h5>
            </b-col>
          </b-row>
        </b-col>
        <b-col cols="1"></b-col>
        <b-col cols="6">
          <b-row style="height:60%">
            <b-col
              v-for="(opencall, index) in opencalls"
              :key="opencall.id"
              style="padding: inherit; height: 100%"
            >
              <OpenCallBrief
                :opencallid="opencall.id"
                v-if="index < 3"
              ></OpenCallBrief>
            </b-col>
          </b-row>
          <b-row>
            <b-col style="padding-top:15px;">
              <span class="see-more">
                <router-link :to="{ path: `/city/${city}/opencalls` }"
                  >See more</router-link
                >
              </span>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import ComplaintBrief from '@/components/Home/ComplaintBrief.vue'
import OpenCallBrief from '@/components/Home/OpenCallBrief.vue'
import Navbar from '@/components/Navbar.vue'
import CitySelection from '@/components/Home/CitySelection.vue'

/*let options = {
  shouldSort: true,
  threshold: 0.6,
  location: 0,
  distance: 100,
  maxPatternLength: 32,
  minMatchCharLength: 2,
  keys: ['title', 'description']
}*/
/*var fuse = new Fuse(list, options); // "list" is the item array
var result = fuse.search("");
*/
export default {
  components: {
    ComplaintBrief,
    OpenCallBrief,
    Navbar,
    CitySelection
  },
  props: ['city'],
  data() {
    return {
      showCitySelection: false
    }
  },
  computed: {
    complaints() {
      return this.$store.state['data'].complaints
    },
    opencalls() {
      return this.$store.state['data'].opencalls
    }
  },
  mounted() {
    this.showCitySelection = this.$route.name !== 'home-city'
  }
}
</script>

<style>
.main-container {
  background-color: #eee;
  background-image: url(/lady.svg);
  background-repeat: no-repeat;
  background-size: 100%;
}

.complaints-titles {
  color: white;
}

@media screen and (max-width: 1600px) {
  .complaints-titles {
    color: #2c3e50;
  }
}

.nav-text a {
  color: white !important;
}

.nav-text {
  font-weight: 800;
  padding: 0px 10px 0px 10px;
}

.see-more {
  font-weight: bold;
  cursor: pointer;
}
.see-more a {
  color: #2c3e50 !important;
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

h5 {
  font-size: 18px;
  font-weight: 600;
  text-align: right;
}

.change-city {
}

.main-title {
  display: inline-block;
  color: white;
  /* color: white; */
  font-size: 64px;
  font-weight: 900;
  padding-bottom: 0.4em;
}

.card-title {
  /* display: inline-block; */
  /* color: white; */
  /* color: white; */
  font-size: 64px;
  font-weight: 900;
  padding-bottom: 0.4em;
  padding-left: 0.4em;
  padding-top: 0.8em;
  text-align: left;
}

.category-title {
  font-size: 26px;
  font-weight: 900;
  padding-bottom: 0.4em;
  /* padding-left: 0.4em; */
  /* padding-top: 0.8em; */
  text-align: left;
}

.bootstrap-botton-color {
  background-color: #ffa370;
  border-style: none;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.25);
}

@media screen and (max-width: 1200px) {
  .main-title {
    color: #2c3e50;
  }
}
</style>
