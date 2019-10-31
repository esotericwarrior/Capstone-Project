<template>
  <v-footer absolute color="primary lighten-1" padless>
    <v-row justify="center" no-gutters>
      <!-- Footer Links -->
      <v-btn
        v-for="link in links"
        :key="link.title"
        color="white"
        text
        :to="link.path"
        class="my-2"
      >
        {{ link.title }}
      </v-btn>
    </v-row>
  </v-footer>
</template>
<script>
export default {
  name: "Footer",
  data() {
    return {
      links: [
        {
          title: "Home",
          path: "/"
        },
        {
          title: "About",
          path: "/about"
        },
        {
          title: "Team",
          path: "/team"
        },
        {
          title: "Contact Us",
          path: "/support"
        }
      ]
    };
  }
};
</script>
<style lang="scss" scoped></style>
