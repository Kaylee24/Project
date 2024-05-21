<template>
  <div>
    <Card
    v-for="data in store.comparisonPageDatas"
    :key="data.id"
    :data="data"
    />
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import Card from '@/components/ComparisonView/Card.vue'

const store = useCounterStore()

onMounted(() => {
  store.comparisonPage()
  console.log(store.comparisonPageDatas)
})



</script>

<style scoped>

</style>