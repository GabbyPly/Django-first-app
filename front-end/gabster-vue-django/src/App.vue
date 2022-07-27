<template>
  <v-app>
    <v-main>
      <div id="root">
        <h1>Hello World - later changed to Header component</h1>
        <nav>
          <router-link to="/home">Home</router-link> |
          <router-link to="/blog-post">Blog posts</router-link> |
          <router-link to="/universities">Universities</router-link> |
          <router-link to="/about">About</router-link>
          <img alt="Vue logo" src="./assets/logo.png" />
        </nav>
        <router-view />
      </div>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",
  // data() {
  //   return {}; // Should all components have data ? or is in not mandatory
  // },
};
</script>

<style>
* {
  /* background-color: rosybrown; */
}

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
