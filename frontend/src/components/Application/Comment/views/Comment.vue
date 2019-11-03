<template>
  <div>
    <p>
      <strong>{{ comment.author }}</strong> &#8901; {{ comment.created_at }}
    </p>
    <p>{{ comment.body }}</p>
    <div v-if="isCommentAuthor">
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn icon>
            <router-link
              :to="{ name: 'comment-editor', params: { id: comment.id } }"
            >
              <font-awesome-icon icon="edit" size="2x" v-on="on" />
            </router-link>
          </v-btn>
        </template>
        <span>Edit Comment</span>
      </v-tooltip>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn icon>
            <font-awesome-icon
              icon="trash"
              size="2x"
              v-on="on"
              @click="triggerDeleteComment"
            />
          </v-btn>
        </template>
        <span>Delete Comment</span>
      </v-tooltip>
    </div>
    <v-divider />
  </div>
</template>

<script>
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

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
  components: {
    FontAwesomeIcon
  },
  computed: {
    isCommentAuthor() {
      return this.comment.author === this.requestUser;
    }
  },
  data() {
    return {};
  },
  methods: {
    triggerDeleteComment() {
      this.$emit("delete-comment", this.comment);
    }
  }
};
</script>
<style lang="scss" scoped></style>
