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
            <h6>Results for {{ inputCountry }}</h6>
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
              <h6>Backpacker Recommendations</h6>
              <ul class="list-group mb-3">
                <li v-for="rec in backpackerRecommendations" :key="rec.country" class="list-group-item">
                  {{ rec.country }}
                </li>
              </ul>
            </template>
            
            <!-- Mid-range 리스트 -->
            <template v-if="midRangeRecommendations.length">
              <h6>Mid-range Recommendations</h6>
              <ul class="list-group mb-3">
                <li v-for="rec in midRangeRecommendations" :key="rec.country" class="list-group-item">
                  {{ rec.country }}
                </li>
              </ul>
            </template>
            
            <!-- Luxury 리스트 -->
            <template v-if="luxuryRecommendations.length">
              <h6>Luxury Recommendations</h6>
              <ul class="list-group mb-3">
                <li v-for="rec in luxuryRecommendations" :key="rec.country" class="list-group-item">
                  {{ rec.country }}
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

// 부모 컴포넌트에서 전달된 props 정의
const props = defineProps({
  recommendations: Array, // 추천 결과 배열
  inputCountry: String // 입력된 Desired Country
});

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
</script>

<style scoped>
/* 스타일은 그대로 유지 */
</style>