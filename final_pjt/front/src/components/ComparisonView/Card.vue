<template>
<div>
  <img :src="imgUrl(data.image1)" alt="" class="resized-image">
  <h5>{{ data.name }}</h5>
  <p>{{ data.code }}</p>
  <p>{{ data.rate }}</p>
  <p>{{ burger }}\</p>
  <p>{{ coffee }}\</p>
  <img :src="imgUrl(data.graph)" alt="" class="resized-image">
</div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const imgUrl = store.getImageUrl


const props = defineProps({
  data: Object,
})

const burger = (Math.round(props.data.burger * props.data.rate / 10)) * 10
const coffee = (Math.round(props.data.coffee * props.data.rate / 10)) * 10

// console.log((Math.round(props.data.burger * props.data.rate / 10)) * 10)

</script>

<style scoped>
.resized-image {
  width: 200px; /* 원하는 너비로 설정 */
  height: auto; /* 높이는 비율에 맞게 자동 조절 */
}
</style>