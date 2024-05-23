<template>
  <div class="card-container">
    <Card
      v-for="data in store.comparisonPageDatas"
      :key="data.id"
      :data="data"
      class="card"
      @toggleSelect="toggleSelect"
    />
    <div class="button-container">
      <button class="btn btn-primary" @click="updateVisitedCountries">Update Visited Countries</button>
      <button class="btn btn-secondary" @click="updateInterestedCountries">Update Interested Countries</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import Card from '@/components/ComparisonView/Card.vue'

const store = useCounterStore()
const selectedCountries = ref([])

const toggleSelect = (countryId) => {
  const index = selectedCountries.value.indexOf(countryId)
  if (index > -1) {
    selectedCountries.value.splice(index, 1)
  } else {
    selectedCountries.value.push(countryId)
  }
  store.selectedCountries.value = selectedCountries.value
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
  gap: 20px;
}

.card {
  width: calc(33.33% - 20px);
  margin-bottom: 20px;
  transition: transform 0.3s ease-in-out;
}

.card:hover {
  transform: translateY(-5px);
}

.button-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  gap: 10px;
}

.btn {
  padding: 10px 20px;
  border-radius: 5px;
  transition: background-color 0.3s, color 0.3s;
}

.btn-primary {
  background-color: #007bff;
  color: white;
  border: none;
}

.btn-primary:hover {
  background-color: #0056b3;
  color: white;
}

.btn-secondary {
  background-color: #6c757d;
  color: white;
  border: none;
}

.btn-secondary:hover {
  background-color: #5a6268;
  color: white;
}

@media (max-width: 992px) {
  .card {
    width: calc(50% - 20px);
  }
}

@media (max-width: 576px) {
  .card {
    width: 100%;
  }
}
</style>
