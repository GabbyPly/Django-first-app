<template>
  <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
  <div id="root">
    <img alt="Vue logo" src="./assets/logo.png" />
    <h1>Hello World</h1>
    <Button @isr-uni="loadUnis" />
    <UniversitiesList :universities="unis" />
  </div>
</template>

<script>
// import HelloWorld from "./components/HelloWorld.vue";
import Button from "./components/Button.vue";
import UniversitiesList from "./components/UniversitiesList.vue";

export default {
  name: "App",
  methods: {
    loadUnis(data) {
      this.$data.unis = data;
    },
  },
  components: {
    // HelloWorld,
    Button,
    UniversitiesList,
  },
  data() {
    return {
      unis: [],
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
