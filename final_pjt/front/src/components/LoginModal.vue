<template>
  <div v-if="isVisible" class="custom-modal-overlay" @click="closeModal">
    <div class="custom-modal" @click.stop>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <div class="mb-3">
          <label for="username" class="form-label">Username:</label>
          <input v-model="username" id="username" type="text" class="form-control" required />
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password:</label>
          <input v-model="password" id="password" type="password" class="form-control" required />
        </div>
        <button type="submit" class="btn btn-primary">Login</button>
      </form>
      <button @click="closeModal" class="btn btn-secondary mt-2">Close</button>
    </div>
  </div>
</template>

<script>
import { useCounterStore } from '@/stores/counter';

export default {
  props: {
    isVisible: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      username: '',
      password: ''
    };
  },
  setup() {
    const store = useCounterStore()
    return { store }
  },
  methods: {
    closeModal() {
      this.$emit('close');
    },
    async login() {
      try {
        await this.store.logIn({
          username: this.username,
          password: this.password
        });
        console.log('Logging in with', this.username, this.password);
        console.log('this', this)
        this.closeModal(); // 로그인 성공 시 모달 닫기
      } catch (error) {
        console.error('Login failed:', error);
        // 로그인 실패 시 적절한 오류 처리
      }
    }
  }
};
</script>

<style scoped>
.custom-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1050; /* Bootstrap 모달 z-index와 맞추기 */
}

.custom-modal {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 300px;
  max-width: 100%;
  z-index: 1060; /* Bootstrap 모달 z-index와 맞추기 */
}
</style>
