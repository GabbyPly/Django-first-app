<template>
  <div></div>
</template>

<script>
import router from "../router";
export default {
  name: "LogOutView",
  methods: {},
  data: () => ({}),
  computed: {},
  created() {
    localStorage.removeItem("token");
    router.push("home");
  },
};
</script>

<style scoped></style>
