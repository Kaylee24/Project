<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <!-- <img src="/EasyTravelLogo-removebg.png" alt="Easy Travel Logo" height="60"> -->
        <RouterLink class="navbar-brand" :to="{ name: 'MainView' }">
          <img src="/EasyTravelLogo-removebg.png" alt="Easy Travel Logo" height="60" style="margin-left: 10px;">
        </RouterLink>

        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <RouterLink class="nav-link active" :to="{ name: 'ComparisonView' }">Easy World Tour</RouterLink>
            </li>
          </ul>
        </div>

        <div class="ms-auto">
          <template v-if=!store.token>
            <button class="btn btn-outline-primary me-2" @click="showLoginModal = true">로그인</button>
            <button class="btn btn-outline-secondary" @click="showSignUpModal = true">회원가입</button>
          </template>
          <template v-else>
            <button class="btn btn-outline-danger" @click="logoutbutton">로그아웃</button>
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
import { useCounterStore } from './stores/counter';

const store = useCounterStore()

const showLoginModal = ref(false); // 로그인 모달이 표시되는지 여부를 제어하는 변수
const showSignUpModal = ref(false); // 회원가입 모달이 표시되는지 여부를 제어하는 변수

const closeLoginModal = () => {
  showLoginModal.value = false;
  console.log(store.token)
};

const closeSignUpModal = () => {
  showSignUpModal.value = false;
};

// 사용자가 로그아웃할 때 호출되는 함수
const logoutbutton = () => {
  store.token = null
};

</script>

<style scoped>
</style>