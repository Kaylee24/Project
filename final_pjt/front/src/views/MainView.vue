<template>
  <div class="main">
    <div class="main-content">
      <!-- 갤러리 -->
      <div class="gallery-container">
        <Gallery />
      </div>
      <!-- 추천 -->
      <div class="recommendation-wrapper">
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

const query = ref('');
const store = useCounterStore();

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
.main {
  background-color: #f0f8ff; /* 더 부드러운 배경색 */
  margin-top: 50px;
  min-height: 600px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.main-content {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  max-width: 1400px;
  padding: 20px;
  box-sizing: border-box;
  justify-content: space-between;
}

.gallery-container, .recommendation-wrapper {
  padding: 20px;
  box-sizing: border-box;
}

.gallery-container {
  flex: 1 1 60%; /* 더 넓은 비율 할당 */
  max-width: 60%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.recommendation-wrapper {
  flex: 1 1 35%; /* 더 좁은 비율 할당 */
  max-width: 35%;
  display: flex;
  justify-content: center;
  align-items: center;
}

@media (max-width: 1150px) {
  .gallery-container, .recommendation-wrapper {
    margin: 0 auto;
    max-width: 100%;
    flex: 1 1 100%;
  }
}

@media (max-width: 850px) {
  .main-content {
    flex-direction: column;
  }

  .gallery-container, .recommendation-wrapper {
    flex: 1 1 100%;
    max-width: 100%;
  }
}
</style>
