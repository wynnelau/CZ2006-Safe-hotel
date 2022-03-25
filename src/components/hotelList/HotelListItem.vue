<template>
  <div class="hotel-list-item flex-row">
    <div class="hotel-image">
      <el-image :src="hotel.image" />
      <!-- <img :src="hotel.image" alt=""> -->
    </div>
    <div class="flex-col text">
      <div class="hotel-name">
        {{hotel.name}}
      </div>
      <div style="margin-top: 10px;">
        <div class="location flex-row">
          <img src="@/assets/img/location.svg" alt="" style="width: 1em; height: 1em; margin-right: 5px;">
          {{hotel.location}}
        </div>
        <div class="rate flex-row">
          <img src="@/assets/img/star.svg" alt="" style="width: 1em; height: 1em; margin-right: 5px;">
          <div>{{hotel.review}}</div>
        </div>
        <div>
          Risk Level: {{hotel.risk_level}}
        </div>
      </div>
      <div class="flex-row" style="margin-top: 10px;">
        <div class="price">{{hotel.price}}</div>
        <div class="book" @click="link">Book</div>
      </div>
    </div>
  </div>
</template>

<script>
import { ElImage } from 'element-plus'
export default {
  components: {
    ElImage
  },
  props: {
    hotel: Object
  },
  data() {
    return {

    }
  },
  methods: {
    link() {
      window.open(this.hotel.url, '_blank');
    }
  }
}
</script>

<style scoped>
.hotel-list-item {
  margin: 20px auto;
  padding: 10px 20px 10px 10px;
  min-height: 200px;
  width: 730px;
  border-radius: 5px;
  box-shadow: 0 0 5px gainsboro;
}
.hotel-image {
  margin-left: 0;
  margin-right: 10px;
  width: 200px;
  height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.hotel-image .el-image {
  text-align: center;
}
.flex-col {
  display: flex;
  flex-direction: column;
}
.flex-row {
  display: flex;
  flex-direction: row;
}
.text {
  text-align: left;

}
.hotel-name {
  font-weight: bold;
  font-size: larger;
}
.rate {
  margin: 5px 0;
}
.price {
  font-weight: bold;
  font-size: xx-large;
  color: darksalmon;
}
.book {
  margin: 0 10px 0 10px;
  border-radius: 8px;
  background-color: olive;
  padding: 5px;
  color: white;
  font-weight: bold;
  font-size: x-large;

  cursor: pointer;
}
</style>
