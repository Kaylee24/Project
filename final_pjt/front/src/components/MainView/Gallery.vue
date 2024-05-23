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
    <!-- 이전 버튼 -->
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <!-- 다음 버튼 -->
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
  <!-- 사진이 로딩 중일 때 -->
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
// 이미지 리스트를 가지고 있음
const photos = computed(() => store.pictures);

// 컴포넌트가 마운트되면 메인 국가의 사진 가져오기
onMounted(() => {
  store.getMainCountryPictures();
});

// 상세 페이지로 이동하는 함수
const goToDetail = (countryId) => {
  router.push({ name: 'DetailView', params: { countryId } });
};
</script>

<style>
/* 이미지 컨테이너 스타일 */
.fixed-img-container {
  width: 850px;
  height: 600px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 이미지 스타일 */
.fixed-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  cursor: pointer;
}

/* 반응형 스타일 */
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

/* 로딩 메시지 스타일 */
.loading-message {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.5rem;
  height: 600px; /* 로딩 메시지를 이미지와 동일한 크기로 유지 */
}
</style>
