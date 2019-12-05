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
    
    <video id="webcam-stream" autoplay muted style="display:none"></video>
    <button id="screenshot-button" @click="takePicture" style="display:none">
      Take Picture
    </button>
    <button id="record-button" @click="recordVideo" style="display:none">
      Record Video
    </button>
    <img src="" />
    <canvas style="display:none;"></canvas>
    <video id="playback-video" style="display:none" controls></video>
    <button id="save-media-button" @click="saveMedia" style="display:none">
      Add Media To Post
    </button>
    <button id="discard-media-button" @click="discardMedia" style="display:none">
      Discard Media
    </button>
    <button id="stop-recording-button" style="display:none">
      Stop Recording
    </button>
    <a id="download" style="display:none">Download</a>

    <v-flex xs2 sm1 text-xs-center>
      <v-btn
        dark
        @click.stop="mediaToggle ? stopMediaStream() : startMediaStream()"
        icon
        :color="!mediaToggle ? 'grey' : speaking ? 'red' : 'red darken-3'"
        :class="{ 'animated infinite pulse': mediaToggle }"
      >
        <v-icon>{{
          mediaToggle ? "Stop Mediastream" : "Start Mediastream"
        }}</v-icon>
      </v-btn>
    </v-flex>
    
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
      mediaToggle: false,
      speaking: false,
      toggle: false,
      runtimeTranscription: "",
      sentences: null,
      speech: null,
      post_body: "",
      file: null,
      text: "",
      snackbar: false,
      url: null,
      video: null,
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
      if((this.$refs.file.files[0].type.includes("image") && (this.$refs.file.files[0].type.includes("jpeg") || this.$refs.file.files[0].type.includes("gif") || this.$refs.file.files[0].type.includes("tiff") || this.$refs.file.files[0].type.includes("apng") || this.$refs.file.files[0].type.includes("png"))) || (this.$refs.file.files[0].type.includes("video"))){
        this.file = this.$refs.file.files[0];
      }
      else{
        this.error = "File type not supported. File will not be uploaded. Please choose another file.";
        this.snackbar = true;
      }
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
      } else if (!this.post_body && (speech && speech.length < 1)) {
        this.error = "You can't send an empty post!";
      } else if (
        (this.post_body && this.post_body.length > 240) ||
        (speech && speech.length > 240)
      ) {
        this.error = "Ensure this field has no more than 240 characters!";
        this.snackbar = true;
      } else if (this.file.type && this.file.type.includes("video")) {

        let endpoint = "/upload/video/";
        let method = "POST";
        new_content = this.post_body;

        let video_data = new FormData();
        video_data.append("video", this.file);
        video_data.append("content", new_content);
        // eslint-disable-next-line no-console
        console.log(Array.from(video_data));

        apiService(endpoint, method, video_data).then(response => {
          // eslint-disable-next-line no-console
          video_data.append("url", response.data);
          // eslint-disable-next-line no-console
          console.log(video_data.get("url"));

          apiService("/api/posts/", "POST", video_data).then(post_data => {
            this.$router.push({
              name: "post",
              params: { slug: post_data.data.slug }
            });
          });
        });
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
          method = "PATCH";
        }
        if (this.file != null){
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
        else{
           let data = new FormData();
           data.append("content", new_content);
       	   apiService(endpoint, method, data).then(post_data => {
           this.$router.push({
              name: "post",
              params: { slug: post_data.data.slug }
            });
          });
        }

      }
    },
    checkMediaCompatibility() {
      if (!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia)) {
        this.error = "mediastream not supported";
      } 
    },
    startMediaStream() {
      const constraints = {
        video: true,
        audio: true
      };
      const video = document.querySelector("#webcam-stream");
      this.mediaToggle = true;

      navigator.mediaDevices.getUserMedia(constraints).then(stream => {
        video.srcObject = stream;
      });

      video.style.display = "inline";
      const screenshotButton = document.querySelector("#screenshot-button");
      screenshotButton.style.display = "block";
      const recordButton = document.querySelector("#record-button");
      recordButton.style.display = "block";
    },
    stopMediaStream() {
      const video = document.querySelector("#webcam-stream");
      video.srcObject.getVideoTracks().forEach(track => track.stop());
      video.srcObject.getAudioTracks().forEach(track => track.stop());
      video.srcObject = null;
      video.style.display = "none";
      const screenshotButton = document.querySelector("#screenshot-button");
      screenshotButton.style.display = "none";
      const recordButton = document.querySelector("#record-button");
      recordButton.style.display = "none";
      this.mediaToggle = false;
    },
    takePicture() {
      const video = document.querySelector("#webcam-stream");
      const canvas = document.querySelector("canvas");
      const img = document.querySelector("img");
      const saveMediaButton = document.querySelector("#save-media-button");
      const discardMediaButton = document.querySelector(
        "#discard-media-button"
      );
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext("2d").drawImage(video, 0, 0);
      img.src = canvas.toDataURL("image/png");
      saveMediaButton.style.display = "block";
      discardMediaButton.style.display = "block";
    },
    recordVideo() {
      let _this = this;
      const video = document.querySelector("#webcam-stream");
      const stream = video.srcObject;
      const stopButton = document.querySelector("#stop-recording-button");
      const downloadLink = document.querySelector("#download");
      const options = { mimeType: "video/webm" };
      const recordedChunks = [];
      const mediaRecorder = new MediaRecorder(stream, options);
      const screenshotButton = document.querySelector("#screenshot-button");
      const recordButton = document.querySelector("#record-button");

      screenshotButton.style.display = "none";
      recordButton.style.display = "none";
      stopButton.style.display = "block";

      stopButton.addEventListener("click", function() {
        stopButton.style.display = "none";
        _this.stopMediaStream();
        mediaRecorder.stop()
      });

      mediaRecorder.addEventListener("dataavailable", function(e) {
        if (e.data.size > 0) {
          recordedChunks.push(e.data);
        }
      });

      mediaRecorder.addEventListener("stop", function() {
        downloadLink.style.display = "block";
        
        var blob = new Blob(recordedChunks);
        _this.file = new File([blob], "video.webm", { type: "video/webm", lastModified: Date.now() });

        downloadLink.href = URL.createObjectURL(blob);
        downloadLink.download = "video.webm";
        const playback_video = document.querySelector("#playback-video");
        const discardMediaButton = document.querySelector("#discard-media-button");
        playback_video.src = downloadLink.href;
        playback_video.style.display = "block";
        discardMediaButton.style.display = "block";
        playback_video.load();

      });

      mediaRecorder.start();
    },
    saveMedia() {
      const img = document.querySelector("img");
      var str = img.src;
      var new_str = str.replace("data:image/png;base64,","");
      this.file = new_str;
    },
    discardMedia() {
      const img = document.querySelector("img");
      const video = document.querySelector("#playback-video");
      const saveMediaButton = document.querySelector("#save-media-button");
      const discardMediaButton = document.querySelector(
        "#discard-media-button"
      );
      const downloadLink = document.querySelector("#download");
      img.src = "";
      video.style.display = "none";
      saveMediaButton.style.display = "none";
      discardMediaButton.style.display = "none";
      downloadLink.style.display = "none";

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
    this.checkMediaCompatibility();
  }
};
</script>

<style lang="scss" scoped></style>
