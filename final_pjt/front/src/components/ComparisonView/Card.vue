<template>
  <div class="card">
    <img
    :src="imgUrl(data.image1)" alt="" class="resized-image"
    @click="goToDetailView(data.id)"
    >
    <div class="image-info">
      <div class="info">
        <h5>{{ data.name }}</h5>
        <p>{{ data.code }}</p>
        <p>{{ data.rate }}</p>
      </div>
      <div class="right-info"> <!-- 오른쪽에 위치할 div -->
        <img :src="imgUrl(data.image1)" alt="" class="hamburger-coffee-image">
        <p>{{ burger }}\</p>
        <img :src="imgUrl(data.image1)" alt="" class="hamburger-coffee-image">
        <p>{{ coffee }}\</p>
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

</script>

<style scoped>
.card {
  background: #e6feff;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.resized-image {
  width: 100%;
  height: auto;
}

.image-info {
  display: flex; /* 내부 요소를 가로로 배치 */
  margin-top: 20px;
}

.info {
  flex: 1; /* 공간을 나눠 사용하도록 설정 */
  padding: 0 16px; /* 좌우 패딩 추가 */
}

.right-info {
  flex: 1; /* 공간을 나눠 사용하도록 설정 */
  justify-content: flex-end; /* 내부 요소를 오른쪽으로 정렬 */
}

.hamburger-coffee-image {
  width: 20%;
  height: 20%;
}
</style>
