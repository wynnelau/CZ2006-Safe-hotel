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
    this.hotelData = this.$store.state.hotels;
  }
}
</script>

<style scoped>
.title {
  margin: 20px auto;
  font-size: xx-large;
}
</style>
