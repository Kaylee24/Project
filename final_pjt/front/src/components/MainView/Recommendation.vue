<template>
  <div>
    <b-form @submit.prevent="calculateRecommendations">
      <b-form-group label="Country:" label-for="country-input">
        <b-form-input id="country-input" v-model="desiredCountry" required></b-form-input>
      </b-form-group>
      <b-form-group label="Budget (USD):" label-for="budget-input">
        <b-form-input id="budget-input" type="number" v-model.number="budget" required></b-form-input>
      </b-form-group>
      <b-form-group label="Days:" label-for="days-input">
        <b-form-input id="days-input" type="number" v-model.number="days" required></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Calculate Recommendations</b-button>
    </b-form>

    <!-- 모달 창 정의 -->
    <b-modal v-model="showModal" title="Travel Recommendations">
      <div v-for="rec in recommendations" :key="rec.country">
        <h5>{{ rec.country }}</h5>
        <p>Travel Style: {{ rec.travel_style }}</p>
        <p>Cost Index: {{ rec.cost_index.toFixed(2) }}</p>
      </div>
    </b-modal>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();
const { countries } = store;

const desiredCountry = ref('');
const budget = ref(0);
const days = ref(0);
const recommendations = ref([]);
const showModal = ref(false);

function calculateRecommendations() {
  const selectedCountry = countries.value.find(c => c.name === desiredCountry.value);
  if (!selectedCountry) {
    alert('Country not found');
    return;
  }

  const areaCountries = countries.value.filter(c => c.area === selectedCountry.area);
  recommendations.value = areaCountries.map(c => {
    const totalCostPerDay = (c.burger + c.coffee) * c.rate;
    const dailyBudget = budget.value / days.value;
    const dailyCostIndex = dailyBudget / totalCostPerDay;

    let style = 'Not recommended';
    if (dailyCostIndex >= 3 && dailyCostIndex < 6) {
      style = 'Backpacker';
    } else if (dailyCostIndex >= 6 && dailyCostIndex < 10) {
      style = 'Mid-range';
    } else if (dailyCostIndex >= 10) {
      style = 'Luxury';
    }

    return { country: c.name, travel_style: style, cost_index: dailyCostIndex };
  });

  showModal.value = true;
}
</script>
