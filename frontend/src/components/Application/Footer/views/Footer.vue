<template>
  <v-footer absolute color="primary lighten-1" padless> </v-footer>
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
