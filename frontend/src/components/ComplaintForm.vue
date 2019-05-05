<template>
  <div>
    <b-row>
      <b-col style="width:600px;">
        <b-form
          @submit="submit"
          @reset="reset"
          style="text-align:left; margin-top:30px;"
        >
          <b-form-group
            label="Title of your complaint"
            label-for="inline-form-input-name"
          >
            <!-- <b-label>Description</b-label> -->
            <b-input
              id="inline-form-input-name"
              class="mb-2 mr-sm-2 mb-sm-0"
              v-model="form.title"
              placeholder="Give a descriptive title for your complaint..."
            ></b-input>
          </b-form-group>

          <!-- <b-row></b-row> -->
          <b-form-group label="Description" label-for="textarea">
            <b-form-textarea
              id="textarea"
              v-model="form.description"
              placeholder="Describe your complaint..."
              rows="3"
              max-rows="8"
            ></b-form-textarea>
          </b-form-group>

          <b-row></b-row>
          <div>
            <div class="title-form">Choose category</div>
            <span
              v-bind:key="label.id"
              :id="label.id"
              class="complaint-label"
              v-on:click="assignLabel"
              v-for="label in unassignedLabels"
              >{{ label.name }}</span
            >
          </div>

          <div style="margin-top:15px;">
            <div class="title-form">Assigned Category</div>
            <span
              v-bind:key="label.id"
              :id="label.id"
              class="complaint-label"
              v-on:click="unassignLabel"
              v-for="label in form.labels"
              >{{ label.name }}</span
            >
          </div>

          <div style=" margin-top:30px">
            <b-button
              class="bootstrap-botton-color"
              style="margin:10px;"
              type="submit"
              variant="primary"
              >Submit</b-button
            >
            <b-button
              type="reset"
              style="background-color:#c4c4c4; border:none; 
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.25);"
              variant="danger"
              >Cancel</b-button
            >
          </div>
        </b-form>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: 'CompaintForm',
  data() {
    return {
      form: {
        title: '',
        description: '',
        labels: []
      }
    }
  },
  props: ['onSubmit', 'onReset'],
  computed: {
    user() {
      return this.$store.getters['getUser']
    },
    labels() {
      return this.$store.getters.getLabels
    },
    unassignedLabels() {
      return this.$store.getters.getLabels.filter(label => {
        return !this.form.labels.includes(label)
      })
    }
  },
  methods: {
    assignLabel(event) {
      const labelID = event.target.id
      const label = this.unassignedLabels.filter(
        label => label.id == labelID
      )[0]
      this.form.labels.push(label)
    },
    unassignLabel(event) {
      const labelID = event.target.id
      const labels = this.form.labels.filter(label => label.id != labelID)
      this.form.labels = labels
    },
    submit(evt) {
      evt.preventDefault()
      const formData = this.form
      formData.complainer = this.user.id
      formData.labels = Array.from(formData.labels, label => label.id)
      formData.city = 1
      this.onSubmit(evt, formData)
    },
    reset(evt) {
      evt.preventDefault()
      this.onReset(evt)
    }
  }
}
</script>

<style scoped>
.complaint-label {
  background: #c4c4c4;
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

.complaint-label:hover {
  cursor: pointer;
}

.title-form {
  font-weight: 800;
}
</style>
