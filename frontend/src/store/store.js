import Vue from 'vue'
import Vuex from 'vuex'
import * as data from '@/store/modules/data.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userPrivilege: 'public', // public | moderator | town
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
    }
  },
  actions: {
    selectCity({ commit }, { cityId, cityName }) {
      commit('SET_CITY', { id: cityId, name: cityName })
    }
  },
  getters: {
    getSelectedCity: state => {
      return state.selectedCity
    }
  }
})
