<template>
  <div>
    <v-toolbar color="">
      <v-spacer></v-spacer>
      <v-btn class="ml-4" icon to="/">
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <v-divider class="mx-4" inset vertical></v-divider>
    </v-toolbar>
  </div>
</template>
<script>
export default {
  name: "TopMenu",
  data: () => ({})
};
</script>
<style lang="scss" scoped></style>
