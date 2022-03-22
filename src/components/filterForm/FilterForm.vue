<template>
  <el-card class="form">
    <el-row :gutter="20" class="header-container">
      <div class="header">
        Find Your Hotel
      </div>
    </el-row>
    <el-row :gutter="20" class="filter-row">
      <el-col :span="6" class="label-container">
        Location
      </el-col>
      <!-- <input type="text" placeholder="Your location"> -->
      <select-bar ref="selectBar" v-on:selectedVal="selectedVal" />
    </el-row>
    <el-row :gutter="20" class="filter-row">
      <el-col :span="6" style="display: flex; flex-direction: column;">
        <div class="label-container">Price</div>
        <div class="note">Higher bound</div>
      </el-col>
      <input v-model="highPrice" type="number" placeholder="Higher bound">
    </el-row>
    <el-row :gutter="20" class="filter-row">
      <el-col :span="6" style="display: flex; flex-direction: column;">
        <div class="label-container">Price</div>
        <div class="note">Lower bound</div>
      </el-col>
      <input v-model="lowPrice" type="number" placeholder="Lower bound">
    </el-row>
    <el-button class="button" @click="search">Search</el-button>
  </el-card>
</template>

<script>
import {ElRow, ElCol, ElButton, ElCard} from 'element-plus'
import SelectBar from '@/components/filterForm/SelectBar'

import { postFilterForm } from '@/network/filter.js'

export default {
  name: "FilterForm",
  components: {
    ElRow, ElCol, ElButton, ElCard, SelectBar
  },
  data() {
    return {
      selected: null,
      highPrice: null,
      lowPrice: null
    }
  },
  methods: {
    search() {
      postFilterForm({
        area: this.selected,
        highPrice: this.highPrice,
        lowPrice: this.lowPrice
      }).then(res => {
        console.log(res);
      }).catch(err => {
        console.log(err);
      })
    },
    selectedVal(childVal) {
      this.selected = childVal;
    }
  }
}
</script>

<style scoped>
  .form {
    width: 500px;
    padding: 40px 30px;
    margin: auto;
    border-radius: 15px;
    box-shadow: 0 0 10px 0 gainsboro;
  }
  .header-container {
    padding: 0 20px 20px;
    display: flex;
  }
  .header {
    font-size: xx-large;
    color: gray;
    justify-content: flex-start;
  }
  .filter-row {
    margin: 20px 0;
    display: flex;
    justify-content: space-around;
    align-items: center;
  }
  .label-container {
    line-height: 30px;
    font-size: larger;
    font-weight: bold;
    display: flex;
    flex-direction: row;
  }
  .note {
    font-size: small;
    color: gray;
  }
  input {
    width: 320px;
    height: 50px;
    padding: 0 25px;
    box-sizing: border-box;
  }
  .button {
    height: 40px;
    width: 240px;
    margin: 20px;
    border-radius: 10px;
    border-style: hidden;
    background-color: #FCAC91;
    color: white;
    -webkit-transition-duration: 0.1s; /* Safari */
    transition-duration: 0.1s;
  }
  .button:hover {
    border: 3px solid #FCAC91;
    background-color: white;
    color: black;
    cursor: pointer;
  }
</style>
