<template>
  <el-container>
    <div class="title">Daily Recommendations</div>
    <br>
    <el-main>
      <hotel-block :hotelData="hotelRecomList" />
    </el-main>
    <el-footer></el-footer>
  </el-container>
</template>

<script>
import hotelList from '@/data/recommendation.json'
import { ElContainer, ElMain, ElFooter } from 'element-plus'
import HotelBlock from '@/components/hotelList/HotelBlock'
export default {
  name: "Recom",
  components: {
    ElContainer, ElMain, ElFooter, HotelBlock
  },
  data() {
    return {
      hotelRecomList: []
    }
  },
  created() {
    this.hotelRecomList = [];
    for (let item of hotelList) {
      if (item.price[0] != "S") {
        item.price = "S$ " + item.price;
      }
      this.hotelRecomList.push(item);
    }
  }
}
</script>

<style scoped>
.el-container {
  margin: 0;
}
.el-footer {
  background-color:antiquewhite;
  height: 60px;
}
.title {
  margin: 20px auto;
  font-size: xx-large;
}
/* iphone6 7 8 plus */
@media screen and (max-width: 414px) {
.title {
  font-size: 28px;
}
}
</style>
