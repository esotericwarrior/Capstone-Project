<template>
  <v-app>
    <TopMenu />
  </v-app>
</template>

<script>
import { TopMenu } from "@/components/Application/Navigation";

export default {
  name: "App",
  components: {
    TopMenu
  },
  data: () => ({
    //
  })
};
</script>
