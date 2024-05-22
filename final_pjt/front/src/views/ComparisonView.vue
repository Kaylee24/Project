<template>
  <div class="card-container">
    <Card
      v-for="data in store.comparisonPageDatas"
      :key="data.id"
      :data="data"
      class="card"
      @toggleSelect="toggleSelect"
    />
    <button @click="updateVisitedCountries">Update Visited Countries</button>
    <button @click="updateInterestedCountries">Update Interested Countries</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import Card from '@/components/ComparisonView/Card.vue'

const store = useCounterStore()
const selectedCountries = ref([])

// const toggleSelect = (countryId) => {
//   const index = selectedCountries.value.indexOf(countryId)
//   if (index > -1) {
//     selectedCountries.value.splice(index, 1)
//   } else {
//     selectedCountries.value.push(countryId)
//   }
// }

const toggleSelect = (countryId) => {
  const index = selectedCountries.value.indexOf(countryId)
  if (index > -1) {
    selectedCountries.value.splice(index, 1)
  } else {
    selectedCountries.value.push(countryId)
  }
  store.selectedCountries.value = selectedCountries.value // 수정된 부분
}

const updateVisitedCountries = () => {
  if (store.isLogin) {
    store.updateVisitedCountries(selectedCountries.value)
  } else {
    alert('로그인이 필요합니다.')
  }
}

const updateInterestedCountries = () => {
  if (store.isLogin) {
    store.updateInterestedCountries(selectedCountries.value)
  } else {
    alert('로그인이 필요합니다.')
  }
}

onMounted(() => {
  store.comparisonPage()
})
</script>

<style scoped>
.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 20px; /* 카드 사이의 간격을 설정합니다. */
}

.card {
  width: calc(33.33% - 20px); /* 카드의 너비를 계산하고 카드 사이의 간격을 고려합니다. */
  margin-bottom: 20px; /* 아래 여백을 설정합니다. */
  transition: transform 0.3s ease-in-out; /* 마우스 호버 시 움직이는 효과를 추가합니다. */
}

.card:hover {
  transform: translateY(-5px); /* 마우스 호버 시 약간 위로 움직이도록 설정합니다. */
}

@media (max-width: 992px) {
  .card {
    width: calc(50% - 20px); /* 미디어 쿼리를 사용하여 반응형으로 설정합니다. */
  }
}

@media (max-width: 576px) {
  .card {
    width: 100%; /* 미디어 쿼리를 사용하여 반응형으로 설정합니다. */
  }
}
</style>
