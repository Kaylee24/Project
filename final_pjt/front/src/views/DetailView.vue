<template>
  <div>
    <h1>Detail View</h1>
  </div>
</template>

<script setup>
import { ref, onMounted, defineProps } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const countryId = ref(null)
const props = defineProps(['countryId']) // props 정의

onMounted(() => {
  countryId.value = props.countryId // props로 전달받은 countryId 사용
  // console.log('hi')
  // console.log(countryId.value)
  // console.log('hi')
  store.detailCountry(countryId.value) // 국가 데이터 요청
  console.log(store.detailContryData)
})
</script>
