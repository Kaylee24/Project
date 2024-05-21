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
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const router = useRouter()

  // 메인 국가 사진 가져오기
  const getMainCountryPictures = () => {
    axios({
      method: 'get',
      url: `${API_URL}/countries/main_country_picture/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
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

  // 회원가입
  const signUp = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    const { username, password1, password2, name, gender, age } = payload

    // 2. axios로 django에 요청을 보냄
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
    // 1. 사용자 입력 데이터를 받아
    const { username, password } = payload
    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        // console.log('로그인 성공!')
        // console.log(response)
        // console.log(response.data.key)
        // 3. 로그인 성공 후 응답 받은 토큰을 저장
        token.value = response.data.key
      })
      .catch((error) => {
        console.log(error)
      })
  }

  return { 
    API_URL, 
    token, 
    isLogin, 
    pictures, 
    comparisonPageDatas,
    signUp, 
    logIn, 
    getMainCountryPictures, 
    comparisonPage, 
    getImageUrl,
    getTravelRecommendations, // 추가된 메서드
  }
}, { persist: true })
