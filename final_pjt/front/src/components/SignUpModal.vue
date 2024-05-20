<template>
  <div v-if="isVisible" class="custom-modal-overlay" @click="closeModal">
    <div class="custom-modal" @click.stop>
      <h2>Sign Up</h2>
      <form @submit.prevent="signUp">
        <div class="mb-3">
          <label for="username" class="form-label">Username:</label>
          <input v-model="username" id="username" type="text" class="form-control" required />
        </div>
        <!-- <div class="mb-3">
          <label for="email" class="form-label">Email:</label>
          <input v-model="email" id="email" type="email" class="form-control" required />
        </div> -->
        <div class="mb-3">
          <label for="password" class="form-label">Password:</label>
          <input v-model="password" id="password" type="password" class="form-control" required />
        </div>
        <!-- 추가된 필드 -->
        <div class="mb-3">
          <label for="name" class="form-label">Name:</label>
          <input v-model="name" id="name" type="text" class="form-control" required />
        </div>
        <div class="mb-3">
          <label for="gender" class="form-label">Gender:</label>
          <select v-model="gender" id="gender" class="form-select" required>
            <option value="">Select gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <!-- <option value="other">Other</option> -->
          </select>
        </div>
        <div class="mb-3">
          <label for="age" class="form-label">Age:</label>
          <input v-model.number="age" id="age" type="number" class="form-control" required />
        </div>
        <!-- 추가된 필드 -->
        <button type="submit" class="btn btn-primary">Sign Up</button>
      </form>
      <button @click="closeModal" class="btn btn-secondary mt-2">Close</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

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
      // email: '',
      password: '',
      // 추가된 데이터 필드
      name: '',
      gender: '',
      age: null
    };
  },
  methods: {
    closeModal() {
      this.$emit('close');
    },
    async signUp() {
      try {
        const response = await axios.post('http://your-django-server/api/signup/', {
          username: this.username,
          // email: this.email,
          password: this.password,
          // 추가된 데이터 필드
          name: this.name,
          gender: this.gender,
          age: this.age
        });
        console.log('Signed up:', response.data);
        this.closeModal();
      } catch (error) {
        console.error('Sign up failed:', error);
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
  z-index: 1050;
}

.custom-modal {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 300px;
  max-width: 100%;
  z-index: 1060;
}
</style>
