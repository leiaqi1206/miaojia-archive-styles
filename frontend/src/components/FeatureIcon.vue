<script setup lang="ts">
// 线性图标：stroke 使用 currentColor，颜色由外层 .feature-icon 的 color 决定，随风格变化。
defineProps<{ name: 'profile' | 'weight' | 'vaccine' | 'clinic' }>()
</script>

<template>
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <template v-if="name === 'profile'">
      <rect x="3" y="4" width="18" height="16" rx="2" />
      <circle cx="9" cy="11" r="2.5" />
      <path d="M5.5 17c.8-1.8 2-2.5 3.5-2.5s2.7.7 3.5 2.5" />
      <path d="M15 9.5h3M15 13h3" />
    </template>
    <template v-else-if="name === 'weight'">
      <path d="M6 7h12l2 13H4L6 7z" />
      <circle cx="12" cy="7" r="3" />
      <path d="M12 12v4M10 16h4" />
    </template>
    <template v-else-if="name === 'vaccine'">
      <path d="M17 3l4 4M19 5l-9.5 9.5M14 6l4 4M7 13l4 4M5 19l3-3" />
      <path d="M8.5 11.5l4 4" />
    </template>
    <template v-else>
      <path d="M12 21s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.5-7 10-7 10z" />
      <path d="M12 10v5M9.5 12.5h5" />
    </template>
  </svg>
</template>
