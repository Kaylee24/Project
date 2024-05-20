<template>
  <div v-if="photos.length" id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div 
        v-for="(photo, index) in photos" 
        :key="index" 
        class="carousel-item" 
        :class="{ active: index === 0 }">
        <div class="img-container">
          <img :src="getImageUrl(photo.image1)" class="d-block w-100" alt="Photo">
        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
  <div v-else>
    Loading...
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const photos = computed(() => store.pictures)

onMounted(() => {
  store.getMainCountryPictures()
})

const getImageUrl = (imagePath) => {
  return `http://127.0.0.1:8000${imagePath}`
}
</script>

<style>
.carousel-item .img-container {
  width: 100%;
  height: 500px; /* 원하는 높이 설정 */
  overflow: hidden; /* 이미지가 넘치는 부분을 숨김 */
}

.carousel-item img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 이미지 비율을 유지하면서 컨테이너에 맞춤 */
}
</style>
