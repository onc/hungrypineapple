import axios from 'axios'

const api = axios.create({
  baseURL: '/api/',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
})

export default {
  getUserById(id) {
    return api.get('user/' + id)
  },

  getLabels() {
    return api.get('label')
  },
  getLabelById(id) {
    return api.get('label/' + id)
  },

  getCities() {
    return api.get('city')
  },

  getComplaints() {
    return api.get('complaint')
  },
  getComplaintsForUser(id) {
    return api.get('user/' + id + '/complaint')
  },
  getComplaintsByLabelId(id) {
    return api.get('label/' + id + '/complaint')
  },
  getComplaintById(id) {
    return api.get('complaint/' + id)
  },
  updateComplaint({ c, id }) {
    return api.post('complaint/' + id, c)
  },
  postComplaint(c) {
   return api.post('complaint', c)
  },

  getOpencalls() {
    return api.get('opencall')
  },
  getOpencallById(id) {
    return api.get('opencall/' + id)
  },
  postVote(user_id, c_id, vote) {
    return api.post(`user/${user_id}/complaint/${c_id}/vote`, vote);
  }
}
