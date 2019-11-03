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
      <div>
        <v-form @submit.prevent="onSubmit">
          <v-textarea
            background-color="grey lighten-5"
            class="mx-2 grey lighten-5"
            flat
            no-resize
            placeholder="Add a comment..."
            rows="2"
            solo
            v-model="newCommentBody"
          >
            <template v-slot:append>
              <v-btn type="submit" color="success">Post</v-btn>
            </template>
          </v-textarea>
        </v-form>
        <div v-if="error">
          {{ error }}
        </div>
      </div>
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
      post: {},
      showForm: false,
      userHasCommented: false
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
    onSubmit() {
      // Tell the REST API to create a new comment for this post based on the user input, then update some data properties
      if (this.newCommentBody) {
        let endpoint = `/api/posts/${this.slug}/comment/`;
        apiService(endpoint, "POST", { body: this.newCommentBody }).then(
          data => {
            this.comments.unshift(data);
          }
        );
        this.newCommentBody = null;
        this.userHasCommented = true;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "Please add a comment before submitting!";
      }
    },
    setPageTitle(title) {
      document.title = title;
    }
  }
};
</script>
<style lang="scss" scoped></style>
