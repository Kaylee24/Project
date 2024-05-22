<template>
  <div class="detail-view">
    <div class="detail-content">
      <DetailGallery :data="data" />
      <DetailGraph :data="data" />
    </div>
    <div class="button-container">
      <button class="styled-button" @click="selectVisited(data.id)">Visited</button>
      <button class="styled-button" @click="selectInterested(data.id)">Interested</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, defineProps } from 'vue'
import { useCounterStore } from '@/stores/counter'
import DetailGraph from '@/components/DetailView/DetailGraph.vue'
import DetailGallery from '@/components/DetailView/DetailGallery.vue'

const store = useCounterStore()
const countryId = ref(null)
const props = defineProps(['countryId']) // props 정의
const data = store.detailContryData

const selectVisited = (countryId) => {
  if (store.isLogin) {
    store.updateVisitedCountries([countryId])
  } else {
    alert('로그인이 필요합니다.')
  }
}

const selectInterested = (countryId) => {
  if (store.isLogin) {
    store.updateInterestedCountries([countryId])
  } else {
    alert('로그인이 필요합니다.')
  }
}

onMounted(() => {
  countryId.value = props.countryId // props로 전달받은 countryId 사용
  store.detailCountry(countryId.value) // 국가 데이터 요청
})
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
  gap: 10px; /* 버튼 사이의 간격 */
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
