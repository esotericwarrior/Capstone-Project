<template>
  <div class="single-post mt-2">
    <div class="container">
      <img :src="post.url">
      <blockquote class="imgur-embed-pub" lang="en" data-id="oBlivgM"></blockquote>
      <h1>{{ post.content }}</h1>
      <PostActions v-if="isPostAuthor" :slug="post.slug" />
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
          <p class="error">{{ error }}</p>
        </div>
      </div>
    </div>
    <div class="container">
      <Comment
        v-for="comment in comments"
        :comment="comment"
        :key="comment.id"
        :requestUser="requestUser"
        @delete-comment="deleteComment"
      />
    </div>
    <div align="center">
      <!-- Load More Comments Button -->
      <v-btn
        text
        color="success"
        v-show="next"
        @click="getPostComments"
        class="ma-2"
      >
        Load More Comments
        <template v-slot:loader>
          <span>Loading...</span>
        </template>
      </v-btn>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { Comment } from "@/components/Application/Comment";
import { PostActions } from "@/components/Application/Posts";

export default {
  name: "Post",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    Comment,
    PostActions
  },
  computed: {
    isPostAuthor() {
      // Returns true if the logged in user is also the author of the post instance
      return this.post.author === this.requestUser;
    }
  },
  created() {
    this.getPostComments();
    this.getPostData();
    this.setRequestUser();
  },
  data() {
    return {
      comments: [],
      error: null,
      loadingComments: false,
      newCommentBody: null,
      next: null,
      post: {},
      requestUser: null,
      showForm: false,
      userHasCommented: false
    };
  },
  methods: {
    async deleteComment(comment) {
      let endpoint = `/api/comments/${comment.id}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.$delete(this.comments, this.comments.indexOf(comment));
      } catch (err) {
        // eslint-disable-next-line no-console
        console.log(err);
      }
    },
    // Get a page of comments for a single post from the REST API
    getPostComments() {
      let endpoint = `/api/posts/${this.slug}/comments/`;
      if (this.next) {
        endpoint = this.next;
      }
      apiService(endpoint).then(data => {
        this.comments.push(...data.results);
        this.loadingComments = true;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
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
            this.comments.unshift(data.data);
            // eslint-disable-next-line no-console
            console.log(this.comments);
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
    },
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    }
  }
};
</script>
<style lang="scss" scoped>
.error {
  font-weight: bold;
  color: blue;
}
</style>
