<template>
  <div class="wrap" style="margin-top: 2%;">
    <div class="detail-content">
      <img :src="imgUrl(data.graph)" alt="" class="resized-image" @click="showModal = true">
      <div class="info-container">
        <div class="exchange-rate">
          <p class="code">{{ props.data.code }}</p>
          <p class="rate">{{ props.data.rate }}</p>
        </div>
        <div class="price-info">
          <div class="item">
            <img src="/burger.png" alt="Burger" class="icon">
            <p>{{ burger }}원</p>
          </div>
          <div class="item">
            <img src="/coffee.png" alt="Coffee" class="icon">
            <p>{{ coffee }}원</p>
          </div>
        </div>
      </div>
    </div>
    <div>
      <DetailComment />
    </div>
    <DetailGraphModal v-if="showModal" :imgUrl="imgUrl(data.graph)" @close="showModal = false" />
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue';
import { useCounterStore } from '@/stores/counter';
import DetailComment from '@/components/DetailView/DetailComment.vue';
import DetailGraphModal from '@/components/DetailView/DetailGraphModal.vue';

const store = useCounterStore();
const imgUrl = store.getImageUrl;

const props = defineProps({
  data: Object,
});

const showModal = ref(false);

const burger = (Math.round(props.data.burger * props.data.rate / 10)) * 10;
const coffee = (Math.round(props.data.coffee * props.data.rate / 10)) * 10;
</script>

<style scoped>
.wrap {
  display: flex;
  flex-direction: column;
  margin-top: 2%;
}

.detail-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px; /* 간격 추가 */
}

.resized-image {
  width: 70%;
  height: auto;
  cursor: pointer;
  border-radius: 8px;
  transition: transform 0.3s ease-in-out;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 추가 */
}

.resized-image:hover {
  transform: scale(1.05);
}

.info-container {
  display: flex;
  flex-direction: column;
  gap: 20px; /* 간격 추가 */
  align-items: flex-end;
  margin-right: 10%;
}

.exchange-rate {
  background-color: #f8f9fa; /* 더 부드러운 배경색 */
  padding: 10px 20px; /* 패딩 조정 */
  border-radius: 8px;
  text-align: right;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 추가 */
}

.code {
  font-size: 1rem;
  margin: 0;
  color: #333; /* 색상 조정 */
}

.rate {
  font-size: 1.5rem;
  margin: 0;
  color: #333; /* 색상 조정 */
}

.price-info {
  display: flex;
  flex-direction: column;
  gap: 15px; /* 간격 추가 */
}

.item {
  display: flex;
  align-items: center;
  gap: 10px;
  background-color: #f8f9fa; /* 더 부드러운 배경색 */
  padding: 10px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 추가 */
}

.icon {
  width: 50px;
  height: auto;
  border-radius: 50%;
  transition: transform 0.3s ease-in-out;
}

.icon:hover {
  transform: scale(1.1);
}

.item p {
  margin: 0;
  font-size: 1rem;
  color: #333; /* 색상 조정 */
}
</style>
