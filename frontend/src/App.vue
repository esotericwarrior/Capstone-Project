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
  created() {
    this.setUserInfo();
  },
  methods: {
    async setUserInfo() {
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      const first_name = data["first_name"];
      const last_name = data["last_name"];
      window.localStorage.setItem("username", requestUser);
      window.localStorage.setItem("first_name", first_name);
      window.localStorage.setItem("last_name", last_name);
      // eslint-disable-next-line no-console
      console.log(data);
      // eslint-disable-next-line no-console
      console.log(requestUser);
    }
  }
};
</script>
