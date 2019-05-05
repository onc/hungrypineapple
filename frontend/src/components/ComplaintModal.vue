<template>
  <b-container id="modal">
    <b-row>
      <b-col cols="9" class="left-part">
        <b-row>
          <b-col>
            <b-row>
              <h2 slot="modal-title">
                {{ complaint.title }}
                <span class="city-name">– {{ complaint.city.name }}</span>
              </h2>
            </b-row>

            <b-row>
              <span class="labels">
                <Label
                  v-for="label in complaint.labels"
                  :key="label.id"
                  :id="label.id"
                ></Label>
              </span>
            </b-row>

            <b-row>
              <div class="content">{{ complaint.description }}</div>
            </b-row>

            <b-row>
              <div class="content content-small">
                Posted by
                <span class="gray-font">Jan Polák</span>
                on {{ complaint.created_at | formatDate }}
              </div>
            </b-row>
          </b-col>
          <!-- 
          <b-col cols="4">
            <b-row>
              <button type="button" class="close" @click="close">
                <span aria-hidden="true">&times;</span>
              </button>
            </b-row>
          </b-col>-->
        </b-row>
        <b-row style="margin-top:50px;">
          <h2>
            Response from
            <span class="gray-font">Brno Townhall</span>
          </h2>
        </b-row>
        <b-row>
          <b-col class="content" style="padding-left:0px;">
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi
            imperdiet, mauris ac auctor dictum, nisl ligula egestas nulla, et
            sollicitudin sem purus in lacus. Sed ac dolor sit amet purus
            malesuada congue. Nullam feugiat, turpis at pulvinar vulputate, erat
            libero tristique tellus.
          </b-col>
        </b-row>
        <b-row>
          <b-col style="padding-left: 0px; margin-top: 20px;">
            <h3>Is this solution helpful?</h3>
          </b-col>
        </b-row>
        <b-row>
          <b-col style="padding-left:0px;">
            <div class="srdicka"></div>
          </b-col>
        </b-row>
        <b-row style="margin-top:50px;">
          <h2>Related Open Calls</h2>
        </b-row>
        <b-row>
          <b-col style="padding-left:0px;">Semkajc jde ukazka opencalls</b-col>
        </b-row>
      </b-col>
      <b-col cols="3" class="right-part my-auto">
        <b-row style="margin-bottom:50px;">
          <b-col cols="1"></b-col>
          <b-col class="my-auto">
            <VotingArrows
              :complaint="complaint"
              :onUpvoteClick="upvote"
              :onDownvoteClick="downvote"
            />
          </b-col>
        </b-row>
        <b-row class="my-auto">
          <b-col class="my-auto">
            <b-button size="sm" class="bootstrap-botton-color round"
              >Subscribe</b-button
            >
          </b-col>
        </b-row>
        <b-row>
          <b-col class="my-auto">
            <b-row style="margin-top:20px">
              <b-col cols="2"></b-col>
              <b-col cols="2">
                <div class="fb"></div>
              </b-col>
              <b-col cols="2">
                <div class="twitter"></div>
              </b-col>
              <b-col cols="2">
                <div class="insta"></div>
              </b-col>
            </b-row>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <div class="timeline"></div>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Label from '@/components/Label.vue'
import VotingArrows from '@/components/VotingArrows.vue'
import Vue from 'vue'
import moment from 'moment'
Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('MM/DD/YYYY hh:mm')
  }
})

export default {
  components: {
    Label,
    VotingArrows
  },
  props: ['id'],
  computed: {
    complaint() {
      return this.$store.getters['getComplaintById'](this.id)
    }
  },
  methods: {
    close() {
      this.$emit('modal-close')
    }
  }
}
</script>

<style scoped>
#modal {
  padding: 16px 34px;
}

.gray-font {
  color: gray;
}

.srdicka {
  background-image: url(/srdicka.svg);
  background-repeat: no-repeat;
  background-position: left;
  /* padding-left: -20px; */
  width: 100%;
  height: 20px;
}

h2 {
  text-align: left;
  font-weight: bold;
  font-style: normal;
  font-size: 32px;
  line-height: 44px;
}

span.city-name {
  font-weight: normal;
  color: #808080;
}

div.content {
  margin-top: 10px;
  font-style: normal;
  font-weight: normal;
  font-size: 14px;
  line-height: 19px;
  text-align: left !important;
}

div.content-small {
  font-size: 10px;
  line-height: 14px;
}

.round {
  border-radius: 20px;
  stroke: #ffa370;
  width: 90px;
}

.fb {
  /* width: 100%;
  height: 100%; */
  width: 40px;
  height: 100px;
  background-image: url(/fb.svg);
  background-repeat: no-repeat;
}

.twitter {
  /* width: 100%;
  height: 100%; */
  width: 40px;
  height: 100px;
  background-image: url(/twitter.svg);
  background-repeat: no-repeat;
}

.insta {
  /* width: 100%;
  height: 100%; */
  width: 40px;
  height: 100px;
  background-image: url(/insta.svg);
  background-repeat: no-repeat;
}
.timeline {
  /* width: 100%;
  height: 100%; */
  width: 150px;
  height: 280px;
  background-image: url(/timeline.svg);
  background-repeat: no-repeat;
  /* background-position: right; */
}
</style>
