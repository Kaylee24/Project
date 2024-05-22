<template>
  <div class="modal fade show" tabindex="-1" style="display: block;" aria-labelledby="profileModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="profileModalLabel">{{ profileData.name }}님</h5>
          <button type="button" class="btn-close" aria-label="Close" @click="closeModal"></button>
        </div>
        <div class="modal-body">
          <div class="text-center">
            <img v-if="profileData.image" :src="getImageUrl(profileData.image)" class="rounded-circle" alt="Profile Image" width="100" height="100">
            <h6>{{ profileData.age }}세</h6>
          </div>
          <div class="mt-3">
            <h6>방문한 나라</h6>
            <ul class="list-inline">
              <li class="list-inline-item" v-for="country in profileData.visited" :key="country.name">
                <img :src="getImageUrl(country.image1)" class="rounded" alt="Visited Country" width="50" height="50">
                <span>{{ country.name }}</span>
              </li>
            </ul>
          </div>
          <div class="mt-3">
            <h6>관심 있는 나라</h6>
            <ul class="list-inline">
              <li class="list-inline-item" v-for="country in profileData.interested" :key="country.name">
                <img :src="getImageUrl(country.image1)" class="rounded" alt="Interested Country" width="50" height="50">
                <span>{{ country.name }}</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';

const props = defineProps({
  isVisible: Boolean,
});

const emit = defineEmits(['close']);
const store = useCounterStore();
const profileData = store.profileData

const closeModal = () => {
  emit('close');
};

const getImageUrl = (imagePath) => {
  return store.getImageUrl(imagePath);
};

onMounted(() => {
  store.profilePage(store.user)
  console.log(profileData)
});
</script>

<style scoped>
.modal-content {
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 0.3rem;
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
}
</style>
