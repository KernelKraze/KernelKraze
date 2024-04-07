<script setup lang="ts">
import Main from './components/Main.vue'
</script>

<template>
  <div>
    <a href="https://github.com/KernelKraze" target="_blank">
      <img src="./assets/notion-avatar-1711210711924.svg" class="logo KernelKraze" alt="logo" />
    </a>
  </div>
  <Main msg="KernelKrze" />
</template>

<style scoped>
.logo {
  height: 20em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo.KernelKraze:hover {
  filter: drop-shadow(0 0 2em #ffffffaa);
}
</style>
./components/Main.vue