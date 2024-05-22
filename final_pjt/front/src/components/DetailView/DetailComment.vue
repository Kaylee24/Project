<template>
  <div class="detail-comments">
    <h3>댓글</h3>
    <div>
      <div v-for="comment in comments" :key="comment.id" class="comment">
        <p>username : {{ comment.user.name }}</p>
        <p>{{ comment.content }}</p>
        <small>{{ comment.created_at }}</small>
      </div>
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
    <div v-else-if="!comments.length">
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
  return store.detailContryData.comment_set
})
const isLogin = computed(() => store.isLogin)

console.log('DetailComment의 store.detailCountryData', store.detailContryData)
console.log('comments', comments)
// console.log(comments)

const submitComment = async () => {
  await store.addComment({
    countryId: store.detailContryData.id,
    content: newComment.value,
    // user: user
  })
  newComment.value = ''

  // // 새로운 댓글을 포함하여 모든 댓글을 다시 가져옴
  // await store.fetchComments(store.detailContryData.id)
  
  // // 댓글 작성 후 DetailView로 이동
  // goToDetailView(store.detailContryData.id)
  // console.log('add는 됨')
  // console.log(comments.value)

}

// const goToDetailView = (countryId) => {
//   console.log('push되기 전')
//   router.replace({ name: 'DetailView', params: { countryId } })
//   console.log('push가 됨')
// }
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
