<template>
  <v-card max-width="800" class="mx-auto grey lighten-5" flat>
    <v-card-text color="grey lighten-5">
      <v-card-title class="pa-0 ma-0">
        <!-- Avatar -->
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

        <!-- Comment Author -->
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
        <v-spacer></v-spacer>

        <v-menu bottom left>
          <template v-slot:activator="{ on }">
            <v-btn icon v-on="on">
              <font-awesome-icon icon="ellipsis-h" size="2x" />
            </v-btn>
          </template>

          <v-list>
            <v-list-item>
              <v-list-item-title>
                <div v-if="isCommentAuthor">
                  <router-link
                    :to="{
                      name: 'comment-editor',
                      params: { id: comment.id }
                    }"
                  >
                    <v-list-item>
                      <v-tooltip bottom>
                        <template v-slot:activator="{ on }">
                          <v-btn text icon>
                            <font-awesome-icon
                              icon="edit"
                              size="2x"
                              v-on="on"
                            />
                          </v-btn>
                        </template>
                        <span>Edit Comment</span>
                      </v-tooltip>
                      <v-list-item-title>Edit Comment</v-list-item-title>
                    </v-list-item>
                  </router-link>

                  <v-list-item @click="triggerDeleteComment">
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on }">
                        <v-btn icon>
                          <font-awesome-icon icon="trash" size="2x" v-on="on" />
                        </v-btn>
                      </template>
                      <span>Delete Comment</span>
                    </v-tooltip>
                    <v-list-item-title>Delete Comment</v-list-item-title>
                  </v-list-item>
                </div>

                <div v-else>
                  <v-list-item>
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on }">
                        <v-btn icon>
                          <font-awesome-icon icon="share" size="2x" v-on="on" />
                        </v-btn>
                      </template>
                      <span>Share</span>
                    </v-tooltip>
                    <v-list-item-title>
                      Share
                    </v-list-item-title>
                  </v-list-item>
                  <v-list-item>
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on }">
                        <v-btn icon>
                          <font-awesome-icon icon="ban" size="2x" v-on="on" />
                        </v-btn>
                      </template>
                      <span>Unfollow {{ comment.author }}</span>
                    </v-tooltip>
                    <v-list-item-title>
                      Unfollow {{ comment.author }}
                    </v-list-item-title>
                  </v-list-item>
                </div>
              </v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-card-title>
    </v-card-text>

    <v-card-text class="title font-weight-light pl-5 ma-0 pa-0">
      {{ comment.body }}
    </v-card-text>

    <v-card-actions>
      <v-list-item class="grow">
        <v-list-item-content>
          <v-list-item-title>{{ likesCounter }} likes</v-list-item-title>
        </v-list-item-content>

        <v-row align="center" justify="end">
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
        </v-row>
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
      items: [{ title: "Edit" }, { title: "Delete" }],
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
