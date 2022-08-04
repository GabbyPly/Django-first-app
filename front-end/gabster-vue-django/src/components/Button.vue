<template>
  <button @click="getUniversities" class="btn">
    Click me to get universities
  </button>
</template>

<script>
import axios from "axios";
export default {
  name: "BasicButton",
  methods: {
    async getUniversities() {
      console.log(process.env.SERVER_PORT);
      const ax = await axios.get(`/contacts`);
      console.log("getUniversities ~ ax", ax);
      const res = await axios.get(
        "http://universities.hipolabs.com/search?country=Israel"
      );
      this.$emit("isr-uni", res.data);
    },
  },
  components: {},
  data() {
    return {};
  },
};
</script>

<style>
.btn {
  font-size: 3rem;
  margin: 1rem;
  background-color: green;
  /* color: red; */
  /* border-color: white; */
  border-radius: 2rem;
  border-block: 1rem;
}
</style>
