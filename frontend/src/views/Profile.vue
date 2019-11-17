<template>
  <div></div>
</template>
<script>
export default {
  name: "Profile",
  props: {
    username: {
      type: String,
      required: true
    }
  },
  computed: {},
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
