<template>
    <transition-group name="fade" tag="div">
      <h1 v-if="show">The creator is <span class="creator-name">KernelKraze</span></h1>
      <div class="github-container">
      </div>
    </transition-group>
</template>
<script>
export default {
  data() {
    return {
      show: false,
    };
  },
  mounted() {
  setTimeout(() => {
    // 显示 show
    this.show = true;
  }, 1000);
  

}};
</script>
<style scoped>
.github-container {
  position: relative;
  display: inline-block; /* 或其他适合的布局 */
  top: 90px;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity 1s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
.creator-name {
  transition: color 0.5s ease-in-out; /* 添加颜色变化的过渡效果 */
  color: #333; /* GitHub的经典颜色 */
}
.creator-name:hover {
  color: transparent; /* 使文字透明 */
  background-clip: text; /* 将背景裁剪到文字形状 */
  -webkit-background-clip: text;
  background-image: linear-gradient(45deg, #ff7eb3, #ff7ee7, #7afcff, #feff9c, #fff740, #87ff70); /* 彩色渐变 */
  animation: rainbow-animation 5s infinite linear; /* 添加彩色动态效果 */
}
</style>