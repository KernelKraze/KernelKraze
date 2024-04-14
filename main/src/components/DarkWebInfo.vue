<!-- DarkWebExplanation.vue -->
<template>
    <div class="dark-web-explanation">
      <section>
        <h1>{{ localizedContent.title }}</h1>
        <p v-html="localizedContent.introduction"></p>
        <h2>{{ localizedContent.featuresTitle }}</h2>
        <p v-html="localizedContent.anonymity"></p>
        <p v-html="localizedContent.privacy"></p>
        <p v-html="localizedContent.accessRestrictions"></p>
        <h2>{{ localizedContent.legalConsiderationsTitle }}</h2>
        <p v-html="localizedContent.legalUse"></p>
        <p v-html="localizedContent.illegalActivities"></p>
        <h2>{{ localizedContent.securityConcernsTitle }}</h2>
        <p v-html="localizedContent.securityRisks"></p>
        <p v-html="localizedContent.surveillancePossibility"></p>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DarkWebExplanation',
    computed: {
      localizedContent() {
        const lang = navigator.language;
        if (lang.startsWith('zh')) {
          return this.content.zh;
        } else if (lang.startsWith('ko')) {
          return this.content.ko;
        } else {
          return this.content.en; // Default to English if the locale is not Chinese or Korean
        }
      },
      content() {
        return {
          en: {
            title: "About the Dark Web",
            introduction: "The Dark Web is a part of the internet that cannot be accessed through standard browsers; it requires special software, configurations, or authorization. A typical example of these networks are sites accessed via the Tor network, which end in '.onion' and cannot be directly accessed through ordinary browsers.",
            featuresTitle: "Features of the Dark Web",
            anonymity: "<strong>Anonymity:</strong> The primary feature of the dark web is that it provides anonymity. Users and website operators can interact while protecting their identities.",
            privacy: "<strong>Privacy Protection:</strong> Due to its high level of anonymity, the dark web is often used to handle transactions involving privacy.",
            accessRestrictions: "<strong>Access Restrictions:</strong> Unlike ordinary websites, dark web sites cannot be found using traditional search engines.",
            legalConsiderationsTitle: "Legal and Ethical Considerations of Using the Dark Web",
            legalUse: "<strong>Legal Use:</strong> Although the dark web is notorious for some illegal activities, it also has many legitimate uses.",
            illegalActivities: "<strong>Illegal Activities:</strong> Indeed, the dark web is also used for various illegal transactions.",
            securityConcernsTitle: "Security Concerns",
            securityRisks: "<strong>Security Risks:</strong> The dark web is not entirely safe, and users may face phishing attacks, malware infections, and other forms of network attacks.",
            surveillancePossibility: "<strong>Surveillance Possibility:</strong> Although the dark web offers a high degree of anonymity, complete anonymity is still challenging under certain circumstances, especially when it involves advanced network monitoring technologies."
          },
          zh: {
            title: "关于暗网",
            introduction: "暗网(Dark Web)通常是指在互联网上无法通过标准的浏览器访问的一部分, 需要特殊软件, 配置或授权才能进入. 这些网络的一个典型例子是使用Tor网络访问的网站, 这些网站以'.onion'结尾, 不能通过普通的浏览器直接访问.",
            featuresTitle: "暗网的特点",
            anonymity: "<strong>匿名性:</strong>暗网最主要的特性是提供匿名性. 用户和网站运营者可以在保护其身份的情况下进行交互.",
            privacy: "<strong>隐私保护:</strong>由于其高度的匿名性, 暗网常被用来处理涉及隐私的交易.",
            accessRestrictions: "<strong>访问限制:</strong>不同于普通的网站, 暗网网站不能通过传统的搜索引擎找到.",
            legalConsiderationsTitle: "使用暗网的法律和道德考量",
            legalUse: "<strong>合法用途:</strong>暗网虽然因一些非法活动而臭名昭著, 但它也有许多合法用途.",
            illegalActivities: "<strong>非法活动:</strong>确实, 暗网也被用于各种非法交易.",
            securityConcernsTitle: "安全顾虑",
            securityRisks: "<strong>安全风险：</strong>暗网并非完全安全, 用户可能遭遇钓鱼攻击, 恶意软件感染, 以及其他形式的网络攻击.",
            surveillancePossibility: "<strong>监控可能：</strong>尽管暗网提供了较高的匿名性, 但在某些情况下, 特别是涉及到先进的网络监控技术时, 完全的匿名仍然是有挑战的."
          },
          ko: {
            title: "암넷(DarkWeb)에 대하여",
            introduction: "암넷(Dark Web)은 일반적인 브라우저로 접근할 수 없는 인터넷의 일부로, 특수 소프트웨어, 설정 또는 인증을 통해서만 접근할 수 있습니다. 이러한 네트워크의 전형적인 예는 Tor 네트워크를 통해 접근되는 사이트로, 이들 사이트는 '.onion'으로 끝나며 일반 브라우저로는 직접 접근할 수 없습니다.",
            featuresTitle: "암넷의 특성",
            anonymity: "<strong>익명성:</strong>암넷의 가장 주요한 특성은 익명성을 제공하는 것입니다. 사용자와 웹사이트 운영자는 신원을 보호하면서 상호 작용할 수 있습니다.",
            privacy: "<strong>개인 정보 보호:</strong>높은 수준의 익명성 덕분에 암넷은 종종 개인 정보와 관련된 거래를 처리하는 데 사용됩니다.",
            accessRestrictions: "<strong>접근 제한:</strong>일반 사이트와 달리 암넷 사이트는 전통적인 검색 엔진으로 찾을 수 없습니다.",
            legalConsiderationsTitle: "암넷 사용시 법적 및 도덕적 고려 사항",
            legalUse: "<strong>합법적 사용:</strong>암넷은 일부 불법 활동으로 악명이 높지만, 많은 합법적 용도가 있습니다.",
            illegalActivities: "<strong>불법 활동:</strong>실제로, 암넷은 다양한 불법 거래에 사용되기도 합니다.",
            securityConcernsTitle: "보안 고려 사항",
            securityRisks: "<strong>보안 위험:</strong>암넷은 완전히 안전하지 않으며, 사용자는 피싱 공격, 악성 소프트웨어 감염 등 다양한 네트워크 공격에 직면할 수 있습니다.",
            surveillancePossibility: "<strong>감시 가능성:</strong>암넷은 높은 수준의 익명성을 제공하지만, 특정 상황에서는 여전히 감시가 가능할 수 있습니다."
          }
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .dark-web-explanation h1, .dark-web-explanation h2 {
    color: #333; /* Dark gray for headings */
  }
  
  .dark-web-explanation p {
    font-size: 16px;
    line-height: 1.6; /* Improve readability with more line spacing */
  }
  
  /* Styling for <strong> tags to make them stand out */
  .dark-web-explanation strong {
    color: #c00; /* Deep red color for emphasis */
    font-weight: bold; /* Ensure it's bold if not already */
  }
  </style>
  