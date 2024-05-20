<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <RouterLink class="navbar-brand" :to="{ name: 'MainView' }">Easy Travel</RouterLink>
        <div class="ms-auto">
          <button class="btn btn-outline-primary me-2" @click="showLoginModal = true">로그인</button>
          <button class="btn btn-outline-secondary" @click="showSignUpModal = true">회원가입</button>
        </div>
      </div>
    </nav>
  </header>
  <RouterView />

  <div id="app">
    <!-- 조건부 렌더링을 통해 모달을 표시 -->
    <LoginModal v-if="showLoginModal" :isVisible="showLoginModal" @close="closeLoginModal" />
    <SignUpModal v-if="showSignUpModal" :isVisible="showSignUpModal" @close="closeSignUpModal" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { RouterView, RouterLink } from 'vue-router';
import LoginModal from './components/LoginModal.vue';
import SignUpModal from './components/SignUpModal.vue';

const showLoginModal = ref(false); // 로그인 모달이 표시되는지 여부를 제어하는 변수
const showSignUpModal = ref(false); // 회원가입 모달이 표시되는지 여부를 제어하는 변수

const closeLoginModal = () => {
  showLoginModal.value = false;
};

const closeSignUpModal = () => {
  showSignUpModal.value = false;
};
</script>

<style scoped>
</style>
