<template>
  <div class="modal show d-block" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Travel Recommendations</h5>
          <button type="button" class="btn-close" @click="$emit('close')"></button>
        </div>
        <div class="modal-body">
          <ul>
            <li v-for="rec in recommendations" :key="rec.country">
              <strong>{{ rec.country }}</strong>: {{ rec.travel_style }} (Cost Index: {{ rec.cost_index }})
            </li>
          </ul>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="$emit('close')">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  recommendations: Array
});
</script>

<style scoped>
/* Add your styles here if needed */
</style>
