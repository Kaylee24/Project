import { createRouter, createWebHistory } from 'vue-router';
import MainView from '@/views/MainView.vue';
import TestView from '@/views/TestView.vue';
import ComparisonView from '@/views/ComparisonView.vue';
import DetailView from '@/views/DetailView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainView',
      component: MainView,
    },
    {
      path: '/test',
      name: 'TestView',
      component: TestView,
    },
    {
      path: '/comparison',
      name: 'ComparisonView',
      component: ComparisonView,
    },
    {
      path: '/detail/:countryId',
      name: 'DetailView',
      component: DetailView,
      props: true,
    },
  ],
});

export default router;
