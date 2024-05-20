<template>
<div>
  <h5>{{ data.name }}</h5>
  <img :src="imgUrl(data.image1)" alt="" class="resized-image">
</div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const imgUrl = store.getImageUrl

defineProps({
  data: Object,
})
</script>

<style scoped>
.resized-image {
  width: 200px; /* 원하는 너비로 설정 */
  height: auto; /* 높이는 비율에 맞게 자동 조절 */
}
</style>