<template>
  <div>
    <router-link :to="{ name: 'post-editor', params: { slug: slug } }"
      ><v-btn>Edit</v-btn>
    </router-link>
    <v-btn @click="deletePost">Delete</v-btn>
  </div>
</template>
<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "PostActions",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  methods: {
    async deletePost() {
      let endpoint = `/api/posts/${this.slug}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.$router.push("/");
      } catch (err) {
        // eslint-disable-next-line no-console
        console.log(err);
      }
    }
  }
};
</script>
<style lang="scss" scoped>
a {
  text-decoration: none;
}
</style>
