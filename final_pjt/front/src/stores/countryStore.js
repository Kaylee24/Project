// stores/countryStore.js
import { defineStore } from 'pinia';
import axios from 'axios';

export const useCountryStore = defineStore('country', {
  state: () => ({
    countries: [],
  }),
  actions: {
    async fetchCountries() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/countries/country_list/');
        this.countries = response.data;
      } catch (error) {
        console.error('Failed to fetch countries:', error);
      }
    },
  },
});
