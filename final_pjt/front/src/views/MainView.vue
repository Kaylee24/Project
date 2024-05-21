<template>
  <div class="search-box">
    <form class="d-flex" role="search" @submit.prevent="search">
      <input class="form-control me-2" v-model="query" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success" type="submit">Search</button>
    </form>
  </div>
    
  <div class="main">
    <div class="row">
      <div class="col-lg-6 col-12">
        <Gallery />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import Gallery from '@/components/MainView/Gallery.vue';

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
  height: 500px;
  background-color: rgba(130, 206, 219, 0.63);
  margin-top: 50px;
}
</style>
