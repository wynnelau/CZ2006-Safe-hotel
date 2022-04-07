<template>
  <div class="preloading">
    <img src="@/assets/img/loading.png" alt="">
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.preloading {
  position: fixed;
  width: 100vw;
  height: 96vh;
  background-color: rgba(250, 235, 215, 0.5);

  display: flex;
  justify-content: center;
  align-items: center;
}
.preloading img {
  width: 30%;
}
</style>
