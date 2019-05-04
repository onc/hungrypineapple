<template>
  <el-container>
    <el-header>
      <h1>Sere mě {{ city }}</h1>
      <Navbar />
    </el-header>

    <el-main>
      <el-card shadow="always" v-for="complaint in complaints">Always</el-card>
    </el-main>
  </el-container>
</template>

<script>
import Navbar from '@/components/Navbar.vue'

export default {
  components: {
    Navbar
  },
  props: ['city']
}
</script>

<style lang="scss" scoped></style>
