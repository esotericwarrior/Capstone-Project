<template>
  <div class="single-post mt-2">
    <div class="container">
      {{ slug }}
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
  }
};
</script>
<style lang="scss" scoped></style>
