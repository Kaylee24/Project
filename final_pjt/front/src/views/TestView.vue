<template>
<div>

</div>
</template>

<script setup>
import { ref } from 'vue'
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

onMounted(() => {
  store.getMainCountryPictures()
})

</script>

<style scoped>

</style>