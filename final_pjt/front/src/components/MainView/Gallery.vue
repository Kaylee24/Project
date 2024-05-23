<template>
  <div v-if="photos.length" id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div 
        v-for="(photo, index) in photos" 
        :key="index" 
        class="carousel-item" 
        :class="{ active: index === 0 }">
        <div class="fixed-img-container">
          <img 
            :src="store.getImageUrl(photo.image1)" 
            class="fixed-img" 
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
  <div v-else class="loading-message">
    Loading...
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const store = useCounterStore();
const router = useRouter();
const photos = computed(() => store.pictures);

onMounted(() => {
  store.getMainCountryPictures();
});

const goToDetail = (countryId) => {
  router.push({ name: 'DetailView', params: { countryId } });
};
</script>

<style>
.fixed-img-container {
  width: 1000px; /* 더 넓은 비율로 조정 */
  height: 643px; /* 14:9 비율로 조정 */
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 15px; /* 이미지 컨테이너의 둥근 모서리 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 이미지 컨테이너의 그림자 */
}

.fixed-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  cursor: pointer;
}

@media (max-width: 850px) {
  .fixed-img-container {
    width: 100%;
    height: auto;
  }

  .fixed-img {
    width: 100%;
    height: auto;
  }
}

.loading-message {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.5rem;
  height: 643px; /* 이미지와 동일한 높이로 조정 */
}
</style>
