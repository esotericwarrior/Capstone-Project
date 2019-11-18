<template>
  <v-container class="grey lighten-5">
    <v-row>
      <v-col cols="12" sm="6" offset-sm="3"> </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  name: "ProfilePictures",
  data() {
    return {
      dialog: false,
      fullscreen: false,
      isHovered: false,
      selectedImage: null
    };
  },
  methods: {
    closeZoom() {
      this.dialog = false;
      this.fullscreen = false;
    },
    openDialog(url) {
      this.dialog = !this.dialog;
      // eslint-disable-next-line no-console
      console.log(url);
      this.zoom(url);
    },
    zoom(url) {
      // eslint-disable-next-line no-console
      console.log("Zoom", url);
      this.selectedImage = url;
    }
  }
};
</script>
<style lang="scss" scoped></style>
