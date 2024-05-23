// stores/counter.js
import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useCounterStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000';
  const token = ref(null);
  const user = ref('');
  const pictures = ref([]);
  const comparisonPageDatas = ref([]);
  const detailCountryData = ref({});
  const profileData = ref([]);

  const getImageUrl = (imagePath) => {
    return `http://127.0.0.1:8000${imagePath}`;
  };

  const isLogin = computed(() => token.value !== null);

  const getMainCountryPictures = () => {
    axios.get(`${API_URL}/countries/main_country_picture/`)
      .then(response => {
        pictures.value = response.data;
      })
      .catch(error => {
        console.log(error);
      });
  };

  const comparisonPage = () => {
    axios.get(`${API_URL}/countries/comparison_page/`)
      .then(response => {
        comparisonPageDatas.value = response.data;
      })
      .catch(error => {
        console.log(error);
      });
  };

  const getTravelRecommendations = async ({ country, budget, days }) => {
    try {
      const response = await axios.post(`${API_URL}/countries/recommendations/`, {
        country,
        budget,
        days,
      });
      return response.data.recommendations;
    } catch (error) {
      console.error(error);
      return [];
    }
  };

  const detailCountry = async (countryId) => {
    try {
      const response = await axios.get(`${API_URL}/countries/detail_page/${countryId}`);
      detailCountryData.value = response.data;
    } catch (error) {
      console.error(error);
    }
  };

  const fetchComments = async (countryId) => {
    try {
      const response = await axios.get(`${API_URL}/countries/detail_page/${countryId}`);
      detailCountryData.value.comment_set = response.data.comment_set;
    } catch (error) {
      console.error(error);
    }
  };

  const addComment = async (payload) => {
    try {
      await axios.post(`${API_URL}/countries/detail_page/${payload.countryId}`, { content: payload.content }, {
        headers: {
          Authorization: `Token ${token.value}`,
        },
      });
      fetchComments(payload.countryId);
    } catch (error) {
      console.error(error);
    }
  };

  const deleteComment = async (commentId) => {
    try {
      await axios.delete(`${API_URL}/countries/detail_page/delete/${commentId}`, {
        headers: {
          Authorization: `Token ${token.value}`,
        },
      });
      fetchComments(detailCountryData.value.id);
    } catch (error) {
      console.error(error);
    }
  };

  const signUp = async (payload) => {
    try {
      const { username, password1, password2, name, gender, age } = payload;
      await axios.post(`${API_URL}/accounts/signup/`, { username, password1, password2, name, gender, age });
      logIn({ username, password: password1 });
    } catch (error) {
      console.error(error);
    }
  };

  const logIn = async (payload) => {
    try {
      const { username, password } = payload;
      const response = await axios.post(`${API_URL}/accounts/login/`, { username, password });
      token.value = response.data.key;
      user.value = username;
      await profilePage(username);
    } catch (error) {
      console.error(error);
    }
  };

  const searchCountry = async (query) => {
    try {
      const response = await axios.get(`${API_URL}/countries/search_country/`, {
        params: { q: query },
      });
      return response.data;
    } catch (error) {
      console.error(error);
      return null;
    }
  };

  const profilePage = async (username) => {
    try {
      const response = await axios.get(`${API_URL}/countries/profile_page/${username}`);
      profileData.value = response.data;
    } catch (error) {
      console.error(error);
    }
  };

  const updateVisitedCountries = async (countryIds) => {
    try {
      await axios.post(`${API_URL}/countries/update_visited_countries/`, { country_ids: countryIds }, {
        headers: {
          Authorization: `Token ${token.value}`,
        },
      });
      await profilePage(user.value); // Update profile data after changing visited countries
    } catch (error) {
      console.error(error);
    }
  };

  const updateInterestedCountries = async (countryIds) => {
    try {
      await axios.post(`${API_URL}/countries/update_interested_countries/`, { country_ids: countryIds }, {
        headers: {
          Authorization: `Token ${token.value}`,
        },
      });
      await profilePage(user.value); // Update profile data after changing interested countries
    } catch (error) {
      console.error(error);
    }
  };

  return {
    API_URL,
    user,
    token,
    isLogin,
    pictures,
    comparisonPageDatas,
    detailCountryData,
    profileData,
    signUp,
    logIn,
    getMainCountryPictures,
    comparisonPage,
    getImageUrl,
    getTravelRecommendations,
    searchCountry,
    detailCountry,
    fetchComments,
    addComment,
    profilePage,
    updateVisitedCountries,
    updateInterestedCountries,
    deleteComment,
  };
}, { persist: true });
