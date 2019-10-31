<template>
  <v-container fluid fill-height align="center" justify="center">
    <v-row align="center" justify="center" no-gutters>
      <v-col align="center" justify="center" cols="12">
        <h1>Contact Us</h1>
        Remember to check out our tutorial videos for guided help.
      </v-col>
      <v-col align="center" justify="center" cols="12">
        For all other questions, please feel free to ask!
        <!-- Horizontal Divider -->
        <v-col cols="4"><v-divider class="my-4"/></v-col>
      </v-col>
      <v-col cols="12">
        <v-card class="mx-auto grey lighten-5" max-width="500" flat>
          <v-card-title class="headline justify-center">
            What can we do to help?
          </v-card-title>
          <!-- Contact Us Form -->
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="name"
              :counter="30"
              :rules="nameRules"
              label="Name"
              required
            ></v-text-field>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
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
  },
  methods: {
    reset() {
      this.$refs.form.reset();
    },
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        this.formSubmitted = true;
        this.submitResult = "Thanks! We'll be in touch!";
        this.reset();
      }
    }
  }
};
</script>
<style lang="scss" scoped></style>
