<template>
  <div class="search-box">
    <form class="d-flex" role="search" @submit.prevent="search">
      <input class="form-control me-2" v-model="query" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success" type="submit">Search</button>
    </form>
  </div>
    
  <div class="main">
    <div class="main-content">
      <div class="gallery-container">
        <Gallery />
      </div>
      <div class="recommendation-container">
        <Recommendation />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';
import Gallery from '@/components/MainView/Gallery.vue';
import Recommendation from '@/components/MainView/Recommendation.vue';

const query = ref('');
const store = useCounterStore();
const router = useRouter();

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

<style>
.search-box {
  margin: 20px auto;
  max-width: 600px;
  padding: 0 20px;
}

.main {
  background-color: #B3E5Fc;
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
  max-width: 1200px;
  padding: 20px;
  box-sizing: border-box;
}

.gallery-container, .recommendation-container {
  padding: 10px;
  box-sizing: border-box;
}

.gallery-container {
  flex: 1 1 297px;
  max-width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.recommendation-container {
  flex: 2 1 600px;
  max-width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

@media (max-width: 1150px) {
  .gallery-container {
    margin: 0 auto;
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
