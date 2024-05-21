<template>
  <div class="search-box">
    <form class="d-flex" role="search" @submit.prevent="search">
      <input class="form-control me-2" v-model="query" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success" type="submit">Search</button>
    </form>
  </div>
    
  <div class="main d-flex flex-column align-items-center">
    <div class="row main-content w-100">
      <div class="col-lg-6 col-12 gallery-container">
        <Gallery />
      </div>
      <div class="col-lg-6 col-12 recommendation-container">
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

const search = () => {
  // Implement search functionality if needed
};
</script>

<style>
.search-box {
  margin-top: 30px;
  margin-bottom: 30px;
  margin-right: 200px;
  margin-left: 200px;
}

.main {
  background-color: rgba(130, 206, 219, 0.63);
  margin-top: 50px;
  height: 530px;
  justify-content: center;
}

.main-content {
  display: flex;
  flex-wrap: wrap;
}

.gallery-container, .recommendation-container {
  padding: 0;
}

@media (max-width: 768px) {
  .gallery-container, .recommendation-container {
    flex: 0 0 100%;
    max-width: 100%;
  }
  .main {
    height: auto;
  }
}
</style>
