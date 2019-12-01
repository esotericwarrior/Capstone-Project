<template>
  <v-container>
    <v-row no-gutters>
      <v-col>
        <div>
          <v-form @submit.prevent="onSubmit">
            <v-textarea
              auto-grow
              background-color="grey lighten-5"
              class="mx-2 grey lighten-5"
              no-resize
              solo
              v-model="commentBody"
            >
              <template v-slot:append>
                <v-btn type="submit" color="success">Save Comment</v-btn>
              </template>
            </v-textarea>
          </v-form>
          <div v-if="error">
            <p class="error">{{ error }}</p>
          </div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "CommentsEditor",
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      commentBody: null,
      error: null,
      postSlug: null
    };
  },
  methods: {
    onSubmit() {
      if (this.commentBody) {
        let endpoint = `/api/comments/${this.id}/`;
        apiService(endpoint, "PUT", { body: this.commentBody }).then(() => {
          this.$router.push({
            name: "post",
            params: { slug: this.postSlug }
          });
        });
      } else {
        this.error = "You can't submit an empty comment!";
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // Get the comment's data from the REST API and set two data properties for the component
    let endpoint = `/api/comments/${to.params.id}/`;
    let data = await apiService(endpoint);
    return next(
      vm => ((vm.commentBody = data.body), (vm.postSlug = data.post_slug))
    );
  }
};
</script>
