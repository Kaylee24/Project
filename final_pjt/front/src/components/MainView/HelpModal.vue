<template>
  <div class="modal-overlay" @click.self="closeModal">
    <div class="modal-content">
      <h1 style="margin-top: 10px; margin-bottom: 30px;">유로존 안내</h1>
      <p>반갑습니다!</p>
      <p>Easy Travel은 환율을 기반으로 여행지 선택에 도움을 드리고 있습니다.</p>
      <p>따라서 다음의 유로존 국가들은 한 페이지에서 정보 확인이 가능합니다.</p>

      <img src="/Eurozone.png" alt="Eurozone.png" width="auto" style="margin-bottom: 30px;">


      <p style="margin-bottom: 8px;">🛫 여행 계획은 쉽고 간편하게! 🛫</p>
      <img src="/EasyTravelLogo-removebg.png" alt="Easy Travel Logo" width="30%" height="auto" style="align-self: center;">


      <button class="btn btn-outline-secondary" @click="closeModal">Close</button>
    </div>
  </div>
</template>

<script setup>
import { defineEmits } from 'vue';
const emit = defineEmits(['close']);
const closeModal = () => {
  emit('close');
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  max-width: 500px;
  width: 90%;
  text-align: center;
}

button {
  margin-top: 10px;
}
</style>
