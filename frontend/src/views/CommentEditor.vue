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
      commentBody: null
    };
  },
  methods: {}
};
</script>
