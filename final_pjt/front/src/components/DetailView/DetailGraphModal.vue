<template>
  <div class="modal-overlay" @click="closeModal">
    <div class="modal-content" @click.stop>
      <button class="close-button" @click="closeModal">&times;</button>
      <!-- <div class="zoom-buttons">
        <button class="zoom-button" @click="changeZoom(1.25)">125%</button>
        <button class="zoom-button" @click="changeZoom(1.5)">150%</button>
        <button class="zoom-button" @click="changeZoom(1)">Reset</button>
      </div> -->
      <img :src="imgUrl" :style="{ transform: `scale(${zoom})`, transition: 'transform 0.3s ease' }" alt="Detailed Graph" />
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits, ref } from 'vue';

const props = defineProps({
  imgUrl: String
});

const emit = defineEmits(['close']);

const zoom = ref(1);

const closeModal = () => {
  emit('close');
};

const changeZoom = (scale) => {
  zoom.value = scale;
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  position: relative;
  max-width: 80%;
  max-height: 80%;
}

.modal-content img {
  width: 100%;
  height: auto;
  border-radius: 10px;
  transition: transform 0.3s ease;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: transparent;
  border: none;
  font-size: 2rem;
  color: black;
  cursor: pointer;
  font-family: 'Arial', sans-serif;
  z-index: 1010; /* 버튼이 항상 위에 표시되도록 z-index 설정 */
}

.zoom-buttons {
  position: absolute;
  top: 50px; /* 닫기 버튼 아래로 이동 */
  right: 10px; /* 창의 오른쪽에 위치 */
  display: flex;
  flex-direction: column; /* 수직 정렬 */
  gap: 10px;
  z-index: 1010; /* 버튼이 항상 위에 표시되도록 z-index 설정 */
}

.zoom-button {
  background-color: transparent; /* 배경색을 투명하게 설정 */
  color: #007BFF; /* 글자색을 파란색으로 설정 */
  border: 2px solid #007BFF; /* 테두리만 남기기 */
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
  font-family: 'Arial', sans-serif;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.zoom-button:hover {
  background-color: #007BFF; /* 호버 시 배경색을 파란색으로 설정 */
  color: white; /* 호버 시 글자색을 흰색으로 변경 */
}
</style>
