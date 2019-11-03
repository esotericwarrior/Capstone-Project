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
    },
    requestUser: {
      type: String,
      required: true
    }
  },
  computed: {
    isCommentAuthor() {
      return this.comment.author === this.requestUser;
    }
  }
  data() {
    return {};
  }
};
</script>
<style lang="scss" scoped></style>
