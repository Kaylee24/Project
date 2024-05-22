import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)

  const pictures = ref([])
  const comparisonPageDatas = ref([])
  const detailContryData = ref([])

  // 이미지 URL 생성
  const getImageUrl = (imagePath) => {
    return `http://127.0.0.1:8000${imagePath}`
  }

  // 로그인 상태 확인
  const isLogin = computed(() => {
    return token.value !== null;
  })

  const router = useRouter()

  // 메인 국가 사진 가져오기
  const getMainCountryPictures = () => {
    axios({
      method: 'get',
      url: `${API_URL}/countries/main_country_picture/`,
    })
      .then(response => {
        pictures.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  // 비교 페이지 데이터 가져오기
  const comparisonPage = () => {
    axios({
      method: 'get',
      url: `${API_URL}/countries/comparison_page/`,
    })
      .then(response => {
        comparisonPageDatas.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  // 여행 추천 데이터 가져오기
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

  // detail의 나라 정보들
  const detailCountry = (countryId) => {
    axios({
      method: 'get',
      url: `${API_URL}/countries/detail_page/${countryId}`,
    })
      .then(response => {
        detailContryData.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  // 댓글 가져오기
  const fetchComments = (countryId) => {
    axios({
      method: 'get',
      url: `${API_URL}/countries/detail_page/${countryId}`,
    })
      .then(response => {
        detailContryData.value.comment_set = response.data.comment_set
      })
      .catch(error => {
        console.log(error)
      })
  }

  // 댓글 추가하기
  const addComment = (payload) => {
    axios({
      method: 'post',
      url: `${API_URL}/countries/detail_page/${payload.countryId}`,
      data: { content: payload.content },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(response => {
        console.log(response)
        detailContryData.value.comment_set.push(response.data)
      })
      .catch(error => {
        console.log(error)
      })
  }

  // 회원가입
  const signUp = function (payload) {
    const { username, password1, password2, name, gender, age } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, name, gender, age
      }
    })
     .then((response) => {
       console.log('회원가입 성공!')
       console.log(payload)
       const password = password1
       logIn({ username, password })
     })
     .catch((error) => {
        console.log('틀렸음 다시해')
        console.log(error)
     })
  }

  // 로그인
  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        token.value = response.data.key
      })
      .catch((error) => {
        console.log(error)
      })
  }

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

  const profilePage = async (token) => {
    try {
      const response = await axios.get(`${API_URL}/countries/profile_page/${token}`, {
        headers: {
          Authorization: `Token ${token}`,
        },
      });
      return response.data;
    } catch (error) {
      console.error(error);
      return null;
    }
  };


  return { 
    API_URL, 
    token, 
    isLogin, 
    pictures, 
    comparisonPageDatas,
    detailContryData,
    signUp, 
    logIn, 
    getMainCountryPictures, 
    comparisonPage, 
    getImageUrl,
    getTravelRecommendations,
    searchCountry,
    detailCountry,
    fetchComments, // 댓글 가져오기 메서드 추가
    addComment,    // 댓글 추가하기 메서드 추가
    profilePage,
  }
}, { persist: true })
