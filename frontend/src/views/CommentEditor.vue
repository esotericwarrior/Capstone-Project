<template>
  <div class="container"></div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "CommentsEditor",
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      commentBody: null,
      error: null,
      postSlug: null
    };
  },
  methods: {},
  async beforeRouteEnter(to, from, next) {
    // Get the comment's data from the REST API and set two data properties for the component
    let endpoint = `/api/comments/${to.params.id}/`;
    let data = await apiService(endpoint);
    return next(
      vm => ((vm.commentBody = data.body), (vm.postSlug = data.post_slug))
    );
  }
};
</script>
