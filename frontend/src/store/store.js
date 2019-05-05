import Vue from 'vue'
import Vuex from 'vuex'
import * as data from '@/store/modules/data.js'
import Service from '@/services/Service.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {},
    selectedCity: {
      id: NaN,
      name: ''
    }
  },
  modules: {
    data
  },
  mutations: {
    SET_CITY(state, city) {
      state.selectedCity = city
    },
    SET_USER(state, user) {
      state.user = user
    }
  },
  actions: {
    selectCity({ commit }, { cityId, cityName }) {
      commit('SET_CITY', { id: cityId, name: cityName })
    },

    fetchUser({ commit }, id) {
      return Service.getUserById(id).then(user => {
        commit('SET_USER', user.data)
      })
    },
    
  },
  getters: {
    getSelectedCity: state => {
      return state.selectedCity
    },
    getUser: state => {
      return state.user
    }
  }
})
