<template>
  <div>
    <b-form @submit="submit" @reset="reset" inline>
      <b-form-group>
        <b-input
          id="inline-form-input-name"
          class="mb-2 mr-sm-2 mb-sm-0"
          v-model="form.title"
          placeholder="Give a descriptive title for your complaint..."
          ></b-input>
      </b-form-group>

      <b-form-group>
        <b-form-textarea
          id="textarea"
          v-model="form.description"
          placeholder="Describe your complaint..."
          rows="3"
          max-rows="6"
          ></b-form-textarea>
      </b-form-group>

      <div>
        <span>Labels</span>
        <span v-bind:key="label.id"
              :id="label.id"
              class="complaint-label"
              v-on:click="assignLabel"
              v-for="label in unassignedLabels">
          {{ label.name }}
        </span>
      </div>

      <div>
        <span>Assigned Labels</span>
        <span v-bind:key="label.id"
              :id="label.id"
              class="complaint-label"
              v-on:click="unassignLabel"
              v-for="label in form.labels">
          {{ label.name }}
        </span>
      </div>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Cancel</b-button>
    </b-form>
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
        labels: [],
      },
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
      const labelID = event.target.id;
      const label = this.unassignedLabels.filter(label => label.id == labelID)[0];
      this.form.labels.push(label);
    },
    unassignLabel(event) {
      const labelID = event.target.id;
      const labels = this.form.labels.filter(label => label.id != labelID);
      this.form.labels = labels;
    },
    submit(evt) {
      evt.preventDefault();
      const formData = this.form;
      formData.complainer = this.user.id;
      formData.labels = Array.from(formData.labels, label => label.id);
      formData.city = 1;
      this.onSubmit(evt, formData);
    },
    reset(evt) {
      evt.preventDefault();
      this.onReset(evt);
    }
  }
}
</script>

<style scoped>
.complaint-label {
    background: #C4C4C4;
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
</style>
