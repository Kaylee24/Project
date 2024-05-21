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
  width: 850px;
  height: 600px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
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
</style>
