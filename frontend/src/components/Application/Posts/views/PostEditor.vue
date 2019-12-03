<template>
  <v-container>
    <v-form @submit.prevent="onSubmit">
      <v-card class="mx-auto grey lighten-5" flat max-width="800">
        <v-card-title class="headline justify-center">
          What would you like to post?
        </v-card-title>

        <v-row no-gutters>
          <v-col>
            <v-textarea
              append
              auto-grow
              v-model="post_body"
              placeholder="What do you want to post?"
            >
              <template v-slot:append>
                <speechToText
                  :text.sync="post_body"
                  @speechend="speechEnd"
                ></speechToText>
              </template>
            </v-textarea>
          </v-col>
        </v-row>
        <v-card-actions>
          <input
            type="file"
            id="file"
            ref="file"
            v-on:change="onFileChange()"
          />
          <v-spacer />
          <v-btn type="submit">Publish</v-btn>
        </v-card-actions>
      </v-card>
    </v-form>

    <v-snackbar color="red" multi-line v-model="snackbar">
      {{ error }}
      <v-btn text @click="snackbar = false">
        Close
      </v-btn>
    </v-snackbar>
  </v-container>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { imgurService } from "@/common/api.service.js";
import { SpeechToText } from "@/components/Application/Speech";

export default {
  name: "PostEditor",
  created() {},
  props: {
    lang: {
      type: String,
      default: "en-US"
    },
    slug: {
      type: String,
      required: false
    }
  },
  components: {
    SpeechToText
  },
  data() {
    return {
      error: null,
      speaking: false,
      toggle: false,
      runtimeTranscription: "",
      sentences: null,
      speech: null,
      post_body: "",
      file: null,
      text: "",
      snackbar: false,
      url: null
    };
  },
  methods: {
    speechEnd({ sentences, post_body }) {
      // eslint-disable-next-line no-console
      console.log("text", post_body);
      // eslint-disable-next-line no-console
      console.log("sentences", sentences);
      this.sentences = sentences;
    },
    onFileChange() {
      this.file = this.$refs.file.files[0];
    },
    onSubmit() {
      var speech = this.speech;
      // Tell the REST API to create or update a Post Instance
      if (
        this.post_body &&
        this.post_body.length > 0 &&
        (speech && speech.length > 0)
      ) {
        this.error =
          "Please use text-to-speech or type your message, not both.";
        this.snackbar = true;
      } else if (!this.post_body && (speech && speech.length < 1)) {
        this.error = "You can't send an empty post!";
        this.snackbar = true;
      } else if (
        (this.post_body && this.post_body.length > 240) ||
        (speech && speech.length > 240)
      ) {
        this.error = "Ensure this field has no more than 240 characters!";
        this.snackbar = true;
      } else if (!this.file) {
        this.error = "Please upload a picture or video to go with your post";
        this.snackbar = true;
      } else {
        let endpoint = "/api/posts/";
        let method = "POST";
        var new_content;
        if (!this.post_body) {
          new_content = speech;
        } else {
          new_content = this.post_body;
        }
        if (this.slug !== undefined) {
          endpoint += `${this.slug}/`;
          method = "PUT";
        }
        let imgur_data = new FormData();
        var file_type;
        if (this.file instanceof File) {
          file_type = "file";
        } else {
          file_type = "base64";
        }
        imgur_data.append("image", this.file);
        imgur_data.append("title", new_content);
        imgur_data.append("type", file_type);
        let data = new FormData();
        data.append("content", new_content);
        data.append("file", this.file);
        imgurService(imgur_data).then(imgur_data => {
          // eslint-disable-next-line no-console
          console.log(imgur_data);
          // eslint-disable-next-line no-console
          console.log(imgur_data["data"]["data"]["link"]);
          data.append("url", imgur_data["data"]["data"]["link"]);
          // eslint-disable-next-line no-console
          console.log(data.get("url"));
          apiService(endpoint, method, data).then(post_data => {
            this.$router.push({
              name: "post",
              params: { slug: post_data.data.slug }
            });
          });
        });
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    if (to.params.slug !== undefined) {
      let endpoint = `/api/posts/${to.params.slug}/`;
      let data = await apiService(endpoint);
      return next(vm => (vm.post_body = data.content));
    } else {
      return next();
    }
  }
};
</script>

<style lang="scss" scoped></style>
