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
              <v-container fluid>
                <v-row>
                  <v-col
                    v-for="n in 9"
                    :key="n"
                    class="d-flex child-flex"
                    cols="4"
                  >
                    <v-card flat tile class="d-flex">
                      <v-img
                        @click="
                          openDialog(
                            `https://picsum.photos/500/300?image=${n * 5 + 10}`
                          )
                        "
                        :src="
                          `https://picsum.photos/500/300?image=${n * 5 + 10}`
                        "
                        :lazy-src="
                          `https://picsum.photos/10/6?image=${n * 5 + 10}`
                        "
                        aspect-ratio="1"
                        class="grey lighten-2"
                      >
                        <template v-slot:placeholder>
                          <v-row
                            class="fill-height ma-0"
                            align="center"
                            justify="center"
                          >
                            <v-progress-circular
                              indeterminate
                              color="grey lighten-5"
                            ></v-progress-circular>
                          </v-row>
                        </template>
                      </v-img>
                    </v-card>
                  </v-col>
                </v-row>
              </v-container>
            </v-card>
          </v-tab-item>

          <!-- Favorites -->
          <v-tab-item>
            <v-card color="grey lighten-5" flat tile>
              <v-container fluid>
                <v-row>
                  <v-col
                    v-for="n in 9"
                    :key="n"
                    class="d-flex child-flex"
                    cols="4"
                  >
                    <v-card flat tile class="d-flex">
                      <v-img
                        :src="
                          `https://picsum.photos/500/300?image=${n * 6 + 15}`
                        "
                        :lazy-src="
                          `https://picsum.photos/10/6?image=${n * 6 + 15}`
                        "
                        aspect-ratio="1"
                        class="grey lighten-2"
                      >
                        <template v-slot:placeholder>
                          <v-row
                            class="fill-height ma-0"
                            align="center"
                            justify="center"
                          >
                            <v-progress-circular
                              indeterminate
                              color="grey lighten-5"
                            ></v-progress-circular>
                          </v-row>
                        </template>
                      </v-img>
                    </v-card>
                  </v-col>
                </v-row>
              </v-container>
            </v-card>
          </v-tab-item>
        </v-tabs>

        <!-- Posts Dialog -->
        <v-dialog v-model="dialog" :fullscreen="fullscreen"> </v-dialog>
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
