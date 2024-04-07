<template>
  <h1>{{ msg }}</h1>
  <div class="about">
    <transition-group name="fade" tag="div">
      <!--<h1 v-if="showMessage" class="read-the-docs">什么都没有<span v-if="showQuestionMark">吗?</span>-->
        <!--<span v-if="showWaitMark_1">
          稍等..
        </span>
      </h1>-->
      <h1 v-if="show">The creator is <span class="creator-name">KernelKraze</span></h1>
      <div class="github-container">
      <!--<a v-if="show" href="https://github.com/KernelKraze" target="_blank" rel="noopener noreferrer" class="github-link">Visit my GitHub</a> -->
      <!-- <svg-icon v-if="show" type="mdi" :path="path" class="github-icon"></svg-icon> -->
      </div>
    </transition-group>
  </div>
</template>

<script>
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiGithub } from '@mdi/js';

export default {
  name: "my-component",
  components: {
    SvgIcon
  },
  data() {
    return {
      show: false,
      //showMessage: true,
      //showQuestionMark: false,
      //showWaitMark_1 : false,
      //path: mdiGithub,
    };
  },
  mounted() {
  // 3秒后显示 showWaitMark_1
  /** 
  setTimeout(() => {
    this.showWaitMark_1 = true;
  }, 3000);
  
  // 2秒后显示 showQuestionMark
  setTimeout(() => {
    this.showQuestionMark = true;
  }, 2000);
  */
  // 10秒后显示 show，并隐藏 showMessage, showQuestionMark, showWaitMark_1
  setTimeout(() => {
    // 显示 show
    this.show = true;
    
    // 隐藏其他标记
    /** 
    this.showMessage = false;
    this.showQuestionMark = false;
    this.showWaitMark_1 = false;
    */
  }, 300);

}

};

</script>

<style scoped>
.github-container {
  position: relative;
  display: inline-block; /* 或其他适合的布局 */
  top: 90px;
}

.github-icon {
  position: absolute;
  top: -100px; /* 根据实际情况调整 */
  left: 50%;
  transform: translateX(-50%);
  width: 100px; /* 控制宽度 */
  height: 100px; /* 控制高度 */
}


.about {
  text-align: center;
  padding: 20px;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 1s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.github-link {
  color: #333; /* GitHub颜色 */
  text-decoration: none; /* 去掉下划线 */
  font-weight: bold; /* 加粗字体 */
}

.github-link:hover {
  color: #0366d6; /* 鼠标悬停时的颜色 */
  border-radius: 6px;
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

@keyframes rainbow-animation {
  0% {background-position: 0% 50%;}
  50% {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}
.read-the-docs {
  color: #888;
}
</style>
