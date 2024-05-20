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
  methods: {
    closeModal() {
      this.$emit('close');
    },
    login() {
      // 로그인 처리 로직
      console.log('Logging in with', this.username, this.password);
      this.closeModal();
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
