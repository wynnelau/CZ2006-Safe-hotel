<template>
  <div>
    <select required class="select-bar" v-model="selected">
      <option value="default" disabled selected>Select your option</option>
      <option v-for="item in options" :key="item.value" :value="item.value">
        {{item.label}}
      </option>
    </select>
  </div>
</template>

<script>
import area from '@/data/area.json'

export default {
  name: 'SelectBar',
  data() {
    return {
      options: [],
      selected: "default"
    }
  },
  created() {
    this.options = [];
    for (let loc of area) {
      this.options.push({
        value: loc,
        label: loc
      });
    }
  },
  watch: {
    selected: function(newVal) {
      this.$emit('selectedVal', newVal);
    }
  }
}
</script>

<style scoped>
.select-bar {
  width: 320px;
  height: 50px;
  padding: 0 25px;
  box-sizing: border-box;
}
</style>
