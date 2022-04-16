<template>
  <el-card class="form">
    <el-row :gutter="20" class="header-container">
      <div class="header">
        Find Your Hotel
      </div>
    </el-row>
    <el-row :gutter="20" class="location-row">
      <el-col :span="6" class="label-container">
        Location
      </el-col>
      <select-bar ref="selectBar" v-on:selectedVal="selectedVal" />
    </el-row>
    <el-row :gutter="20" class="filter-row">
      <el-col :span="6" style="display: flex; flex-direction: column;">
        <div class="label-container">Price</div>
        <div class="note">Higher Bound</div>
      </el-col>
      <input v-model="highPrice" type="number" placeholder="Higher bound">
    </el-row>
    <el-row :gutter="20" class="warning-row">
      <el-col class="label-container"></el-col>
      <div v-if="warningh" class="warning">Please type in the correct number format.</div>
      <div v-else class="warning"></div>
    </el-row>
    <el-row :gutter="20" class="filter-row">
      <el-col :span="6" style="display: flex; flex-direction: column;">
        <div class="label-container">Price</div>
        <div class="note">Lower Bound</div>
      </el-col>
      <input v-model="lowPrice" type="number" placeholder="Lower bound">
    </el-row>
    <el-row :gutter="20" class="warning-row">
      <el-col class="label-container"></el-col>
      <div v-if="warningl" class="warning">Please type in the correct number format.</div>
      <div v-else class="warning"></div>
      <div v-if="warninghl" class="warning">Higher Bound should be not less than Lower Bound</div>
    </el-row>
    <el-button class="button" @click="search">Search</el-button>
  </el-card>
</template>

<script>
import {ElRow, ElCol, ElButton, ElCard} from 'element-plus'
import SelectBar from '@/components/filterForm/SelectBar'

// import { postFilterForm } from '@/network/filter.js'

export default {
  name: "FilterForm",
  components: {
    ElRow, ElCol, ElButton, ElCard, SelectBar
  },
  data() {
    return {
      selected: null,
      highPrice: null,
      lowPrice: null,
      res_hotel: [],
      warningh: false,
      warningl: false,
      warninghl: false
    }
  },
  methods: {
    search() {
      if (this.checkFormat()) {
        this.$router.push({
          path: "/searchresult",
          query: {
            area: this.selected,
            highPrice: this.highPrice,
            lowPrice: this.lowPrice
          }
        });
      }

      // postFilterForm({
      //   area: this.selected,
      //   highPrice: this.highPrice,
      //   lowPrice: this.lowPrice
      // }).then(res => {
      //   this.res_hotel = res;
      //   this.$store.commit('setHotels', this.res_hotel);
      //   this.changeRoute();
      // }).catch(err => {
      //   console.log(err);
      // })
    },
    selectedVal(childVal) {
      this.selected = childVal;
    },
    checkFormat() {
      this.warningh = false;
      this.warningl = false;
      this.warninghl = false;

      if (this.highPrice < 0) {
        this.warningh = true;
      }
      if (this.lowPrice < 0) {
        this.warningl = true;
      }
      if (this.warningh || this.warningl) {
        return false;
      }

      if (this.highPrice != null && this.highPrice < this.lowPrice) {
        this.warninghl = true;
        return false;
      }

      return true;
    }
  }
}
</script>

<style scoped>
  .form {
    width: 800px;
    padding: 40px 30px;
    margin: auto;
    border-radius: 15Px;
    box-shadow: 0 0 10Px 0 gainsboro;
  }
  .header-container {
    padding: 0 20px 20px;
    display: flex;
  }
  .header {
    font-size: 50px;
    color: gray;
    justify-content: flex-start;
  }
  .location-row {
    margin: 40px 0;
    display: flex;
    justify-content:center;
    align-items: center;
  }
  .filter-row {
    margin: 10px 0;
    display: flex;
    justify-content:center;
    align-items: center;
  }
  .warning-row {
    margin: 0;
    position: relative;
    top: -8px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .label-container {
    width: 230px;
    text-align: left;
    line-height: 50px;
    font-size: 1.2em;
    font-weight: bold;
    display: flex;
    flex-direction: row;
  }
  .note {
    width: 230px;
    text-align: left;
    font-size: 0.7em;
    color: gray;
  }
  input {
    width: 380px;
    height: 80px;
    padding: 0 25px;
    box-sizing: border-box;
  }
  .warning {
    margin: 0;
    padding: 0;
    height: 20px;
    text-align: left;
    font-size: 20px;
    color: red;
  }
  .button {
    height: 60px;
    width: 260px;
    margin: 20px;
    border-radius: 10px;
    border-style: hidden;
    background-color: #FCAC91;
    color: white;
    font-size: 28px;
    -webkit-transition-duration: 0.1s; /* Safari */
    transition-duration: 0.1s;
  }
  .button:hover {
    border: 3px solid #FCAC91;
    background-color: white;
    color: black;
    cursor: pointer;
  }

  /* ipad */
@media screen and (max-width: 768px) {
  .form {
    width: 500px;
    padding: 20px 15px;
    margin: auto;
    border-radius: 15Px;
    box-shadow: 0 0 10Px 0 gainsboro;
  }
  .label-container {
    width: 150px;
    text-align: left;
    line-height: 40px;
    font-size: 1.3em;
    font-weight: bold;
    display: flex;
    flex-direction: row;
  }
  .note {
    width: 150px;
    text-align: left;
    font-size: 0.8em;
    color: gray;
  }
  input {
    width: 230px;
    height: 60px;
    padding: 0 25px;
    box-sizing: border-box;
  }
  .button {
    height: 50px;
    width: 240px;
    margin: 20px;
    border-radius: 10px;
    border-style: hidden;
    background-color: #FCAC91;
    color: white;
    font-size: 25px;
    -webkit-transition-duration: 0.1s; /* Safari */
    transition-duration: 0.1s;
  }
  .button:hover {
    border: 3px solid #FCAC91;
    background-color: white;
    color: black;
    cursor: pointer;
  }
}

/* iphone6 7 8 plus */
@media screen and (max-width: 414px) {
  .form {
    width: 80%;
    padding: 20px 10px;
    margin: auto;
    border-radius: 15Px;
    box-shadow: 0 0 10Px 0 gainsboro;
  }
  .header-container {
    padding: 0 20px 20px;
    display: flex;
  }
  .header {
    font-size: 30px;
    color: gray;
    justify-content: flex-start;
  }
  .location-row {
    margin: 25px 0;
    display: flex;
    justify-content:center;
    align-items: center;
  }
  .filter-row {
    margin: 10px 0;
    display: flex;
    justify-content:center;
    align-items: center;
  }
  .warning-row {
    margin: 0;
    position: relative;
    top: -8px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .label-container {
    width: 100px;
    text-align: left;
    line-height: 30px;
    font-size: 22px;
    font-weight: bold;
    display: flex;
    flex-direction: row;
  }
  .note {
    width: 100px;
    text-align: left;
    font-size: 15px;
    color: gray;
  }
  input {
    width: 180px;
    height: 50px;
    padding: 0 10px;
    box-sizing: border-box;
  }
  .button {
    height: 50px;
    width: 200px;
    margin: 15px;
    border-radius: 10px;
    border-style: hidden;
    background-color: #FCAC91;
    color: white;
    font-size: 25px;
    -webkit-transition-duration: 0.1s; /* Safari */
    transition-duration: 0.1s;
  }
  .button:hover {
    border: 3px solid #FCAC91;
    background-color: white;
    color: black;
    cursor: pointer;
  }
}
</style>
