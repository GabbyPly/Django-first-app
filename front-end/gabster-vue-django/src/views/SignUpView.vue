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
    <v-col cols="12" sm="6">
      <v-text-field
        :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
        :type="show2 ? 'text' : 'password'"
        name="input-10-2"
        :rules="passwordRules"
        label="Confirm password"
        hint="At least 6 characters"
        class="input-group--focused"
        @click:append="show2 = !show2"
      ></v-text-field>
    </v-col>
    <v-btn
      :disabled="!valid"
      color="success"
      class="log-in mr-4"
      @click="
        validate();
        sendForm({ username, password });
      "
    >
      Submit
    </v-btn>
  </v-form>
</template>

<script>
import axios from "axios";
import consts from "../consts";
const { api } = consts;

export default {
  data: () => ({
    username: "",
    show1: false,
    show2: true,
    valid: true,
    name: "",
    usernameRules: [
      (v) => {
        return v.length > 0 || "Error";
      },
    ],
    password: "Password",
    passwordRules: [
      (value) => {
        return !!value || "Required.";
      },
      (v) => {
        return v.length >= 8 || "Min 6 characters";
      },
      // emailMatch: () => `The email and password you entered don't match`,
    ],
  }),

  methods: {
    async sendForm(data) {
      const { username, password } = data;
      const res = await axios.post(`${api}/contacts/`, {
        name: username,
        password,
      });
      console.log("sendForm ~ res", res);
      return res.data;
    },
    validate() {
      console.log("in validate");
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
/* .sign-up {
  display: flex;
  width: 100vw !important;
  justify-content: center !important;
} */
</style>
