<template>
  <div class="container mt-2">
    <h1 class="mb-3">Post Something</h1>
    <v-form @submit.prevent="onSubmit">
      <v-textarea
        v-model="post_body"
        class="form-control"
        placehodler="What do you want to post?"
        rows="3"
      ></v-textarea>
      <v-btn type="submit">Publish</v-btn>
    </v-form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>
<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "PostEditor",
  props: {
    slug: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      error: null,
      post_body: null
    };
  },
  methods: {
    onSubmit() {
      // Tell the REST API to create or update a Post Instance
      if (!this.post_body) {
        this.error = "You can't send an empty post!";
      } else if (this.post_body.length > 240) {
        this.error = "Ensure this field has no more than 240 characters!";
      } else {
        let endpoint = "/api/posts/";
        let method = "POST";
        // if (this.slug !== undefined) {
        //   endpoint += `${this.slug}/`;
        //   method = "PUT";
        // }
        apiService(endpoint, method, { content: this.post_body }).then(
          post_data => {
            this.$router.push({
              name: "post",
              params: { slug: post_data.slug }
            });
          }
        );
      }
    }
  }
};
</script>

<style lang="scss" scoped></style>
