<template>
  <div class="detail-view">
    <div class="detail-content">
      <DetailCountry :data="data" />
      <DetailGraph :data="data" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, defineProps } from 'vue'
import { useCounterStore } from '@/stores/counter'
import DetailCountry from '@/components/DetailView/DetailCountry.vue'
import DetailGraph from '@/components/DetailView/DetailGraph.vue'

const store = useCounterStore()
const countryId = ref(null)
const props = defineProps(['countryId']) // props 정의
const data = store.detailContryData

onMounted(() => {
  countryId.value = props.countryId // props로 전달받은 countryId 사용
  store.detailCountry(countryId.value) // 국가 데이터 요청
})
</script>

<style scoped>
.detail-view {
  display: flex;
  justify-content: center;
}

.detail-content {
  display: flex;
}

/* 아래 스타일은 DetailCountry와 DetailGraph에도 적용되어야 합니다. */
.detail-content > * {
  flex: 1;
  margin: 0 10px; 
}
</style>
