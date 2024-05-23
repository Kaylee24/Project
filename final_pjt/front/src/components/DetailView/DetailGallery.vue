<template>
  <div v-if="photos.length" id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel" style="margin-top: 5%;">
    <div class="carousel-inner">
      <div 
        v-for="(photo, index) in photos" 
        :key="index" 
        class="carousel-item" 
        :class="{ active: index === 0 }">
        <div class="fixed-img-container">
          <img 
            :src="store.getImageUrl(photo)" 
            class="fixed-img" 
            alt="Photo">
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
import { computed, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const store = useCounterStore();
const router = useRouter();
const imgUrl = store.getImageUrl

const props = defineProps({
  data: Object
})

const photos = [props.data.image1, props.data.image2, props.data.image3]

// console.log(photos)

</script>

<style>
.fixed-img-container {
  width: 80%;
  height: 600px; /* 일정한 높이로 고정 */
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px auto;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
}

.fixed-img-container:hover {
  transform: scale(1.05);
}

.fixed-img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 이미지 자르기 */
  object-position: center; /* 중앙 부분을 보여줌 */
  cursor: pointer;
  border-radius: 15px;
}

.carousel-control-prev, .carousel-control-next {
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
}

@media (max-width: 850px) {
  .fixed-img-container {
    width: 100%;
    height: auto;
  }

  .fixed-img {
    width: 100%;
    height: auto;
    object-fit: cover;
    object-position: center;
  }
}
</style>
