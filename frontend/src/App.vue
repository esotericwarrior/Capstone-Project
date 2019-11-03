<template>
  <v-app>
    <TopMenu />
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
import { apiService } from "@/common/api.service.js";
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
