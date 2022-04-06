<template>
  <div class="hotel-item">
    <div class="flex-row">
      <img class="hotel-img" :src="hotel.image">
      <!-- <el-image :src="hotel.image" /> -->
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
// import { ElImage } from 'element-plus'
export default {
  name: "HotelBlockItem",
  components: {

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
  height: 300px;
  width: 100%;
  /* width: 540px; */
  margin: 20px 0;
  flex: 0 0 32%;
  /* box-shadow: 0 0 5px gainsboro; */
}
.hotel-item:nth-child(3n-1) {
  margin-left: 2%;
  margin-right: 2%;
}
.hotel-img {
  height: 300px;
  object-fit: contain;
}
.rsection {
  padding: 0 10px;
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
  font-size: 25px;
  font-family: 'Bahnschrift SemiBold', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.risk-level {
  font-size: 22px;
  font-family: 'Bahnschrift SemiBold', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #91AD70;
}
.location {
  margin: 10px 0 5px 0;
  font-size: 22px;
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  color: #535953;
}
.rate {
  margin-bottom: 5px;
  font-size: 22px;
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  color: #535953;
}
.price {
  font-size: 32px;
  color: rgb(15, 174, 236);
  font-weight: bold;
}
.book {
  align-self: flex-start;
  font-size: 22px;
  color: #535953;
  cursor: pointer;
}

/* iphone6 7 8 plus */
@media screen and (max-width: 414px) {
.hotel-item {
  --image-height: 150px;
  height: var(--image-height);
  width: 100%;
  margin: 10px 0;
  flex: 1;
  /* box-shadow: 0 0 5px gainsboro; */
}
.hotel-item:nth-child(3n-1) {
  height: var(--image-height);
  width: 100%;
  margin: 10px 0;
}
.hotel-img {
  height: var(--image-height);
  width: var(--image-height);
  object-fit: contain;
}
.rsection {
  padding: 0 10px;
  /* width: 180px; */
  flex: 0 0 53%;
  /* flex-grow: 1; */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.hotel-name {
  font-size: 19px;
  font-family: 'Bahnschrift SemiBold', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  white-space: normal;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3; /* 行数*/
  -webkit-box-orient: vertical;
}
.risk-level {
  font-size: 15px;
  font-family: 'Bahnschrift SemiBold', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #91AD70;
}
.location {
  margin: 0;
  font-size: 15px;
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  color: #535953;
}
.rate {
  margin-bottom: 0;
  font-size: 15px;
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  color: #535953;
}
.price {
  font-size: 15px;
  color: rgb(15, 174, 236);
  font-weight: bold;
}
.book {
  align-self: flex-start;
  font-size: 15px;
  color: #535953;
  cursor: pointer;
}
}
</style>
