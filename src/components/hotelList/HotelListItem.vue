<template>
  <div class="hotel-list-item flex-row">
    <div class="hotel-image-container">
      <img :src="hotel.image" alt="">
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
        <div class="risk" :style="{ color: riskColor }">
          Risk Level: {{hotel.risk_level}}
        </div>
      </div>
      <div class="flex-row price-book-row">
        <div class="price">{{hotel.price}}</div>
        <div class="book" @click="link">Book</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
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
  },
  computed: {
    riskColor() {
      if (this.hotel.risk_level === "Low") {
        return '#91AD70';
      }
      else if (this.hotel.risk_level === "Medium Low") {
        return '#6699A1';
      }
      else if (this.hotel.risk_level === "Medium") {
        return '#C18A26';
      }
      else if (this.hotel.risk_level === "Medium High") {
        return '#E98B2A';
      }
      else {
        return '#E83015';
      }
    }
  }
}
</script>

<style scoped>
.hotel-list-item {
  margin: 20px auto;
  padding: 10px 20px 10px 10px;
  height: 300px;
  width: 1200px;
  border-radius: 5px;
  box-shadow: 0 0 5px gainsboro;
}
.hotel-image-container {
  margin-left: 0;
  margin-right: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.hotel-image-container img {
  height: 300px;
  width: 300px;
  object-fit: contain;
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
  margin-left: 20px;
  width: 880px;
}
.hotel-name {
  width: 880px;
  font-weight: bold;
  font-size: 32px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.location, .rate, .risk {
  font-size: 24px;
}
.rate {
  margin: 5px 0;
}
.price {
  font-weight: bold;
  font-size: 40px;
  color: darksalmon;
}
.book {
  margin: 0 10px 0 10px;
  border-radius: 8px;
  background-color: olive;
  padding: 5px;
  color: white;
  font-weight: bold;
  font-size: 30px;

  cursor: pointer;
}
.price-book-row {
  margin-top: 10px;
}

/* iphone6 7 8 plus */
@media screen and (max-width: 414px) {
.hotel-list-item {
  margin: 10px auto;
  height: 35vw;
  width: 90vw;
  border-radius: 2px;
  box-shadow: 0 0 2px gainsboro;
}
.hotel-image-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.hotel-image-container img {
  height: 35vw;
  width: 35vw;
  object-fit: contain;
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
  margin-left: 5px;
  width: 50vw;
}
.hotel-name {
  width: 55vw;
  font-weight: bold;
  font-size: 18px;
  white-space: normal;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2; /* 行数*/
  -webkit-box-orient: vertical;
}
.location, .rate, .risk {
  font-size: 14px;
  margin: 0 0 3px 0;
}
.price {
  font-weight: bold;
  font-size: 16px;
  color: darksalmon;
}
.book {
  margin: 0 0 0 10px;
  border-radius: 8px;
  background-color: olive;
  padding: 2px;
  color: white;
  font-weight: bold;
  font-size: 14px;

  cursor: pointer;
}
.price-book-row {
  margin-top: 0px;
}
}
</style>
