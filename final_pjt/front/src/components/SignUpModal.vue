<template>
  <div v-if="isVisible" class="custom-modal-overlay" @click="closeModal">
    <div class="custom-modal" @click.stop>
      <h2>Sign Up</h2>
      <form @submit.prevent="signUp">
        <div class="mb-3">
          <label for="username" class="form-label">닉네임:</label>
          <input v-model="username" id="username" type="text" class="form-control" required />
        </div>
        <div class="mb-3">
          <label for="password1" class="form-label">비밀번호:</label>
          <input v-model="password1" id="password1" type="password" class="form-control" required />
        </div>
        <div class="mb-3">
          <label for="password2" class="form-label">비밀번호 확인:</label>
          <input v-model="password2" id="password2" type="password" class="form-control" required />
        </div>
        <!-- 추가된 필드 -->
        <div class="mb-3">
          <label for="name" class="form-label">이름:</label>
          <input v-model="name" id="name" type="text" class="form-control" required />
        </div>
        <div class="mb-3">
          <label for="gender" class="form-label">성별:</label>
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
        <!-- <div class="mb-3">
          <label for="email" class="form-label">이메일:</label>
          <input v-model="email" id="email" type="text" class="form-control" required />
        </div> -->
        <button type="submit" class="btn btn-primary">Sign Up</button>
      </form>
      <button @click="closeModal" class="btn btn-secondary mt-2">Close</button>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue'
import { useCounterStore } from '@/stores/counter' // 가정: 회원가입 상를 다루는 store

const props = defineProps({
  isVisible: Boolean
})

const emit = defineEmits(['close'])

const username = ref('')
const password1 = ref('')
const password2 = ref('')
const name = ref('')
const gender = ref('')
const age = ref(0)
// const email = ref('')

const store = useCounterStore()

const closeModal = () => {
  emit('close')
}

const signUp = async () => {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    name: name.value,
    gender: gender.value,
    age: age.value,
    // email: email.value,
  }

  try {
    await store.signUp(payload)
    closeModal() // 성공 시 모달 닫기
  } catch (error) {
    console.error('Sign up error:', error)
  }
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
