<template>
  <v-container class="grey lighten-5">
    <v-row>
      <v-col cols="12" sm="6" offset-sm="3">
        <!-- Tabs -->
        <v-tabs
          background-color="grey lighten-5"
          color="blue accent-4"
          fixed-tabs
        >
          <v-tab>My Posts</v-tab>
          <v-tab>Favorites</v-tab>

          <!-- Posts -->
          <v-tab-item>
            <v-card color="grey lighten-5" flat tile>
              <v-container fluid> </v-container>
            </v-card>
          </v-tab-item>
        </v-tabs>
      </v-col>
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
