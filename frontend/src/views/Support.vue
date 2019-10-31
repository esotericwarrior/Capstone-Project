<template>
  <div id="support"></div>
</template>
<script>
export default {
  name: "Support",
  data() {
    return {
      formSubmitted: false,
      email: "",
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+\..+/.test(v) || "E-mail must be valid"
      ],
      message: "",
      name: "",
      nameRules: [
        v => !!v || "Name is required",
        v => (v && v.length <= 30) || "Name must be less than 30 characters"
      ],
      snackbar: false,
      submitResult: "",
      timeout: 3000,
      valid: true
    };
  }
};
</script>
<style lang="scss" scoped></style>
