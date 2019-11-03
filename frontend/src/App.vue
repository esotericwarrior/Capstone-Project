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
  methods: {
    async setUserInfo() {
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      window.localStorage.setItem("username", requestUser);
      // eslint-disable-next-line no-console
      console.log(data);
      // eslint-disable-next-line no-console
      console.log(requestUser);
    }
  }
};
</script>
