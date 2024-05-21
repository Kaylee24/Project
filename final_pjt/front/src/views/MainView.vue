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
  margin: 80px 200px 60px;
}

.main {
  background-color: #B3E5Fc;
  margin-top: 50px;
  height: 600px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.main-content {
  display: flex;
  width: 100%;
  height: 100%;
}

.gallery-container, .recommendation-container {
  padding: 0;
  display: flex;
  align-items: center;
}

.gallery-container {
  width: 297px;
  margin-left: 150px;
}

.recommendation-container {
  flex-grow: 1;
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
  
  .gallery-container {
    width: 100%;
  }

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
