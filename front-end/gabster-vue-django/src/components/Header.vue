<template>
  <nav>
    <router-link to="/home">Home</router-link> |
    <router-link to="/blog-post">Blog posts</router-link> |
    <router-link to="/create-post">Create a blog post</router-link> |
    <router-link to="/universities">Universities</router-link> |
    <router-link to="/log-out">Log out</router-link> |
    <!-- The log out view could also just be removed and subbed with a method that removes token and redirects to "/home" -->
    <router-link to="/about">About</router-link>
  </nav>
  <router-view />
</template>
e
<script>
export default {
  name: "HeaderComponent",
  data() {
    return {};
  },
};
</script>

<style></style>
