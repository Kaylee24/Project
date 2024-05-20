<template>
  <div>
    <ComparisonPage
    v-for="data in store.comparisonPageDatas"
    :key="data.id"
    :data="data"
    />
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ComparisonPage from '@/components/ComparisonPage.vue'

const store = useCounterStore()

onMounted(() => {
  store.comparisonPage()
  console.log(store.comparisonPageDatas)
})

</script>

<style scoped>

</style>