<template>
  <div v-if="isVisible" class="custom-modal-overlay" @click="closeModal">
    <div class="custom-modal" @click.stop>
      <h2>Sign Up</h2>
      <form @submit.prevent="signUp">
        <div class="mb-3">
          <label for="username" class="form-label">Username:</label>
          <input v-model="username" id="username" type="text" class="form-control" required />
        </div>
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
          </select>
        </div>
        <div class="mb-3">
          <label for="age" class="form-label">Age:</label>
          <input v-model.number="age" id="age" type="number" class="form-control" required />
        </div>
        <button type="submit" class="btn btn-primary">Sign Up</button>
      </form>
      <button @click="closeModal" class="btn btn-secondary mt-2">Close</button>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue'
import { useCounterStore } from '@/stores/counter' // 가정: 회원가입 상를 다루는 store

const props = defineProps({
  isVisible: Boolean
});

const { emit } = defineEmits(['close']);

const username = ref(null)
const password = ref(null)
const name = ref(null)
const gender = ref(null)
const age = ref(null)

const store = useCounterStore()

const closeModal = () => {
  emit('close')
}

const signUp = function () {
  const payload = {
    username: username.value,
    password: password.value,
    name: name.value,
    gender: gender.value,
    age: age.value,
  }
  store.signUp(payload)
}

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
