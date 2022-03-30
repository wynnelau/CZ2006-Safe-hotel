import { createStore } from 'vuex'

export default createStore({
  state() {
    return {
      hotels: []
    }
  },
  mutations: {
    setHotels(state, hotels) {
      state.hotels = hotels
    }
  }
})
