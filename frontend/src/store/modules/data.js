import Service from '@/services/Service.js'

export const state = {
  complaints: [],
  opencalls: [],
  cities: [],
  labels: []
}

export const mutations = {
  SET_COMPLAINTS(state, complaints) {
    state.complaints = complaints
  },
  SET_CITIES(state, c) {
    state.cities = c
  },
  SET_OPENCALLS(state, c) {
    state.opencalls = c
  },
  SET_LABELS(state, c) {
    state.labels = c
  }
}

export const actions = {
  createComplaint(
    { dispatch, rootState }, complaint
  ) {
    return Service.postComplaint(complaint)
      .then(() => {
        dispatch('fetchComplaints')
      })
      .catch(error => {
        console.log('error> ' + error.message)
      })
  },
  vote({ dispatch }, { user_id, c_id, vote }) {
    return Service.postVote(user_id, c_id, vote)
      .then(response => {
        
      });
  },
  fetchComplaints({ commit }) {
    Service.getComplaints()
      .then(response => {
        commit('SET_COMPLAINTS', response.data)
      })
      .catch(error => {
        console.log('error> ' + error.message)
      })
  },
  fetchComplaintsByUserId() {
    Service.getComplaintsByUserId()
      .then(response => {
        return response.data
      })
      .catch(error => {
        console.log('error> ' + error.message)
      })
  },
  fetchOpencalls({ commit }) {
    Service.getOpencalls()
      .then(response => {
        commit('SET_OPENCALLS', response.data)
      })
      .catch(error => {
        console.log('error> ' + error.message)
      })
  },
  fetchCities({ commit }) {
    Service.getCities()
      .then(response => {
        commit('SET_CITIES', response.data)
      })
      .catch(error => {
        console.log('error> ' + error.message)
      })
  },
  fetchLabels({ commit }) {
    Service.getLabels()
      .then(response => {
        commit('SET_LABELS', response.data)
      })
      .catch(error => {
        console.log('error> ' + error.message)
      })
  }
}

export const getters = {
  getComplaintById: state => id => {
    return state.complaints.find(c => c.id === id)
  },
  getOpencallById: state => id => {
    return state.opencalls.find(c => c.id === id)
  },
  getCityById: state => id => {
    return state.cities.find(c => c.id === id)
  },
  getLabelById: state => id => {
    return state.labels.find(c => c.id === id)
  },
  getLabels: state => state.labels,
  getOpencallsForUser: state => {
    return state.opencalls
  }
}
