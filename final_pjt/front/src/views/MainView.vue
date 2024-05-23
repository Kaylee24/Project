<template>
  <div class="main">
    <div class="main-content">
      <!-- 갤러리 -->
      <div class="gallery-container">
        <Gallery />
      </div>
      <!-- 추천 -->
      <div class="recommendation-container">
        <Recommendation />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import Gallery from '@/components/MainView/Gallery.vue';
import Recommendation from '@/components/MainView/Recommendation.vue';

// 검색어
const query = ref('');
// 카운터 스토어
const store = useCounterStore();

// 검색 함수
const search = async () => {
  try {
    const country = await store.searchCountry(query.value);
    if (country && country.id) {
      router.push({ name: 'DetailView', params: { countryId: country.id } });
    } else {
      alert('Country not found');
    }
  } catch (error) {
    console.error(error);
    alert('Error occurred while searching');
  }
};
</script>

<style scoped>
/* 메인 스타일 */
.main {
  background-color: #B3E5Fc;
  margin-top: 50px;
  min-height: 600px;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 메인 콘텐츠 스타일 */
.main-content {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  max-width: 1500px;
  padding: 20px;
  box-sizing: border-box;
  justify-content: space-between;
}

/* 갤러리 컨테이너 스타일 */
.gallery-container, .recommendation-container {
  padding: 5px;
  box-sizing: border-box;
}

/* 갤러리 컨테이너 스타일 */
.gallery-container {
  flex: 1 1 60%;
  max-width: 60%;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 추천 컨테이너 스타일 */
.recommendation-container {
  flex: 1 1 40%;
  max-width: 40%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/* 반응형 스타일 */
@media (max-width: 1150px) {
  .gallery-container, .recommendation-container {
    margin: 0 auto;
    max-width: 100%;
    flex: 1 1 100%;
  }
}

@media (max-width: 850px) {
  .main-content {
    flex-direction: column;
  }

  .gallery-container, .recommendation-container {
    flex: 1 1 100%;
    max-width: 100%;
  }
}
</style>
