<template>
  <div></div>
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
  data() {
    return {};
  }
};
</script>
<style lang="scss" scoped></style>
