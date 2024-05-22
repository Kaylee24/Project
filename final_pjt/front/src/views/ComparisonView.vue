<template>
  <div class="card-container">
    <Card
      v-for="data in store.comparisonPageDatas"
      :key="data.id"
      :data="data"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import Card from '@/components/ComparisonView/Card.vue'

const store = useCounterStore()

onMounted(() => {
  store.comparisonPage()
  console.log(store.comparisonPageDatas)
})

</script>

<style scoped>
.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px; /* 카드 간의 간격 */
}

.card-container > * {
  flex: 1 1 calc(20% - 16px); /* 한 줄에 3개씩 배치 */
  box-sizing: border-box; /* 패딩과 보더를 포함한 크기 계산 */
}
</style>
