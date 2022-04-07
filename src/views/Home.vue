<template>
  <div>
    <preloading v-if="isloading" />
    <el-main>
      <map-img @has-mounted="mapLoad" />
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
import Preloading from '@/components/preloading/Preloading'

export default {
  name: "Home",
  components: {
    MapImg, ElButton, ElFooter, ElMain, ElRow, Preloading
  },
  data() {
    return {
      isloading: true
    }
  },
  methods: {
    mapLoad() {
      this.isloading = false;
    },
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
    min-height: 60px;
    min-width: 320px;
    margin: 0 20px;
    padding: 5Px 10Px;
    border-radius: 8Px;
    border-style: hidden;
    background-color: #FCAC91;
    color: white;
    font-size: 1.1em;
    -webkit-transition-duration: 0.3s; /* Safari */
    transition-duration: 0.3s;
  }
  .button:hover {
    border: 3px solid #FCAC91;
    background-color: white;
    color: black;
    cursor: pointer;
  }

/* iphone6 7 8 plus */
@media screen and (max-width: 414px) {
  .button {
    height: 30px;
    min-width: 130px;
    margin: 0 10px;
    padding: 2Px 5Px;
    border-radius: 8Px;
    border-style: hidden;
    background-color: #FCAC91;
    color: white;
    font-size: 15px;
    -webkit-transition-duration: 0.3s; /* Safari */
    transition-duration: 0.3s;
  }
}
</style>
