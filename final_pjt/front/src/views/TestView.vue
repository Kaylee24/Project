<template>
  <div>
    <h1>Test</h1>
    <ul
    v-for="picture in store.pictures"
    :key="picture.id"  
    >
      <li>
        그림 : {{ picture.image1 }}
      </li>
      <li>
        그림 : <img :src="getImageUrl(picture.image1)" alt="img">
      </li>
      <hr>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

onMounted(() => {
  store.getMainCountryPictures()
  console.log(store.pictures)
})

const getImageUrl = (imagePath) => {
  return `http://127.0.0.1:8000/static${imagePath}`
}

</script>

<style scoped>
ul {
  list-style: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}
</style>