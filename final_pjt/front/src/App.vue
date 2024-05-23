<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
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
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Direct
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li v-for="(countries, area) in groupedCountries" :key="area" class="dropdown-submenu">
                  <a class="dropdown-item dropdown-toggle" href="#" role="button">{{ area }}</a>
                  <ul class="dropdown-menu">
                    <li v-for="country in countries" :key="country.id">
                      <RouterLink class="dropdown-item" :to="{ name: 'DetailView', params: { countryId: country.id } }">
                        {{ country.name }}
                      </RouterLink>
                    </li>
                  </ul>
                </li>
              </ul>
            </li>
          </ul>
        </div>

        <div class="ms-auto">
          <template v-if="!store.token">
            <button class="btn btn-outline-primary me-2" @click="showLoginModal = true">로그인</button>
            <button class="btn btn-outline-secondary" @click="showSignUpModal = true">회원가입</button>
          </template>
          <template v-else>
            <button class="btn btn-outline-secondary me-2" @click="showProfileModal = true">프로필</button>
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
    <ProfileModal v-if="showProfileModal" :isVisible="showProfileModal" @close="closeProfileModal" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { RouterView, RouterLink } from 'vue-router';
import LoginModal from './components/LoginModal.vue';
import SignUpModal from './components/SignUpModal.vue';
import ProfileModal from './components/ProfileModal.vue';
import { useCounterStore } from './stores/counter';
import { useCountryStore } from './stores/countryStore';

const store = useCounterStore();
const countryStore = useCountryStore();

const showLoginModal = ref(false);
const showSignUpModal = ref(false);
const showProfileModal = ref(false);

const closeLoginModal = () => {
  showLoginModal.value = false;
};

const closeSignUpModal = () => {
  showSignUpModal.value = false;
};

const closeProfileModal = () => {
  showProfileModal.value = false;
};

const logoutbutton = () => {
  store.token = null;
  store.user = null;
};

// 지역별로 국가들을 그룹화합니다.
const groupedCountries = computed(() => {
  return countryStore.countries.reduce((groups, country) => {
    const area = country.area;
    if (!groups[area]) {
      groups[area] = [];
    }
    groups[area].push(country);
    return groups;
  }, {});
});

onMounted(() => {
  countryStore.fetchCountries();
});
</script>

<style scoped>
.navbar-nav .dropdown-submenu {
  position: relative;
}

.navbar-nav .dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -1px;
  display: none;
}

.navbar-nav .dropdown-submenu:hover > .dropdown-menu,
.navbar-nav .dropdown-submenu:focus > .dropdown-menu {
  display: block;
}
</style>
