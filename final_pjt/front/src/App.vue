<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <RouterLink class="navbar-brand" :to="{ name: 'MainView' }">Easy Travel</RouterLink>

        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <RouterLink class="nav-link active" :to="{ name: 'ComparisonPageView' }">Easy World Tour</RouterLink>
            </li>
          </ul>
        </div>




        <div class="ms-auto">
          <template v-if="!isLoggedIn">
            <button class="btn btn-outline-primary me-2" @click="showLoginModal = true">로그인</button>
            <button class="btn btn-outline-secondary" @click="showSignUpModal = true">회원가입</button>
          </template>
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
