<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import BrandMark from './components/BrandMark.vue'
import FeatureIcon from './components/FeatureIcon.vue'

type MessageResponse = {
  message: string
}


/* ---------- 后端连接状态（沿用原项目逻辑） ---------- */
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000'
const message = ref('')
const errorMessage = ref('')
const isLoading = ref(false)

const statusLabel = computed(() => {
  if (isLoading.value) return '正在连接后端'
  if (errorMessage.value) return '后端暂不可用'
  if (message.value) return message.value
  return '等待连接'
})

async function fetchMessage() {
  isLoading.value = true
  message.value = ''
  errorMessage.value = ''

  try {
    const response = await fetch(`${apiBaseUrl}/api/message`)
    if (!response.ok) {
      throw new Error(`服务器返回错误（HTTP ${response.status}）`)
    }

    const data = (await response.json()) as MessageResponse
    if (!data.message) {
      throw new Error('接口响应中没有 message 字段')
    }
    message.value = data.message
  } catch (error) {
    errorMessage.value = error instanceof Error ? error.message : '请求失败'
  } finally {
    isLoading.value = false
  }
}

onMounted(fetchMessage)

/* ---------- 页面内容 ---------- */
const features = [
  { icon: 'profile', title: '基本资料', text: '名字、品种、生日、性格，每只猫一张清楚的档案卡。' },
  { icon: 'weight', title: '体重记录', text: '定期记一笔，体重变化一目了然，胖瘦心里有数。' },
  { icon: 'vaccine', title: '疫苗驱虫', text: '记录接种和驱虫日期，到期前提醒，不再靠记性。' },
  { icon: 'clinic', title: '就诊记录', text: '症状、诊断、用药和复诊时间，看病时随手就能翻。' },
] as const

const steps = [
  { title: '添加猫咪', text: '为家里的每只猫建立档案，填写基本信息。' },
  { title: '随手记录', text: '称体重、打疫苗、去医院，家里任何人都能记。' },
  { title: '按时提醒', text: '疫苗、驱虫、复诊快到期时，在首页提前看到。' },
]

const ctaNote = ref('')
function startRecording() {
  ctaNote.value = '猫咪档案功能正在开发中，敬请期待。'
}
</script>

<template>
  <a class="skip-link" href="#main">跳到主要内容</a>

  <header class="topbar">
    <div class="container topbar-inner">
      <a class="brand" href="#top"><BrandMark />喵家档案</a>
      <nav class="nav" aria-label="页面导航">
        <a href="#features">功能</a>
        <a href="#steps">使用方法</a>
        <a href="#start">开始</a>
      </nav>
      <a class="btn btn-primary btn-sm" href="#start">开始记录</a>
    </div>
  </header>

  <main id="main">
    <section id="top" class="container hero" aria-labelledby="hero-title">
      <div class="hero-copy">
        <p class="eyebrow">多猫家庭记录系统</p>
        <h1 id="hero-title">每一只猫，<br />都有自己的档案</h1>
        <p class="lead">体重、饮食、疫苗、驱虫和就诊，一家人一起记录，一起照顾。不用再翻聊天记录找上次打针的日期。</p>
        <div class="actions">
          <a class="btn btn-primary" href="#start">开始记录</a>
          <a class="btn btn-secondary" href="#features">了解功能</a>
        </div>
      </div>
      <div class="hero-art">
        <div class="photo-album" aria-label="一只在窗边休息的猫咪照片">
          <div class="photo-tape" aria-hidden="true"></div>
          <img src="/welcome-cat.jpg" alt="一只在窗边休息的灰色虎斑猫" />
        </div>
      </div>
    </section>

    <section id="features" class="section" aria-labelledby="features-title">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">功能</p>
          <h2 id="features-title">照顾猫咪需要记住的事，都放在这里</h2>
          <p>四类记录覆盖日常照护，家人之间共享同一份信息。</p>
        </div>
        <div class="feature-grid">
          <article v-for="f in features" :key="f.title" class="feature">
            <div class="feature-icon"><FeatureIcon :name="f.icon" /></div>
            <h3>{{ f.title }}</h3>
            <p>{{ f.text }}</p>
          </article>
        </div>
      </div>
    </section>

    <section id="steps" class="section" aria-labelledby="steps-title">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">使用方法</p>
          <h2 id="steps-title">三步开始</h2>
        </div>
        <ol class="steps">
          <li v-for="(s, i) in steps" :key="s.title" class="step">
            <span class="step-num" aria-hidden="true">{{ i + 1 }}</span>
            <h3>{{ s.title }}</h3>
            <p>{{ s.text }}</p>
          </li>
        </ol>
      </div>
    </section>

    <section id="start" class="section" aria-labelledby="cta-title">
      <div class="container">
        <div class="cta">
          <h2 id="cta-title">为你家的猫建立第一份档案</h2>
          <p>从名字和一张照片开始，之后的每一次称重和体检都会被好好记下。</p>
          <div class="actions">
            <button class="btn btn-primary" type="button" @click="startRecording">创建猫咪档案</button>
            <a class="btn btn-secondary" href="#features">再看看功能</a>
          </div>
          <p class="cta-note" aria-live="polite">{{ ctaNote }}</p>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer-inner">
      <span>喵家档案 · 为家里的每一只猫</span>
      <span
        class="status"
        :class="{ 'is-online': message, 'is-error': errorMessage, 'is-loading': isLoading }"
        aria-live="polite"
      >
        <span class="status-dot" aria-hidden="true"></span>
        <span>{{ statusLabel }}</span>
        <button v-if="errorMessage" class="status-retry" type="button" @click="fetchMessage">重试</button>
      </span>
    </div>
  </footer>

</template>
