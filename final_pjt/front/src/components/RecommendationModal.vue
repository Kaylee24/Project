<template>
  <div class="modal show d-block" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Travel Recommendations</h5>
          <button type="button" class="btn-close" @click="$emit('close')" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <!-- Desired Country에 대한 추천 결과 -->
          <template v-if="inputCountryRecommendations.length">
            <h6 class="section-title">Results for {{ inputCountry }}</h6>
            <ul class="list-group mb-3">
              <li v-for="rec in inputCountryRecommendations" :key="rec.country" class="list-group-item">
                {{ rec.travel_style }}
              </li>
            </ul>
          </template>

          <!-- 그 외의 추천 결과 -->
          <template v-if="otherRecommendations.length">
            <!-- Backpacker 리스트 -->
            <template v-if="backpackerRecommendations.length">
              <h6 class="section-title">Backpacker Recommendations</h6>
              <ul class="list-group mb-3">
                <li v-for="rec in backpackerRecommendations" :key="rec.country" class="list-group-item country-item">
                  <img :src="getImageUrl(rec.image)" class="country-img rounded-circle shadow-sm" alt="Backpacker Country">
                  <span class="country-name d-block mt-2">{{ rec.country }}</span>
                </li>
              </ul>
            </template>
            
            <!-- Mid-range 리스트 -->
            <template v-if="midRangeRecommendations.length">
              <h6 class="section-title">Mid-range Recommendations</h6>
              <ul class="list-group mb-3">
                <li v-for="rec in midRangeRecommendations" :key="rec.country" class="list-group-item country-item">
                  <img :src="getImageUrl(rec.image)" class="country-img rounded-circle shadow-sm" alt="Mid-range Country">
                  <span class="country-name d-block mt-2">{{ rec.country }}</span>
                </li>
              </ul>
            </template>
            
            <!-- Luxury 리스트 -->
            <template v-if="luxuryRecommendations.length">
              <h6 class="section-title">Luxury Recommendations</h6>
              <ul class="list-group mb-3">
                <li v-for="rec in luxuryRecommendations" :key="rec.country" class="list-group-item country-item">
                  <img :src="getImageUrl(rec.image)" class="country-img rounded-circle shadow-sm" alt="Luxury Country">
                  <span class="country-name d-block mt-2">{{ rec.country }}</span>
                </li>
              </ul>
            </template>
          </template>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="$emit('close')">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, computed } from 'vue';
import { useCounterStore } from '@/stores/counter';

// 부모 컴포넌트에서 전달된 props 정의
const props = defineProps({
  recommendations: Array, // 추천 결과 배열
  inputCountry: String // 입력된 Desired Country
});

const store = useCounterStore();

// 입력된 Desired Country에 대한 추천 결과 필터링
const inputCountryRecommendations = computed(() => 
  props.recommendations.filter(rec => rec.country === props.inputCountry)
);

// 그 외의 추천 결과 필터링
const otherRecommendations = computed(() => 
  props.recommendations.filter(rec => rec.country !== props.inputCountry)
);

// Backpacker 추천 결과 필터링
const backpackerRecommendations = computed(() => 
  otherRecommendations.value.filter(rec => rec.travel_style === 'Backpacker')
);

// Mid-range 추천 결과 필터링
const midRangeRecommendations = computed(() => 
  otherRecommendations.value.filter(rec => rec.travel_style === 'Mid-range')
);

// Luxury 추천 결과 필터링
const luxuryRecommendations = computed(() => 
  otherRecommendations.value.filter(rec => rec.travel_style === 'Luxury')
);

const getImageUrl = (imagePath) => {
  return store.getImageUrl(imagePath);
};
</script>

<style scoped>
.modal-content {
  background-color: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.modal-header {
  border-bottom: 1px solid #e9ecef;
  padding: 1rem 1.5rem;
}

.modal-title {
  font-size: 1.5rem;
  font-weight: bold;
}

.modal-body {
  padding: 1.5rem;
}

.modal-footer {
  border-top: 1px solid #e9ecef;
  padding: 1rem 1.5rem;
}

.section-title {
  font-size: 1.25rem;
  /* font-weight: bold; */
  margin-bottom: 1rem;
}

.list-group-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 15px;
  border: 1px solid #e9ecef;
  border-radius: 0.5rem;
  transition: background-color 0.3s ease-in-out;
}

.list-group-item:hover {
  background-color: #f8f9fa;
}

.country-img {
  width: 50px;
  height: 50px;
  object-fit: cover;
  border-radius: 50%;
  transition: transform 0.2s ease-in-out;
}

.country-img:hover {
  transform: scale(1.1);
}

.country-name {
  font-size: 1rem;
  font-weight: 500;
}

.btn-close {
  background-color: transparent;
  border: none;
  cursor: pointer;
  padding: 0;
  margin: 0;
}

.btn-secondary {
  font-size: 1rem;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  border: none;
  background-color: #6c757d;
  color: white;
  transition: background-color 0.3s ease-in-out;
}

.btn-secondary:hover {
  background-color: #5a6268;
}
</style>
