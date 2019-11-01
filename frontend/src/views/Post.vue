<template>
  <div class="single-post mt-2">
    <div class="container">
      <h1>{{ post.content }}</h1>
      <p class="mb-0">
        Posted by:
        <span class="author-name">{{ post.author }}</span>
      </p>
      <p>{{ post.created_at }}</p>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "Post",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  created() {
    this.getPostData();
  },
  data() {
    return {
      post: {}
    };
  },
  methods: {
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
