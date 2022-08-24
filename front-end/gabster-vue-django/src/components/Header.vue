<template>
  <nav>
    <router-link to="/home">Home</router-link> |
    <router-link to="/blog-post">Blog posts</router-link> |
    <router-link to="/create-post">Create a blog post</router-link> |
    <router-link to="/universities">Universities</router-link> |
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
