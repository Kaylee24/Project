<template>
  <div v-if="photos.length" id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div 
        v-for="(photo, index) in photos" 
        :key="index" 
        class="carousel-item" 
        :class="{ active: index === 0 }">
        <div class="img-container">
          <img 
            :src="store.getImageUrl(photo.image1)" 
            class="d-block" 
            alt="Photo"
            @click="goToDetail(photo.id)">
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
import { useRouter } from 'vue-router'

const store = useCounterStore()
const router = useRouter()
const photos = computed(() => store.pictures)

onMounted(() => {
  store.getMainCountryPictures()
})

const goToDetail = (countryId) => {
  router.push({ name: 'DetailView', params: { countryId } })
}
</script>

<style>
.carousel-item .img-container {
  width: 100%;
  padding-top: 56.25%; /* 9:16 비율을 유지 */
  background-color: transparent;
  position: relative;
}

.carousel-item img {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
  cursor: pointer;
}
</style>
