<template>
  <div></div>
</template>
<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "PostEditor",
  created() {},
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
