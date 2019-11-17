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
  data() {
    return {
      first_name: null,
      last_name: null
    };
  }
};
</script>
<style lang="scss" scoped></style>
