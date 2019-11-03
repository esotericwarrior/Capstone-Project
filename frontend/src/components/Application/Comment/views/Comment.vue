<template>
  <div>
    <p>
      <strong>{{ comment.author }}</strong> &#8901; {{ comment.created_at }}
    </p>
    <p>{{ comment.body }}</p>
    <v-divider />
  </div>
</template>

<script>
export default {
  name: "Comment",
  props: {
    comment: {
      type: Object,
      required: true
    }
  },
  data() {
    return {};
  }
};
</script>
<style lang="scss" scoped></style>
