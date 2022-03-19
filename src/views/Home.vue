<template>
  <div>
    <el-main>
      <map-img />
      <br />
      <br />
      <el-row class="mb-4">
        <el-button @click="filter" class="button">Filter Your Hotels</el-button>
        <el-button @click="recom" class="button">Daily Recommendations</el-button>
      </el-row>
    </el-main>
    <el-footer></el-footer>
  </div>
</template>

<script> 
import { ElButton, ElFooter, ElMain, ElRow } from 'element-plus'
import MapImg from '@/components/map/MapImg.vue'

export default {
  name: "Home",
  components: {
    MapImg, ElButton, ElFooter, ElMain, ElRow
  },
  methods: {
    filter() {
      this.$router.push("/search");
    },
    recom() {
      this.$router.push("/dailyRecommendations")
    }
  }
}
</script>

<style scoped>
  .el-footer {
    height: 60px;
  }
  .button {
    height: 40px;
    width: 300px;
    margin: 1%;
    border-radius: 10px;
    border-style: hidden;
    background-color: #FCAC91;
    color: white;
    -webkit-transition-duration: 0.3s; /* Safari */
    transition-duration: 0.3s;
  }
  .button:hover {
    border: 3px solid #FCAC91;
    background-color: white;
    color: black;
    cursor: pointer;
  }
</style>