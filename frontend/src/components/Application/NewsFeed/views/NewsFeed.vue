<template>
  <v-container>
    <div v-for="post in posts" :key="post.pk">
      <v-card class="mx-auto" max-width="650">
        <v-list-item>
          <v-list-item-avatar color="grey"></v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title class="headline">
              {{ post.author }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-img
          class="white--text align-end"
          height="600px"
          :src="post.url"
        >
        </v-img>

        <v-card-actions>
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn icon @click="toggleLike(post)">
                <font-awesome-icon
                  :color="post.user_has_liked ? 'red' : ''"
                  icon="heart"
                  size="2x"
                  v-on="on"
                />
              </v-btn>
            </template>
            <span>Like</span>
          </v-tooltip>
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
            <router-link
              :to="{ name: 'post', params: { slug: post.slug } }"
              class="post-link"
              >              <v-btn icon>
                <font-awesome-icon icon="comment" size="2x" v-on="on" />
              </v-btn>

            </router-link>
            </template>
            <span>Comment</span>
          </v-tooltip>
          <v-spacer />
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn icon>
                <font-awesome-icon icon="star" size="2x" v-on="on" />
              </v-btn>
            </template>
            <span>Favorite</span>
          </v-tooltip>
        </v-card-actions>

        <v-card-subtitle class="pa-0 pl-4">
          {{ post.likes_count }} likes
        </v-card-subtitle>

        <v-card-subtitle class="pb-0">
          Posted by: {{ post.author }} on {{ post.created_at }}
        </v-card-subtitle>

        <v-card-text class="text--primary">
          <div>
            <router-link
              :to="{ name: 'post', params: { slug: post.slug } }"
              class="post-link"
              >{{ post.content }}
            </router-link>
          </div>
          <div>Comments: {{ post.comments_count }}</div>
        </v-card-text>
      </v-card>
      <v-divider class="mx-auto mt-5 mb-5" inset dark color="white" />
    </div>
    <div align="center">
      <!-- Load More Posts Button -->
      <v-btn color="success" v-show="next" @click="getPosts" class="ma-2">
        Load More Posts
        <template v-slot:loader>
          <span>Loading...</span>
        </template>
      </v-btn>
    </div>
  </v-container>
</template>

<script>
// import axios from "axios";
import { apiService } from "@/common/api.service.js";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

export default {
  name: "NewsFeed",
  components: {
    FontAwesomeIcon
  },
  data() {
    return {
      loader: null,
      loadingPosts: false,
      next: null,
      posts: []
    };
  },
  methods: {
    getPosts() {
      // axios
      //   .get("http://127.0.0.1:8000/api/posts/")
      //   .then(response => (this.posts = response.data.results))
      //   // eslint-disable-next-line no-console
      //   .catch(error => console.log(error));
      this.loader = this.loadingPosts;
      // Make a GET Request to the posts list endpoint and populate the posts array.
      let endpoint = "/api/posts/";
      // If there are paginated posts, set the appropriate endpoint.
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingPosts = true;
      apiService(endpoint).then(data => {
        this.posts.push(...data.results);
        this.loadingPosts = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
    likePost(post) {
      post.user_has_liked = true;
      post.likes_count += 1;
      let endpoint = `/api/posts/${post.id}/like/`;
      apiService(endpoint, "POST");
    },
    toggleLike(post) {
      post.user_has_liked === false
        ? this.likePost(post)
        : this.unLikePost(post);
    },
    unLikePost(post) {
      post.user_has_liked = false;
      post.likes_count -= 1;
      let endpoint = `/api/posts/${post.id}/like/`;
      apiService(endpoint, "DELETE");
    }
  },
  mounted() {
    this.getPosts();
  },
  watch: {
    loader() {
      const l = this.loader;
      this[l] = !this[l];

      setTimeout(() => (this[l] = false), 3000);

      this.loader = null;
    }
  }
};
</script>
<style lang="scss" scoped>
.post-link {
  font-weight: bold;
  color: black;
}

.post-link:hover {
  color: #343a40;
  text-decoration: none;
}
</style>
