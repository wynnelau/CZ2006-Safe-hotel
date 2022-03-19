<template>
  <el-container class="filter">
    <filter-form />
  </el-container>
</template>

<script>
import FilterForm from '@/components/filterForm/FilterForm'
import { ElContainer } from 'element-plus'
export default {
  name: "Filter",
  components: {
    FilterForm, ElContainer
  }
}
</script>

<style scoped>
  .filter {
    margin-top: 60px;
  }
</style>
