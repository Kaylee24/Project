<template>
  <div class="detail-comments">
    <h3>댓글</h3>
    <div v-if="comments.length">
      <div v-for="comment in comments" :key="comment.id" class="comment">
        <strong>{{ comment.user.username }}</strong>
        <p>{{ comment.content }}</p>
        <small>{{ comment.created_at }}</small>
      </div>
    </div>
    <div v-else>
      아직 작성된 댓글이 없습니다. 첫번째 댓글을 남겨보세요!
    </div>
    <div v-if="isLogin">
      <form @submit.prevent="submitComment">
        <div class="mb-3">
          <label for="comment" class="form-label">댓글 작성</label>
          <textarea v-model="newComment" class="form-control" id="comment" rows="3" required></textarea>
        </div>
        <button type="submit" class="btn btn-primary">댓글 작성</button>
      </form>
    </div>
    <div v-else-if="!comments.length">
      <p>로그인한 사용자만 댓글을 작성할 수 있습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();
const newComment = ref('');
const comments = computed(() => store.detailContryData.comment_set);
const isLogin = computed(() => store.isLogin);

const submitComment = () => {
  store.addComment({ countryId: store.detailContryData.id, content: newComment.value });
  newComment.value = '';
};

onMounted(() => {
  // 댓글을 가져오는 API 호출
  store.fetchComments(store.detailContryData.id);
});
</script>

<style scoped>
.detail-comments {
  margin-top: 20px;
}
.comment {
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
}
</style>
