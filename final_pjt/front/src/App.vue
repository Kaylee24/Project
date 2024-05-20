<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'MainView' }">MainView</RouterLink> |
      <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink> |
      <RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink>
    </nav>
  </header>
  <RouterView />

  <div id="app">
    <button @click="showModal = true">Login</button>
    <LoginModal v-if="showModal" :isVisible="showModal" @close="showModal = false" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { RouterView, RouterLink } from 'vue-router';
import LoginModal from './components/LoginModal.vue';

const showModal = ref(false);

const closeModal = () => {
  showModal.value = false;
};
</script>

<style scoped>
</style>