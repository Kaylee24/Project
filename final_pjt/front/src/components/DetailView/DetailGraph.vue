<template>
  <div class="wrap">
    <div class="detail-content">
      <img :src="imgUrl(data.graph)" alt="" class="resized-image" @click="showModal = true">
      <div class="icon-container">
        <img src="/burger.png" alt="Burger" class="icon">
        <p>{{ burger }}원</p>
        <img src="/coffee.png" alt="Coffee" class="icon">
        <p>{{ coffee }}원</p>
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

console.log('DetailGraph의 props', props);
</script>

<style scoped>
.detail-content {
  display: flex;
  align-items: center; /* 이미지를 세로로 가운데 정렬합니다. */
}

.resized-image {
  width: 80%; /* 최대 너비를 80%로 설정합니다. */
  height: auto; /* 높이는 비율에 맞게 자동 조절됩니다. */
  cursor: pointer; /* 클릭할 수 있음을 나타내는 커서 */
}

.wrap {
  display: flex;
  flex-direction: column;
}

.icon-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.icon {
  width: 50px; /* 이미지 너비를 50px로 설정 */
  height: auto; /* 높이는 비율에 맞게 자동 조절 */
}
</style>
