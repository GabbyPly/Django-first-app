<template>
  <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
  <div id="root">
    <img alt="Vue logo" src="./assets/logo.png" />
    <h1>Hello World</h1>
    <Button @isr-uni="loadUnis" />
    <UniversitiesList @delete-uny="deleteUny" :universities="unis" />
  </div>
</template>

<script>
// import HelloWorld from "./components/HelloWorld.vue";
import Button from "./components/Button.vue";
import UniversitiesList from "./components/UniversitiesList.vue";

export default {
  name: "App",
  methods: {
    loadUnis(allUnis) {
      this.$data.unis = allUnis;
    },
    deleteUny(unyToDelete) {
      confirm(`Are you sure you want to delete ${unyToDelete}?`);
      this.$data.unis = this.$data.unis.filter(
        (uny) => uny.name !== unyToDelete
      );
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
/* /* import the fontawesome core */ import { library } from
'@fortawesome/fontawesome-svg-core' /* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome' /* import
specific icons */ import { faUserSecret } from
'@fortawesome/free-solid-svg-icons' /* add icons to the library */
library.add(faUserSecret) createApp(App) .component('font-awesome-icon',
FontAwesomeIcon) .mount('#app') */
