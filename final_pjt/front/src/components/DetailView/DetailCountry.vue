<template>
  <div>
    <h3>{{ data.name }}</h3>
    <img
    :src="imgUrl(data.image1)" alt="" class="resized-image">
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue'

const store = useCounterStore()

const imgUrl = store.getImageUrl

defineProps({
  data: Object
})

</script>

<style scoped>

.resized-image {
  width: 100%;
  height: auto;
}
</style>