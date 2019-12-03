<template>
  <v-container>
    <v-row>
      <v-col>
        <span>{{ runtimeTranscription }}</span>
        <v-btn
          dark
          @click.stop="
            toggle ? endSpeechRecognition() : startSpeechRecognition()
          "
          icon
          :color="!toggle ? 'grey' : speaking ? 'red' : 'red darken-3'"
          :class="{ 'animated infinite pulse': toggle }"
        >
          <div v-if="toggle">
            <font-awesome-icon icon="microphone" size="2x" />
          </div>
          <div v-else>
            <font-awesome-icon icon="microphone-slash" size="2x" />
          </div>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
let SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;
let recognition = SpeechRecognition ? new SpeechRecognition() : false;

export default {
  name: "SpeechToText",
  props: {
    lang: {
      type: String,
      default: "en-US"
    },
    text: {
      type: [String, null],
      required: true
    }
  },
  data() {
    return {
      error: false,
      runtimeTranscription: "",
      sentences: [],
      speaking: false,
      toggle: false
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
      this.$emit("speechend", {
        sentences: this.sentences,
        text: this.sentences.join(". ")
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
      /* eslint-disable no-unused-vars */
      recognition.addEventListener("speechstart", event => {
        this.speaking = true;
      });

      recognition.addEventListener("speechend", event => {
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
      /* eslint-disable no-unused-vars */
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    }
  },
  mounted() {
    this.checkCompatibility();
  }
};
</script>
<style lang="scss" scoped></style>
