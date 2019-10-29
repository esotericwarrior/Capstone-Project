<template>
  <div>
    <v-toolbar color="">
      <v-spacer></v-spacer>
      <v-btn class="ml-4" icon to="/">
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <v-divider class="mx-4" inset vertical></v-divider>
      <v-toolbar-title>
        <div class="pl-3">
          App Title / Logo
        </div>
      </v-toolbar-title>
      <v-text-field
        append-icon="mdi-magnify"
        class="mx-3 pt-7"
        clearable
        @click:clear="clearSearch"
        color="primary"
        flat
        label="Search"
        solo-inverted
        v-model="search"
      >
      </v-text-field>
    </v-toolbar>
  </div>
</template>
<script>
export default {
  name: "TopMenu",
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
