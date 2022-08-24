<template>
  <v-app>
    <v-main>
      <div id="root">
        <Header />
        <nav>
          <router-link to="/home">Home</router-link> |
          <router-link to="/blog-post">Blog posts</router-link> |
          <router-link to="/create-post">Create a blog post</router-link> |
          <router-link to="/universities">Universities</router-link> |
          <router-link to="/about">About</router-link>
          <img
            style="margin-left: 1rem"
            alt="Vue logo"
            src="./assets/gabster-logo-small.png"
          />
        </nav>
        <router-view />
      </div>
    </v-main>
  </v-app>
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
  height: 90vh;
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
</style>
