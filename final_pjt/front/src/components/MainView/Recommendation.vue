<template>
  <div class="recommendation-container">
    <h2>Travel Recommendations</h2>
    <form @submit.prevent="getRecommendations">
      <div class="mb-3">
        <label for="country" class="form-label">Desired Country</label>
        <input type="text" class="form-control" id="country" v-model="country" required>
      </div>
      <div class="mb-3">
        <label for="budget" class="form-label">Budget</label>
        <input type="number" class="form-control" id="budget" v-model="budget" required>
      </div>
      <div class="mb-3">
        <label for="days" class="form-label">Days</label>
        <input type="number" class="form-control" id="days" v-model="days" required>
      </div>
      <button type="submit" class="btn btn-primary">Get Recommendations</button>
    </form>
    <RecommendationModal v-if="showModal" :recommendations="recommendations" @close="showModal = false"/>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import RecommendationModal from '@/components/RecommendationModal.vue';

const store = useCounterStore();
const country = ref('');
const budget = ref('');
const days = ref('');
const showModal = ref(false);
const recommendations = ref([]);

const getRecommendations = async () => {
  const response = await store.getTravelRecommendations({ country: country.value, budget: budget.value, days: days.value });
  console.log('Recommendations:', response);  // 응답 데이터 로그 출력
  if (response && response.length) {
    recommendations.value = response;
    showModal.value = true;
  } else {
    console.error('Failed to get recommendations or no recommendations found');
  }
};
</script>

<style scoped>
.recommendation-container {
  padding: 0 20px;
}

@media (max-width: 768px) {
  .recommendation-container {
    padding: 0 15px;
  }
}
</style>
