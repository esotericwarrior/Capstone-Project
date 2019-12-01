<template>
  <v-card max-width="800" class="mx-auto grey lighten-5" flat>
    <v-card-text color="grey lighten-5">
      <v-card-title>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <router-link
              :to="{
                name: 'profile',
                params: {
                  username: comment.author,
                  displayname: comment.author
                }
              }"
            >
              <v-list-item-avatar color="grey" v-on="on"></v-list-item-avatar>
            </router-link>
          </template>
          <span>{{ comment.author }}</span>
        </v-tooltip>

        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <router-link
              :to="{
                name: 'profile',
                params: { username: comment.author }
              }"
            >
              <span v-on="on">{{ comment.author }}</span>
            </router-link>
          </template>
          <span>{{ comment.author }}</span>
        </v-tooltip>
        <span class="title font-weight-light pl-5">{{ comment.body }}</span>
      </v-card-title>
      <v-card-subtitle class="pl-5">{{ likesCounter }} likes</v-card-subtitle>
    </v-card-text>

    <v-card-actions>
      <v-list-item class="grow">
        <v-list-item-content>
          <v-list-item-title>{{ likesCounter }} likes</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-card-actions>
    <v-divider />
  </v-card>
</template>

<script>
import { apiService } from "@/common/api.service.js";
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
    return {
      liked: false,
      likesCounter: this.comment.likes_count,
      userLikedComment: this.comment.user_has_liked
    };
  },
  methods: {
    likeComment() {
      this.userLikedComment = true;
      this.likesCounter += 1;
      let endpoint = `/api/comments/${this.comment.id}/like/`;
      apiService(endpoint, "POST");
    },
    toggleLike() {
      this.userLikedComment === false
        ? this.likeComment()
        : this.unLikeComment();
    },
    triggerDeleteComment() {
      this.$emit("delete-comment", this.comment);
    },
    unLikeComment() {
      this.userLikedComment = false;
      this.likesCounter -= 1;
      let endpoint = `/api/comments/${this.comment.id}/like/`;
      apiService(endpoint, "DELETE");
    }
  }
};
</script>
<style lang="scss" scoped>
a {
  text-decoration: none;
  color: black;
}
</style>
