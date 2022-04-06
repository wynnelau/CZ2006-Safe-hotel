<template>
  <div class="hotel-block">
    <hotel-block-item v-for="item in hotels" :key="item.name" :hotel="item" />
  </div>
</template>

<script>
import HotelBlockItem from '@/components/hotelList/HotelBlockItem'
export default {
  name: "HotelBlock",
  components: {
    HotelBlockItem
  },
  props: {
    hotelData: Array
  },
  data() {
    return {
      hotels: null
    }
  },
  created() {
    this.hotels = this.hotelData;
    for (let hotel of this.hotels) {
      hotel.location = hotel.location.replace(/Singapore/, "SG");
    }
  }
}
</script>

<style scoped>
.hotel-block {
  width: 90%;
  margin: auto;
  /* display: grid; */
  /* grid-template-columns: repeat(auto-fill, 500px);
  row-gap: 30px;
  column-gap: 40px; */
  justify-content: flex-start;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
</style>
