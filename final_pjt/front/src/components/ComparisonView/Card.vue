<template>
  <div class="card" @mouseover="isHover = true" @mouseleave="isHover = false">
    <div class="img-box">
      <img
        :src="imgUrl(data.image1)"
        alt=""
        class="resized-image"
        @click="goToDetailView(data.id)"
      >
      <h5 class="name">{{ data.name }}</h5>
    </div>
    <div class="content-box">
      <img :src="imgUrl(data.graph)" alt="graph 이미지입니다." class="graph-image">
      <div class="info-container">
        <div class="info">
          <p class="code">{{ data.code }}</p>
          <p class="rate">환율: {{ data.rate }}</p>
        </div>
        <div class="price-info">
          <div class="image-container">
            <img src="/burger.png" alt="햄버거 가격" class="hamburger-coffee-image">
            <p class="price">{{ burger }}원</p>
          </div>
          <div class="image-container">
            <img src="/coffee.png" alt="커피 가격" class="hamburger-coffee-image">
            <p class="price">{{ coffee }}원</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router';

const store = useCounterStore()
const router = useRouter()

const imgUrl = store.getImageUrl

const props = defineProps({
  data: Object,
})

const burger = (Math.round(props.data.burger * props.data.rate / 10)) * 10
const coffee = (Math.round(props.data.coffee * props.data.rate / 10)) * 10

const goToDetailView = (countryId) => {
  router.push({ name: 'DetailView', params: { countryId } })
}

let isHover = false;
</script>

<style scoped>
.card {
  background: #ffffff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.img-box {
  margin-bottom: 20px;
  overflow: hidden;
  border-radius: 10px;
  position: relative;
}

.resized-image {
  width: 100%;
  height: 280px;
  object-fit: cover;
  object-position: center;
  border-radius: 10px;
  transition: transform 0.3s ease-in-out;
}

.resized-image:hover {
  transform: scale(1.1);
}

.name {
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.6);
  color: white;
  padding: 5px 10px;
  border-radius: 5px;
  font-weight: bold;
}

.content-box {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-top: 10px;
}

.graph-image {
  width: 70%;
  height: auto;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.info-container {
  width: 30%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding-left: 40px;
}

.info {
  margin-bottom: 15px;
}

.code {
  font-size: 1.2rem;
  font-weight: bold;
}

.rate {
  font-size: 1rem;
  color: #555;
}

.price-info {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.image-container {
  display: flex;
  align-items: center;
}

.hamburger-coffee-image {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 8px;
}

.price {
  font-size: 1rem;
  font-weight: bold;
  color: #333;
}
</style>
