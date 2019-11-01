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
          src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
        >
        </v-img>

        <v-card-actions>
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn icon>
                <font-awesome-icon icon="heart" size="2x" v-on="on" />
              </v-btn>
            </template>
            <span>Like</span>
          </v-tooltip>
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn icon>
                <font-awesome-icon icon="comment" size="2x" v-on="on" />
              </v-btn>
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
  </v-container>
</template>

<script>
// import axios from "axios";
import { apiService } from "@/common/api.service";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

export default {
  name: "NewsFeed",
  components: {
    FontAwesomeIcon
  },
  data() {
    return {
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
      let endpoint = "api/posts/";
      apiService(endpoint).then(data => {
        this.posts.push(...data.results);
      });
    }
  },
  mounted() {
    this.getPosts();
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
