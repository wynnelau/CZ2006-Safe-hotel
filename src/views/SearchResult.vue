<template>
  <el-container>
    <div class="title">Search Results</div>
    <br>
    <el-main>
      <hotel-list :hotel-data="hotelData"/>
    </el-main>
    <el-footer></el-footer>
  </el-container>
</template>

<script>
import { postFilterForm } from '@/network/filter.js'
import { ElContainer, ElMain, ElFooter } from 'element-plus'
import HotelList from '@/components/hotelList/HotelList'

export default {
  name: "SearchResult",
  components: {
    ElContainer, ElMain, ElFooter, HotelList
  },
  data() {
    return {
      hotelData: []
    }
  },
  created() {
    let filter = this.$route.query;
    filter.highPrice = parseInt(filter.highPrice);
    filter.lowPrice = parseInt(filter.lowPrice);
    this.hotelData = [];
    postFilterForm(filter).then(res => {
      this.hotelData = res;
      for (let item of this.hotelData) {
        if (item.price[0] != "S") {
          item.price = "S$ " + item.price;
        }
      }
    }).catch(err => {
      console.log(err);
    });
    // for (let item of this.$store.state.hotels) {
    //   if (item.price[0] != "S") {
    //     item.price = "S$ " + item.price;
    //   }
    //   this.hotelData.push(item);
    // }
  }
}
</script>

<style scoped>
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
