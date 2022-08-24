<template>
  <v-app>
    <v-main>
      <div id="root">
        <Header />
      </div>
    </v-main>
  </v-app>
  <footer>
    <img alt="Gabster logo" src="./assets/gabster-logo-small.png" />
  </footer>
</template>

<script>
import Header from "./components/Header.vue";
export default {
  name: "App",
  // data() {
  //   return {}; // Should all components have data ? or is in not mandatory
  // },
  components: { Header },
};
</script>

<style>
#root {
  /* background-color: darksalmon; */
  /* height: 90vh; */
  min-height: 100vh;
}

footer {
  margin-top: 1rem;
  /* background-color: darkseagreen; */
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
footer {
  margin-top: auto;
}
</style>
