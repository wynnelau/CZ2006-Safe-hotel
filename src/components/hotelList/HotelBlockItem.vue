<template>
  <div class="hotel-item">
    <div class="flex-row">
      <el-image :src="hotel.image" />
      <div class="rsection">
        <div class="text">
          <div class="hotel-name">
            {{hotel.name}}
          </div>
          <div class="risk-level">
            Risk Level: {{hotel.risk_level}}
          </div>
          <div class="location">
            {{hotel.location}}
          </div>
          <div class="rate flex-row">
            <img src="@/assets/img/star.svg" alt="" style="width: 1em; height: 1em; margin-right: 4px;">
            {{hotel.review}}
          </div>
          <div class="price">{{hotel.price}}</div>
        </div>
        <div class="book" @click="link">See detail ➝</div>
      </div>
    </div>
  </div>
</template>

<script>
import { ElImage } from 'element-plus'
export default {
  name: "HotelBlockItem",
  components: {
    ElImage
  },
  props: {
    hotel: Object
  },
  methods: {
    link() {
      window.open(this.hotel.url, '_blank');
    }
  }
}
</script>

<style scoped>
.hotel-item {
  width: 100%;
  /* box-shadow: 0 0 5px gainsboro; */
}
.rsection {
  padding: 5px 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.flex-row {
  display: flex;
  flex-direction: row;
  justify-content: left;
}
.text {
  text-align: left;
  flex-direction: column;
}
.hotel-name {
  font-size: medium;
  font-family: 'Bahnschrift SemiBold', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.risk-level {
  font-size: small;
  font-family: 'Bahnschrift SemiBold', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #91AD70;
}
.location {
  margin: 10px 0 5px 0;
  font-size: 0.9em;
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  color: #535953;
}
.rate {
  margin-bottom: 5px;
  font-size: 0.9em;
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  color: #535953;
}
.price {
  font-size: 1.2em;
  color: rgb(15, 174, 236);
  font-weight: bold;
}
.book {
  align-self: flex-start;
  font-size: 0.9em;
  color: #535953;
  cursor: pointer;
}
</style>
