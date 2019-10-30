<template>
  <div>
    <!--Scrolling Toolbar -->
    <v-app-bar color="">
      <v-spacer></v-spacer>
      <v-btn class="ml-4" icon to="/">
        <font-awesome-icon icon="home" size="2x" />
      </v-btn>
      <v-divider class="mx-4" inset vertical></v-divider>
      <v-toolbar-title>
        <div class="pl-3">
          App Title / Logo
        </div>
      </v-toolbar-title>
      <v-text-field
        class="mx-3 pt-7"
        clearable
        @click:clear="clearSearch"
        color="primary"
        flat
        label="Search"
        solo-inverted
        v-model="search"
      >
        <template v-slot:append>
          <font-awesome-icon icon="search" size="lg" />
        </template>
      </v-text-field>
      <v-btn icon>
        <font-awesome-icon icon="bell" size="2x" />
      </v-btn>
      <v-btn icon>
        <font-awesome-icon icon="user-circle" size="2x" />
      </v-btn>
      <v-spacer></v-spacer>
    </v-app-bar>
  </div>
</template>
<script>
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

export default {
  name: "TopMenu",
  components: {
    FontAwesomeIcon
  },
  data: () => ({
    search: ""
  }),
  methods: {
    clearSearch() {
      this.search = "";
    }
  }
};
</script>
<style lang="scss" scoped></style>
