<script setup lang="ts">
import Main from './components/Main.vue'
import DarkWebInfo from './components/DarkWebInfo.vue';
import DownloadTorBrowser from './components/DownloadTorBrowser.vue';
import About from './components/About.vue';
</script>
<template>
  <div>
    <a href="https://github.com/KernelKraze/" target="_blank">
      <img src="./assets/notion-avatar-1711210711924.svg" class="logo CryptoWander" alt="logo" />
    </a>
  </div>
  <Main msg="" />
  <DownloadTorBrowser/>
  <DarkWebInfo/>
  <About/>
</template>
<style scoped>
.logo {
  height: 20em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo.CryptoWander:hover {
  filter: drop-shadow(0 0 2em #ffffffaa);
}
</style>