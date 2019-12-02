<template>
  <div class="container mt-2">
    <h1 class="mb-3">Post Something</h1>
    <v-form @submit.prevent="onSubmit">
      <v-card>
        <v-card-text>
          <v-layout row wrap justify-space-around>
            <v-flex xs8 sm9 text-xs-center>
              <v-text-field
                v-model="post_body"
                class="form-control"
                placeholder="What do you want to post?"
                rows="3"
              ></v-text-field>
              <p v-if="error" class="grey--text">{{ error }}</p>
              <p v-else class="mb-0">
                <v-text-field
                  v-model="speech"
                  v-if="sentences.length > 0"
                  v-bind:key="sentences"
                  :value="sentences"
                >
                </v-text-field>
                <span v-for="sentence in sentences" v-bind:key="sentence"
                  >{{ sentence }}
                </span>
                <span>{{ runtimeTranscription }}</span>
              </p>
            </v-flex>
            <v-flex xs2 sm1 text-xs-center>
              <v-btn
                dark
                @click.stop="
                  toggle ? endSpeechRecognition() : startSpeechRecognition()
                "
                icon
                :color="!toggle ? 'grey' : speaking ? 'red' : 'red darken-3'"
                :class="{ 'animated infinite pulse': toggle }"
              >
                <v-icon>{{ toggle ? "mic_off" : "mic" }}</v-icon>
              </v-btn>
            </v-flex>
          </v-layout>
        </v-card-text>
      </v-card>

      <input
        type="file"
        id="file"
        ref="file"
        v-on:change="onFileChange()"
      /><br />
      <v-btn type="submit">Publish</v-btn>
    </v-form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>
<script>
let SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;
let recognition = SpeechRecognition ? new SpeechRecognition() : false;
import { apiService } from "@/common/api.service.js";
import { imgurService } from "@/common/api.service.js";

export default {
  name: "PostEditor",
  created() {},
  props: {
    lang: {
      type: String,
      default: "en-US"
    },
    text: {
      type: [String, null],
      required: true
    },
    slug: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      error: null,
      speaking: false,
      toggle: false,
      runtimeTranscription: "",
      sentences: [],
      speech: null,
      post_body: null,
      file: null,
      url: null
    };
  },
  methods: {
    checkCompatibility() {
      if (!recognition) {
        this.error =
          "Speech Recognition is not available on this browser. Please use Chrome or Firefox";
      }
    },
    endSpeechRecognition() {
      recognition.stop();
      this.toggle = false;
      this.text = this.sentences.join(" ");
      this.speech = this.sentences.join(" ");
      this.$emit("speechend", {
        sentences: this.sentences,
        text: this.sentences.join(" ")
      });
    },
    startSpeechRecognition() {
      if (!recognition) {
        this.error =
          "Speech Recognition is not available on this browser. Please use Chrome or Firefox";
        return false;
      }
      this.toggle = true;
      recognition.lang = this.lang;
      recognition.interimResults = true;

      recognition.addEventListener("speechstart", () => {
        this.speaking = true;
      });

      recognition.addEventListener("speechend", () => {
        this.speaking = false;
      });

      recognition.addEventListener("result", event => {
        const text = Array.from(event.results)
          .map(result => result[0])
          .map(result => result.transcript)
          .join("");
        this.runtimeTranscription = text;
      });

      recognition.addEventListener("end", () => {
        if (this.runtimeTranscription !== "") {
          this.sentences.push(
            this.capitalizeFirstLetter(this.runtimeTranscription)
          );
          this.$emit(
            "update:text",
            `${this.text}${this.sentences.slice(-1)[0]}. `
          );
        }
        this.runtimeTranscription = "";
        recognition.stop();
        if (this.toggle) {
          // keep it going.
          recognition.start();
        }
      });
      recognition.start();
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
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
      } else if (!this.post_body && speech.length < 1) {
        this.error = "You can't send an empty post!";
      } else if (
        (this.post_body && this.post_body.length > 240) ||
        (speech && speech.length > 240)
      ) {
        this.error = "Ensure this field has no more than 240 characters!";
      } else if (!this.file) {
        this.error = "Please upload a picture or video to go with your post";
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
        imgur_data.append("image", this.file);
        imgur_data.append("title", new_content);
        imgur_data.append("type", "file");

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
  },
  mounted() {
    this.checkCompatibility();
  }
};
</script>

<style lang="scss" scoped></style>
