<template>
  <el-menu :default-active="activeIndex" mode="horizontal">
    <el-menu-item index="1">
      <router-link :to="{ name: 'complaint-list' }">Complaints</router-link>
    </el-menu-item>
    <el-menu-item index="2">
      <router-link :to="{ name: 'opencall-list' }">Open calls</router-link>
    </el-menu-item>
  </el-menu>
</template>

<script>
//@select="handleSelect"
export default {
  data() {
    return {
      activeIndex: '1'
    }
  }
}
</script>

<style lang="scss" scoped></style>
