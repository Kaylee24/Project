<template>
  <div class="wrap">
    <div class="detail-content">
      <img :src="imgUrl(data.graph)" alt="" class="resized-image">
      <div>
        <p>{{ burger }}</p>
        <p>{{ coffee }}</p>
      </div>
    </div>
    <div>
      <DetailComment />
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue'
import DetailComment from '@/components/DetailView/DetailComment.vue'

const store = useCounterStore()

const imgUrl = store.getImageUrl

const props = defineProps({
  data: Object,
})

const burger = (Math.round(props.data.burger * props.data.rate / 10)) * 10
const coffee = (Math.round(props.data.coffee * props.data.rate / 10)) * 10

</script>

<style scoped>

.detail-content {
  display: flex;
  align-items: center; /* 이미지를 세로로 가운데 정렬합니다. */
}

.resized-image {
  width: 80%; /* 최대 너비를 50%로 설정합니다. */
  height: auto; /* 높이는 비율에 맞게 자동 조절됩니다. */
}

.wrap {
  display: flex;
  flex-direction: column;
}
</style>
