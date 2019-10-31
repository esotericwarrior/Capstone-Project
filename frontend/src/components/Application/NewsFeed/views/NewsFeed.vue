<template>
  <v-container> </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "NewsFeed",
  data() {
    return {
      posts: []
    };
  },
  methods: {
    getPosts() {
      axios
        .get("http://127.0.0.1:8000/api/posts/")
        .then(response => (this.posts = response.data.results))
        // eslint-disable-next-line no-console
        .catch(error => console.log(error));
    }
  },
  mounted: {}
};
</script>
<style lang="scss" scoped></style>
