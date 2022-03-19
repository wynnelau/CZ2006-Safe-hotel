<template>
  <el-container>
    <div class="title">Daily Recommendations</div>
    <el-main>
      <hotel-list></hotel-list>
    </el-main>
    <el-footer></el-footer>
  </el-container>
</template>

<script>
import { ElContainer, ElMain, ElFooter } from 'element-plus'
import HotelList from '@/components/hotelList/HotelList'
export default {
  name: "Recom",
  components: {
    ElContainer, ElMain, ElFooter, HotelList
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
</style>