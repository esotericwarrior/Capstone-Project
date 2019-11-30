<template>
  <div>
    <v-list-item>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <router-link
            :to="{
              name: 'profile',
              params: { username: comment.author, displayname: comment.author }
            }"
          >
            <v-list-item-avatar color="grey" v-on="on"></v-list-item-avatar>
          </router-link>
        </template>
        <span>{{ comment.author }}</span>
      </v-tooltip>
      <v-list-item-content>
        <v-list-item-title class="headline">
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <router-link
                :to="{ name: 'profile', params: { username: comment.author } }"
              >
                <span v-on="on">{{ comment.author }}</span>
              </router-link>
            </template>
            <span>{{ comment.author }}</span>
          </v-tooltip>
        </v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <p>{{ likesCounter }} likes</p>
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
    <v-tooltip bottom>
      <template v-slot:activator="{ on }">
        <v-btn icon @click="toggleLike">
          <font-awesome-icon
            :color="userLikedComment ? 'red' : ''"
            icon="heart"
            size="2x"
            v-on="on"
          />
        </v-btn>
      </template>
      <span>Like</span>
    </v-tooltip>
    <v-divider />
  </div>
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
<style lang="scss" scoped></style>
