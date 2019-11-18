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
        <v-dialog v-model="dialog" :fullscreen="fullscreen">
          <v-card color="grey lighten-5" max-height="900">
            <v-container>
              <v-row justify="center" no-gutters>
                <v-col cols="12">
                  <v-row>
                    <v-col cols="8">
                      <v-img
                        :src="selectedImage"
                        width="100%"
                        @mouseover="isHovered = true"
                        @mouseleave="isHovered = false"
                      >
                        <v-row justify="start" class="fill-height">
                          <v-col cols="10">
                            <div v-if="isHovered">
                              <v-btn
                                large
                                color="primary"
                                icon
                                absolute
                                top
                                left
                                dark
                                @click="closeZoom"
                              >
                                <v-icon></v-icon>
                                <slot>
                                  <font-awesome-icon icon="times" size="lg" />
                                </slot>
                              </v-btn>
                              <v-btn
                                icon
                                absolute
                                top
                                right
                                dark
                                color="primary"
                                @click="fullscreen = !fullscreen"
                              >
                                <v-icon></v-icon>
                              </v-btn>
                            </div>
                          </v-col>
                        </v-row>
                      </v-img>
                    </v-col>
                    <v-col cols="4">
                      <v-card flat class="grey lighten-5">
                        <v-list-item class="pa-5">
                          <v-list-item-avatar color="grey"></v-list-item-avatar>
                          <v-list-item-content>
                            <v-list-item-title class="headline"
                              ><strong>Username</strong></v-list-item-title
                            >
                          </v-list-item-content>
                          <v-card-actions>
                            <v-btn icon>
                              <v-icon>mdi-pen</v-icon>
                            </v-btn>
                          </v-card-actions>
                        </v-list-item>
                        <v-divider></v-divider>
                        <v-list-item class="pa-5">
                          <v-list-item-avatar color="grey"></v-list-item-avatar>
                          <v-list-item-content>
                            <v-list-item-title
                              ><strong>Username</strong> Post
                              content</v-list-item-title
                            >
                          </v-list-item-content>
                        </v-list-item>
                      </v-card>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
//import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

export default {
  name: "ProfilePictures",
  components: {
    //FontAwesomeIcon
  },
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
