<template>
  <div class="card" @mouseover="isHover = true" @mouseleave="isHover = false">
    <div class="img-box">
      <img
        :src="imgUrl(data.image1)"
        alt=""
        class="resized-image"
        @click="goToDetailView(data.id)"
      >
    </div>
    <h5 class="name">{{ data.name }}</h5>
    <div class="image-info">
      <div class="info">
        <p>{{ data.code }}</p>
        <p>{{ data.rate }}</p>
      </div>
      <div class="right-info">
        <div class="image-container">
          <img :src="imgUrl(data.image1)" alt="" class="hamburger-coffee-image">
          <p>{{ burger }}</p>
        </div>
        <div class="image-container">
          <img :src="imgUrl(data.image1)" alt="" class="hamburger-coffee-image">
          <p>{{ coffee }}</p>
        </div>
      </div>
    </div>
    <img :src="imgUrl(data.graph)" alt="" class="resized-image">
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
  background: #f3f3f3;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
}

.card:hover {
  transform: scale(1.05);
}

.img-box {
  margin-bottom: 20px;
}

.resized-image {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.image-info {
  display: flex;
}

.info {
  flex: 1;
}

.name {
  text-align: center; /* h5 태그 가운데 정렬 */
}

.right-info {
  display: flex;
  align-items: center;
}

.image-container {
  display: flex;
  align-items: center;
  margin-left: 16px;
}

.hamburger-coffee-image {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 8px;
}
</style>
