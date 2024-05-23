<template>
  <div class="recommendation-container">
    <h2 class="recommendation-title">Travel Recommendations</h2>
    <form @submit.prevent="getRecommendations">
      <div class="mb-3">
        <label for="country" class="form-label">Desired Country</label>
        <input type="text" class="form-control custom-width" id="country" v-model="country" required>
      </div>
      <div class="mb-3">
        <label for="budget" class="form-label">Budget</label>
        <input type="number" class="form-control custom-width" id="budget" v-model="budget" required>
        <p class="small-text">* 항공비와 숙박비를 제외한 경비를 입력해주세요!</p>
      </div>
      <div class="mb-3">
        <label for="days" class="form-label">Days</label>
        <input type="number" class="form-control custom-width" id="days" v-model="days" required>
      </div>
      <div class="button-container">
        <button type="submit" class="btn btn-primary">Get Recommendations</button>
      </div>
    </form>
    <RecommendationModal v-if="showModal" :recommendations="recommendations" :inputCountry="country" @close="showModal = false"/>
    <div class="button-container">
      <button class="btn btn-outline-info help-button" @click="toggleHelpModal">Help</button>
    </div>
    <HelpModal v-if="isHelpModalVisible" @close="toggleHelpModal" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import RecommendationModal from '@/components/RecommendationModal.vue';
import HelpModal from '@/components/MainView/HelpModal.vue';

const store = useCounterStore();
const country = ref('');
const budget = ref('');
const days = ref('');
const showModal = ref(false);
const recommendations = ref([]);
const isHelpModalVisible = ref(false);

const getRecommendations = async () => {
  const response = await store.getTravelRecommendations({ country: country.value, budget: budget.value, days: days.value });
  console.log('Recommendations:', response);
  if (response && response.length) {
    recommendations.value = response;
    showModal.value = true;
  } else {
    console.error('Failed to get recommendations or no recommendations found');
  }
};

const toggleHelpModal = () => {
  isHelpModalVisible.value = !isHelpModalVisible.value;
};
</script>

<style scoped>
.recommendation-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 30px 20px;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  width: 100%;
  margin: 20px;
}

.recommendation-title {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
  font-size: 1.8rem; /* 제목의 폰트 크기 */
  font-weight: bold; /* 제목의 폰트 두께 */
}

.form-control.custom-width {
  width: 100%;
}

.button-container {
  display: flex;
  justify-content: center;
  width: 100%;
  margin-top: 15px;
}

.help-button {
  margin-top: 10px;
}

.small-text {
  font-size: 12px;
  color: #555555; /* 텍스트 색상 조정 */
  margin-top: 5px;
}
</style>
