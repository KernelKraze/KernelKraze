<template>
    <h1 v-if="language === 'zh'">欢迎!</h1>
    <h1 v-else-if="language === 'ko'">환영합니다!</h1>
    <h1 v-else>Welcome!</h1>
    <div class="about">
      <p class="read-the-docs" v-html="getWelcomeText()"></p>
      <p class="hint" v-html="getHelpText()"></p>
      <p ref="onionLink" @click="copyOnionLink">4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion</p>
      <button @click="handleAccessButtonClick">{{ getDarkWebButtonText() }}</button>
      <div id="instruction"></div>
    </div>
</template>
  
<script>
export default {
  name: 'Main',
  data() {
    return {
      language: navigator.language.startsWith('zh') ? 'zh' :
                navigator.language.startsWith('ko') ? 'ko' : 'en'
    };
  },
  methods: {
    getWelcomeText() {
      switch(this.language) {
        case 'zh': return "加入我们, 一起探寻知识的海洋, 体验心灵的奇妙旅程.(网站每天可能会变化哦!~,敬请期待吧!)";
        case 'ko': return "우리와 함께 지식의 바다를 탐험하고, 마음의 멋진 여정을 경험하세요. (웹사이트가 매일 바뀔 수 있어요! 기대해 주세요!)";
        default:   return "Join us to explore the vast ocean of knowledge and experience a wonderful journey of the mind. (The site may change daily! Stay tuned!)";
      }
    },
    getHelpText() {
      switch(this.language) {
        case 'zh': return "如果您遇到任何访问问题, 请稍作等待或联系我们.";
        case 'ko': return "접속에 문제가 발생한 경우, 잠시 기다리시거나 저희에게 연락해 주세요.";
        default:   return "If you encounter any access problems, please wait a moment or contact us.";
      }
    },
    getDarkWebButtonText() {
      switch(this.language) {
        case 'zh': return "访问暗网,或点击上面的链接手动访问";
        case 'ko': return "다크웹에 접속하거나, 위의 링크를 클릭하여 수동으로 접속하세요.";
        default:   return "Access the dark web, or click the link above to access manually.";
      }
    },
    copyOnionLink() {
      const onionLinkText = this.$refs.onionLink.innerText;
      navigator.clipboard.writeText(onionLinkText)
        .then(() => {
          const message = this.language === 'zh' ? '地址已复制到剪贴板: ' + onionLinkText :
                         this.language === 'ko' ? '주소가 클립보드에 복사되었습니다: ' + onionLinkText :
                         'Address has been copied to clipboard: ' + onionLinkText;
          alert(message);
        })
        .catch(err => {
          const errMsg = this.language === 'zh' ? '复制到剪贴板失败: ' :
                         this.language === 'ko' ? '클립보드에 복사 실패: ' :
                         'Failed to copy to clipboard: ';
          console.error(errMsg, err);
        });
    },
    handleAccessButtonClick() {
      const ua = navigator.userAgent;
      const instructionDiv = document.getElementById('instruction');
      let htmlContent = "";

      if (/Windows/i.test(ua)) {
        htmlContent = this.language === 'zh' ? "请确保你已安装 Tor Browser,点击下方按钮, 使用Tor Browser访问本网站并<a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>点击此链接</a>访问我的网站." :
                      this.language === 'ko' ? "Tor Browser가 설치되어 있는지 확인하세요. 아래 버튼을 클릭하여 다운로드하고 설치한 후, Tor Browser로 이 웹사이트를 방문하고 <a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>이 링크</a>를 클릭하여 내 사이트에 접속하세요." :
                      "Please make sure you have Tor Browser installed. Click the button below to download and install it, then use Tor Browser to visit this site and <a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>click this link</a> to access my site.";
      } else if (/Android/i.test(ua)) {
        htmlContent = this.language === 'zh' ? "在 Android 设备上, 你需要下载 Tor Browser,点击下方按钮下载使用TorBrowser访问本网站并<a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>点击此链接</a>." :
                      this.language === 'ko' ? "Android 기기에서는 Tor Browser를 다운로드해야 합니다. 아래 버튼을 클릭하여 Tor Browser를 다운로드하고 설치한 후, 이를 사용하여 웹사이트에 접속하고 <a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>이 링크</a>를 클릭하세요." :
                      "On Android devices, you need to download Tor Browser. Click the button below to download and use Tor Browser to visit this site and <a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>click this link</a>.";
      } else if (/Linux/i.test(ua)) {
        htmlContent = this.language === 'zh' ? "在 Linux 上, 点击下方按钮下载并安装 Tor Browser,使用Tor Browser访问本网站并<a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>点击此链接</a>." :
                      this.language === 'ko' ? "Linux에서는 아래 버튼을 클릭하여 Tor Browser를 다운로드하고 설치하세요. 설치 후 Tor Browser를 사용하여 이 웹사이트를 방문하고 <a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>이 링크</a>를 클릭하세요." :
                      "On Linux, click the button below to download and install Tor Browser. Use Tor Browser to visit this website and <a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>click this link</a>.";
      } else if (/iPhone|iPad|iPod/i.test(ua)) {
        htmlContent = this.language === 'zh' ? "iOS 设备上暂无官方开发的浏览器, 不过没关系,点击下方按钮下载第三方开发的浏览器, 依旧安全!,下载完毕后使用浏览器访问本网站并<a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>点击此链接</a>." :
                      this.language === 'ko' ? "iOS 기기에는 공식적으로 개발된 브라우저가 없습니다만, 걱정하지 마세요. 아래 버튼을 클릭하여 제3자가 개발한 브라우저를 다운로드하세요. 이는 여전히 안전합니다! 다운로드 후 이 브라우저를 사용하여 웹사이트에 접속하고 <a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>이 링크</a>를 클릭하세요." :
                      "There is no officially developed browser for iOS devices, but no worries. Click the button below to download a third-party developed browser, which is still safe! After downloading, use the browser to visit this website and <a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>click this link</a>.";
      } else {
        htmlContent = this.language === 'zh' ? "请使用适合你设备的方法安装 Tor Browser, 点击下方按钮下载并使用Tor Browser访问本网站然后访问<a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>我的暗网站点</a>." :
                      this.language === 'ko' ? "장치에 적합한 방법으로 Tor Browser를 설치하세요. 아래 버튼을 클릭하여 다운로드하고 Tor Browser를 사용하여 이 웹사이트에 접속한 다음 <a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>내 다크웹 사이트</a>를 방문하세요." :
                      "Please use an appropriate method to install Tor Browser on your device. Click the button below to download and use Tor Browser to access this website and then visit <a href='http://4f34zolldwh75lheaineh6mcpo64xbg2ix7pxwgdbzouetzxmmvdqsid.onion'>my dark web site</a>.";
      }

      instructionDiv.innerHTML = htmlContent;
    }
  }
}
</script>
  
<style scoped>
  .about {
    text-align: center;
    padding: 20px;
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
  @keyframes rainbow-animation {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
  }
  .read-the-docs {
    color: #888;
  }
  .hint {
    color: #fff740;
  }
</style>
  