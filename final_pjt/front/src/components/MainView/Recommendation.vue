<template>
  <div class="recommendation-container">
    <h2 class="recommendation-title">Travel Recommendations</h2>
    <form @submit.prevent="getRecommendations">
      <div class="mb-3">
        <label for="country" class="form-label">Desired Country</label>
        <input type="text" class="form-control custom-width" id="country" v-model="countryInput" required>
      </div>
      <div class="mb-3">
        <label for="budget" class="form-label">Budget</label>
        <input type="text" class="form-control custom-width" id="budget" v-model="formattedBudget" @input="formatBudget" required>
        <p class="small-text korean-font">* 항공비와 숙박비를 제외한 경비를 입력해주세요!</p>
      </div>
      <div class="mb-3">
        <label for="days" class="form-label">Days</label>
        <input type="number" class="form-control custom-width" id="days" v-model="days" required>
      </div>
      <div class="button-container">
        <button type="submit" class="btn btn-primary">Get Recommendations</button>
      </div>
    </form>
    <p v-if="errorMessage" class="error-message korean-font">{{ errorMessage }}</p>
    <RecommendationModal v-if="showModal" :recommendations="recommendations" :inputCountry="country" @close="showModal = false"/>
    <div class="button-container">
      <button class="btn btn-outline-info help-button" @click="toggleHelpModal">Help</button>
    </div>
    <HelpModal v-if="isHelpModalVisible" @close="toggleHelpModal" />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useCounterStore } from '@/stores/counter';
import RecommendationModal from '@/components/RecommendationModal.vue';
import HelpModal from '@/components/MainView/HelpModal.vue';

// 유로존 국가 목록 (영어와 한글)
const eurozoneCountries = [
  'Austria', '오스트리아',
  'Belgium', '벨기에',
  'Cyprus', '키프로스',
  'Estonia', '에스토니아',
  'Finland', '핀란드',
  'France', '프랑스',
  'Germany', '독일',
  'Greece', '그리스',
  'Ireland', '아일랜드',
  'Italy', '이탈리아',
  'Latvia', '라트비아',
  'Lithuania', '리투아니아',
  'Luxembourg', '룩셈부르크',
  'Malta', '몰타',
  'Netherlands', '네덜란드',
  'Portugal', '포르투갈',
  'Slovakia', '슬로바키아',
  'Slovenia', '슬로베니아',
  'Spain', '스페인'
];

// 대만 변환 목록
const taiwanVariants = ['타이완', '중화민국'];

const store = useCounterStore();
const country = ref('');
const countryInput = ref('');
const budget = ref('');
const formattedBudget = ref('');
const days = ref('');
const showModal = ref(false);
const recommendations = ref([]);
const isHelpModalVisible = ref(false);
const errorMessage = ref('');

// countryInput을 감시하여 유로존 국가 및 대만 변환 확인
watch(countryInput, (newCountry) => {
  if (eurozoneCountries.includes(newCountry)) {
    country.value = '유럽';
  } else if (taiwanVariants.includes(newCountry)) {
    country.value = '대만';
  } else {
    country.value = newCountry;
  }
  errorMessage.value = ''; // Clear the error message when the country input changes
});

// budget과 formattedBudget을 동기화
watch(budget, (newBudget) => {
  formattedBudget.value = newBudget.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
});

// 숫자 형식을 포맷하는 함수
const formatBudget = () => {
  const numericValue = parseInt(formattedBudget.value.replace(/,/g, '')) || 0;
  budget.value = numericValue;
  formattedBudget.value = numericValue.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
};

const getRecommendations = async () => {
  const response = await store.getTravelRecommendations({ country: country.value, budget: budget.value, days: days.value });
  console.log('Recommendations:', response);
  if (response && response.length) {
    recommendations.value = response;
    showModal.value = true;
    errorMessage.value = ''; // Clear the error message if recommendations are found
  } else {
    console.error('Failed to get recommendations or no recommendations found');
    errorMessage.value = '서비스를 준비중인 국가입니다.';
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

.error-message {
  font-size: 14px;
  color: red;
  margin-top: 10px;
}

.korean-font {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 500;
}
</style>
