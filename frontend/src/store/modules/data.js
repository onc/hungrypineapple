import Service from '@/services/Service.js'

export const state = {
  complaints: [],
  opencalls: [],
  cities: []
}

export const mutations = {
  SET_COMPLAINTS(state, complaints) {
    state.complaints = complaints
  },
  SET_CITIES(state, c) {
    state.cities = c
  }
}

export const actions = {
  createComplaint(
    { dispatch, rootState },
    { userId, desc, title, labelIdArr }
  ) {
    console.log(
      'New complaint: ' + title + ' from user ' + rootState.user.login
    )

    return Service.postComplaint({
      complainer: userId,
      description: desc,
      title: title,
      labels: labelIdArr
    })
      .then(() => {
        dispatch('fetchComplaints')
      })
      .catch(error => {
        console.log('error> ' + error.message)
      })
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

  fetchCities({ commit }) {
    Service.getCities()
      .then(response => {
        commit('SET_CITIES', response.data)
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
  getCityById: state => id => {
    return state.cities.find(c => c.id === id)
  }
}
