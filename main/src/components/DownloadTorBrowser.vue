<!-- DownloadTorBrowser.vue -->
<template>
    <div class="download-tor">
      <button @click="redirectToDownload">{{ buttonText }}</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DownloadTorBrowser',
    data() {
      return {
        buttonText: this.getButtonText(navigator.language)
      };
    },
    methods: {
      /**
       * Redirects the user to the correct Tor Browser download page based on their device.
       */
      redirectToDownload() {
        const userAgent = navigator.userAgent;
  
        if (/android/i.test(userAgent)) {
          // Redirect Android users to Google Play Store
          window.location.href = 'https://play.google.com/store/apps/details?id=org.torproject.torbrowser';
        } else if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
          // Redirect iOS users to the App Store
          window.location.href = 'https://apps.apple.com/app/onion-browser/id519296448';
        } else {
          // Redirect desktop users to the Tor Project download page
          window.location.href = 'https://www.torproject.org/download/';
        }
      },
      /**
       * Returns the localized button text based on the user's browser language.
       * @param {string} lang - The browser's current language setting.
       * @returns {string} Localized text for the download button.
       */
      getButtonText(lang) {
        if (lang.startsWith('zh')) {
          return '下载TOR浏览器';
        } else if (lang.startsWith('ko')) {
          return 'TOR Browser 다운로드하기';
        } else {
          return 'Download TOR Browser';
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .download-tor button {
    background-color: #007BFF;
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 5px;
  }
  .download-tor button:hover {
    background-color: #0056b3;
  }
  </style>
  