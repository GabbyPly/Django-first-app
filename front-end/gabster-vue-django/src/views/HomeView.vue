<template>
  <v-form ref="form" v-model="valid" lazy-validation>
    <v-text-field
      v-model="username"
      :rules="usernameRules"
      label="Username"
      required
    ></v-text-field>

    <v-col cols="12" sm="6">
      <v-text-field
        :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
        :type="show2 ? 'text' : 'password'"
        name="input-10-2"
        :rules="passwordRules"
        label="Password"
        hint="At least 6 characters"
        class="input-group--focused"
        @click:append="show2 = !show2"
      ></v-text-field>
    </v-col>
    <v-btn
      :disabled="!valid"
      color="success"
      class="log-in mr-4"
      @click="validate"
    >
      Log in
    </v-btn>

    <v-btn color="error" class="sign-up mr-4" @click="reset">
      <router-link to="/sign-up"> Don't have an account ? Sign-up </router-link>
    </v-btn>
  </v-form>
</template>

<script>
export default {
  data: () => ({
    username: "",
    show1: false,
    show2: true,
    valid: true,
    name: "",
    usernameRules: [
      (v) => {
        console.log("username values", v);
        return v.length > 0 || "Error";
      },
    ],
    password: "Password",
    passwordRules: [
      (value) => {
        console.log("value", value);
        return !!value || "Required.";
      },
      (v) => {
        console.log("v", v);
        return v.length >= 8 || "Min 6 characters";
      },
      // emailMatch: () => `The email and password you entered don't match`,
    ],
  }),

  methods: {
    validate() {
      this.$refs.form.validate();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
  },
};
</script>

<style scoped>
.log-in {
  color: green;
  width: 100vw !important;
}
.sign-up {
  display: flex;
  /* margin: 1rem; */
  /* justify-content: space-evenly; */
  width: 60vw !important;
}
</style>
