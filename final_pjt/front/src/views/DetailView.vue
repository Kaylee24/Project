<template>
  <div class="detail-view">
    <div class="detail-content" v-if="data">
      <div>
        <DetailGallery :data="data" />
        <div class="button-container">
          <button class="styled-button" :class="{ 'visited': isVisited, 'unvisited': !isVisited }" @click="toggleVisited(data.id)">
            {{ isVisited ? 'Unvisit' : 'Visited' }}
          </button>
          <button class="styled-button" :class="{ 'interested': isInterested, 'uninterested': !isInterested }" @click="toggleInterested(data.id)">
            {{ isInterested ? 'Uninterested' : 'Interested' }}
          </button>
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
const isVisited = ref(false);
const isInterested = ref(false);

const checkVisitedAndInterested = () => {
  if (data.value) {
    isVisited.value = store.profileData.visited.some(country => country.id === data.value.id);
    isInterested.value = store.profileData.interested.some(country => country.id === data.value.id);
  }
};

const toggleVisited = async (countryId) => {
  if (store.isLogin) {
    await store.updateVisitedCountries([countryId]);
    checkVisitedAndInterested();
  } else {
    alert('로그인이 필요합니다.');
  }
};

const toggleInterested = async (countryId) => {
  if (store.isLogin) {
    await store.updateInterestedCountries([countryId]);
    checkVisitedAndInterested();
  } else {
    alert('로그인이 필요합니다.');
  }
};

const fetchCountryData = async (countryId) => {
  data.value = null; // 이전 데이터 초기화
  await store.detailCountry(countryId);
  data.value = store.detailCountryData;
  checkVisitedAndInterested();
};

watch(
  () => route.params.countryId,
  async (newId) => {
    if (newId) {
      await fetchCountryData(newId);
    }
  },
  { immediate: true }
);

onMounted(async () => {
  if (route.params.countryId) {
    await fetchCountryData(route.params.countryId);
  }
});
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
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.visited {
  background-color: #6c757d; /* Green */
  color: white;
}

.unvisited {
  background-color: #007bff; /* blue */
  color: white;
}

.interested {
  background-color: #6c757d; /* Yellow */
  color: white;
}

.uninterested {
  background-color: #28a745; /* Gray */
  color: white;
}

.styled-button:hover {
  filter: brightness(90%);
}
</style>
