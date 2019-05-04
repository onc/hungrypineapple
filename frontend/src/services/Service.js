import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:3000',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
})

export default {
  getComplaints(perPage, currentPage) {
    return apiClient.get('/complaints?_limit=' + perPage + '&_page=' + currentPage)
  }
}
