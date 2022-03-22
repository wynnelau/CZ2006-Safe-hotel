<template>
  <div>
    <div class="flex-row tag">
      <div class="style-button" v-if="!isStyle1" @click="switch1">style 1</div>
      <div class="style-button isActive" v-if="isStyle1">style 1</div>
      <div class="style-button" v-if="isStyle1" @click="switch2">style 2</div>
      <div class="style-button isActive" v-if="!isStyle1">style 2</div>
    </div>
    <div v-if="isStyle1">
      <div v-for="item in hotelPage1" :key="item.name">
        <hotel-list-item :hotel="item">
        </hotel-list-item>
      </div>
    </div>
    <div v-if="!isStyle1">
      <hotel-block :hotelData="hotelPage1" />
    </div>
  </div>
</template>

<script>
import hotelList from '@/data/hotel_data.json'
import HotelListItem from '@/components/hotelList/HotelListItem'
import HotelBlock from '@/components/hotelList/HotelBlock'
export default {
  components: {
    HotelListItem, HotelBlock
  },
  created() {
    this.hotelList = hotelList;
    this.hotelPage1 = hotelList.slice(0, 20);
    for (let item of this.hotelPage1) {
      item.price = "S$ " + item.price.slice(3);
    }
  },
  data() {
    return {
      hotelList,
      hotelPage1: null,
      isStyle1: true
    }
  },
  methods: {
    switch1() {
      this.isStyle1 = true;
    },
    switch2() {
      this.isStyle1 = false;
    }
  }
}
</script>

<style scoped>
.flex-row {
  display: flex;
  flex-direction: row;
}
.tag {
  margin: auto;
  width: 60%;
}
.style-button {
  margin: 0;
  padding: 5px;
  border: 1px solid white;
  background-color: rgb(111, 197, 250);
  color: white;
  cursor: pointer;
}
.isActive {
  background-color: rgb(157, 214, 250);
}
</style>
