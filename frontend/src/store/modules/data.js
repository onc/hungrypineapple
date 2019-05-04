import Service from '@/services/Service.js'

export const state = {
  complaints: [],
  opencalls: []
}

export const mutations = {
  SET_COMPLAINTS(state, complaints) {
    console.log('setting complaints to ' + complaints)
    state.complaints = complaints
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
  }
}

export const getters = {
  getComplaintById: state => id => {
    return state.complaints.find(c => c.id === id)
  }
}
