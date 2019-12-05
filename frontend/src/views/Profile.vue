<template>
  <div>
    <ProfileBanner :displayname="full_name" :username="username" />
    <profile-pictures />
  </div>
</template>
<script>
import { ProfileBanner } from "@/components/Application/Profile";
import { ProfilePictures } from "@/components/Application/Profile";

export default {
  name: "Profile",
  components: {
    ProfileBanner,
    ProfilePictures
  },
  props: {
    username: {
      type: String,
      required: true
    }
  },
  computed: {
    full_name: function() {
      return this.first_name + " " + this.last_name;
    }
  },
  data() {
    return {
      first_name: null,
      last_name: null
    };
  },
  methods: {
    getUser() {
      this.first_name = window.localStorage.getItem("first_name");
      this.last_name = window.localStorage.getItem("last_name");
    }
  },
  mounted() {
    this.getUser();
  }
};
</script>
<style lang="scss" scoped></style>
