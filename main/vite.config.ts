import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath } from 'url';
// 如果您的GitHub仓库名是`repo`，并且项目托管在`https://<username>.github.io/repo/`
const repoName = 'KernelKraze'; // 请替换成您的仓库名

export default defineConfig({
  base: `/${repoName}/`, // 添加 base 配置，用于GitHub Pages服务的路径
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  // 其他配置...
})
