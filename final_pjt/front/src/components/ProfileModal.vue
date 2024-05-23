<template>
  <div class="modal fade show" tabindex="-1" style="display: block;" aria-labelledby="profileModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="profileModalLabel">My Profile</h5>
          <button type="button" class="btn-close" aria-label="Close" @click="closeModal"></button>
        </div>
        <div class="modal-body">
          <div class="user-info-block p-3 mb-4">
            <div v-if="profileData.gender === 'female'" class="d-flex flex-column align-items-start">
              <h5>{{ profileData.name }}님</h5>
              <div class="d-flex align-items-center mt-1">
                <h5>🙋‍♀️</h5>
                <p class="ms-2">{{ profileData.age }}세</p>
              </div>
            </div>
            <div v-else class="d-flex flex-column align-items-start">
              <h5>{{ profileData.name }}님</h5>
              <div class="d-flex align-items-center mt-1">
                <h5>🙋‍♂️</h5>
                <p class="ms-2">{{ profileData.age }}세</p>
              </div>
            </div>
          </div>
          <div class="section mb-4">
            <h6 class="section-title">방문한 나라</h6>
            <div class="visited-block mt-3 p-3">
              <ul class="list-inline text-center">
                <li class="list-inline-item country-item" v-for="country in profileData.visited" :key="country.name">
                  <img :src="getImageUrl(country.image1)" class="country-img rounded-circle shadow-sm" alt="Visited Country" @click="handleClick(country.id)">
                  <span class="country-name d-block mt-2">{{ country.name }}</span>
                </li>
              </ul>
            </div>
          </div>
          <div class="section">
            <h6 class="section-title">관심 있는 나라</h6>
            <div class="interested-block mt-3 p-3">
              <ul class="list-inline text-center">
                <li class="list-inline-item country-item" v-for="country in profileData.interested" :key="country.name" @click="handleClick(country.id)">
                  <img :src="getImageUrl(country.image1)" class="country-img rounded-circle shadow-sm" alt="Interested Country">
                  <span class="country-name d-block mt-2">{{ country.name }}</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const props = defineProps({
  isVisible: Boolean,
});

const emit = defineEmits(['close']);
const store = useCounterStore();
const router = useRouter();

const profileData = ref(null);

const closeModal = () => {
  emit('close');
};

const getImageUrl = (imagePath) => {
  return store.getImageUrl(imagePath);
};

const goToDetail = async (countryId) => {
  await store.detailCountry(countryId);
  router.push({ name: 'DetailView', params: { countryId } });
};

const handleClick = async (countryId) => {
  closeModal();
  await goToDetail(countryId);
};

onMounted(() => {
  store.profilePage(store.user);
});

watch(
  () => store.profileData,
  (newData) => {
    profileData.value = newData;
  },
  { immediate: true }
);
</script>

<style scoped>
.modal-content {
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 0.5rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}
.modal-header {
  border-bottom: 1px solid #e9ecef;
}
.modal-header .btn-close {
  background-color: #00000000;
}
.modal-body {
  padding: 1.5rem;
}
.user-info-block {
  border-radius: 0.5rem;
  background-color: #e9ecef;
  text-align: left;
}
.section {
  margin-bottom: 1.5rem;
}
.section-title {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 1rem;
}
.visited-block, .interested-block {
  border-radius: 0.5rem;
  background-color: #f8f9fa;
}
.country-img {
  width: 70px;
  height: 70px;
  cursor: pointer;
  transition: transform 0.2s;
}
.country-img:hover {
  transform: scale(1.1);
}
.country-name {
  font-size: 1.1rem;
}
.country-item {
  margin: 10px 20px;
}
</style>
