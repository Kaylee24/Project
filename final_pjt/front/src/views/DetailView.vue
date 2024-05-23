<template>
  <div class="detail-view">
    <div class="detail-content" v-if="data">
      <div>
        <DetailGallery :data="data" />
        <div class="button-container">
          <button class="styled-button" @click="selectVisited(data.id)">Visited</button>
          <button class="styled-button" @click="selectInterested(data.id)">Interested</button>
        </div>
      </div>
      <DetailGraph :data="data" />
    </div>
    <div v-else>
      Loading...
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import DetailGraph from '@/components/DetailView/DetailGraph.vue';
import DetailGallery from '@/components/DetailView/DetailGallery.vue';

const store = useCounterStore();
const route = useRoute();
const data = ref(null);

const selectVisited = (countryId) => {
  if (store.isLogin) {
    store.updateVisitedCountries([countryId]);
  } else {
    alert('로그인이 필요합니다.');
  }
};

const selectInterested = (countryId) => {
  if (store.isLogin) {
    store.updateInterestedCountries([countryId]);
  } else {
    alert('로그인이 필요합니다.');
  }
};

watch(
  () => route.params.countryId,
  async (newId) => {
    await store.detailCountry(newId);
    data.value = store.detailCountryData;
  },
  { immediate: true }
);
</script>

<style scoped>
.detail-view {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.detail-content {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: center;
}

.detail-content > * {
  flex: 1;
  margin: 0 10px; 
}

.button-container {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  gap: 10px;
}

.styled-button {
  padding: 10px 20px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.styled-button:hover {
  background-color: #0056b3;
}
</style>
