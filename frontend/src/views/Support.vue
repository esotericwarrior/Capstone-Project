<template>
  <div id="support"></div>
</template>
<script>
export default {
  name: "Support",
  data() {
    return {
      email: "",
      message: "",
      name: "",
      rules: {
        required: value => !!value || "Required.",
        counter: value => value.length <= 30 || "Max 30 characters",
        email: value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || "Invalid e-mail.";
        }
      }
    };
  }
};
</script>
<style lang="scss" scoped></style>
