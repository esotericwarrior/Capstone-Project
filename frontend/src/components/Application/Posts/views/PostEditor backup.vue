<template>
  <div class="container mt-2">
    <h1 class="mb-3">Post Something</h1>
    <v-form @submit.prevent="onSubmit">
      <v-textarea
        v-model="post_body"
        class="form-control"
        placeholder="What do you want to post?"
        rows="3"
        x-webkit-speech
      ></v-textarea>
      <input type="file" id="file" ref="file" v-on:change="onFileChange()"/><br />
      <v-btn type="submit">Publish</v-btn>
    </v-form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>
<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "PostEditor",
  created() {},
  data() {
    return {
      error: null,
      post_body: null,
      file: null
    };
  },
  methods: {
    onFileChange() {
     this.file = this.$refs.file.files[0];
    },
    onSubmit() {
       /*eslint no-console: ["error", { allow: ["log", "error"]}] */
       // console.log(this)
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

        /*eslint no-console: ["error", { allow: ["log", "error"]}] */
        //console.log(this.post_body)
        //console.log(this.file)
        console.log(this)

        apiService(endpoint, method, {
          content: this.post_body,
          file: this.file,
        }).then(post_data => {
        /*eslint no-console: ["error", { allow: ["log", "error"]}] */
          console.log(post_data)
          this.$router.push({
            name: "post",
            params: { slug: post_data.slug }
          });
        });
      }
    }
  }
};
</script>

<style lang="scss" scoped></style>
