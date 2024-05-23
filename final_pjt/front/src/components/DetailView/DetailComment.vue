<template>
  <div class="detail-comments" style="margin-top: 7%;">
    <h3>댓글</h3>
    <div v-if="comments.length">
      <div v-for="comment in comments" :key="comment.id" class="comment">
        <div class="comment-content">
          <p>username: {{ comment.user.name }}</p>
          <p>{{ comment.content }}</p>
          <small>{{ comment.created_at.slice(0, 10) }}</small> <!-- 댓글 작성 시간 10개까지만 slicing -->
        </div>
        <button v-if="isLogin && comment.user.username === store.user" @click="deleteComment(comment.id)" class="delete-button">삭제</button> <!-- 삭제 버튼 -->
      </div>
    </div>
    <div v-else>
      <p>댓글이 없습니다.</p>
    </div>
    <div v-if="isLogin">
      <form @submit.prevent="submitComment">
        <div class="mb-3">
          <label for="comment" class="form-label">댓글 작성</label>
          <textarea v-model="newComment" class="form-control" id="comment" rows="3" required @keyup.enter="submitComment"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">댓글 작성</button>
      </form>
    </div>
    <div v-else>
      <p>로그인한 사용자만 댓글을 작성할 수 있습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useCounterStore()
const newComment = ref('')
const comments = computed(() => {
  return store.detailCountryData?.comment_set || []
})
const isLogin = computed(() => store.isLogin)

const submitComment = async () => {
  await store.addComment({
    countryId: store.detailCountryData.id,
    content: newComment.value,
  })
  newComment.value = ''
}

const deleteComment = async (commentId) => {
  await store.deleteComment(commentId)
}

onMounted(() => {
  if (store.detailCountryData && store.detailCountryData.id) {
    store.fetchComments(store.detailCountryData.id)
  }
})
</script>

<style scoped>
.detail-comments {
  margin-top: 20px;
  margin-right: 10%;
}

.comment {
  display: flex;
  align-items: flex-start;
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
}

.comment-content {
  flex: 1;
}

.delete-button {
  padding: 5px 10px;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-left: 10px; /* 여백 추가 */
  align-self: flex-end;
}

.delete-button:hover {
  background-color: #bb2d3b;
}
</style>
