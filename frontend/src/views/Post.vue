<template>
  <div class="single-post mt-2">
    <div class="container">
      <h1>{{ post.content }}</h1>
      <p class="mb-0">
        Posted by:
        <span class="author-name">{{ post.author }}</span>
      </p>
      <p>{{ post.created_at }}</p>
      <v-divider />
    </div>
    <div class="container">
      <Comment
        v-for="(comment, index) in comments"
        :comment="comment"
        :key="index"
      />
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { Comment } from "@/components/Application/Comment";

export default {
  name: "Post",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    Comment
  },
  created() {
    this.getPostComments();
    this.getPostData();
  },
  data() {
    return {
      comments: [],
      error: null,
      newCommentBody: null,
      post: {}
    };
  },
  methods: {
    getPostComments() {
      let endpoint = `/api/posts/${this.slug}/comments/`;
      apiService(endpoint).then(data => {
        this.comments = data.results;
      });
    },
    getPostData() {
      let endpoint = `/api/posts/${this.slug}/`;
      apiService(endpoint).then(data => {
        this.post = data;
        this.setPageTitle(data.content);
      });
    },
    setPageTitle(title) {
      document.title = title;
    }
  }
};
</script>
<style lang="scss" scoped></style>
