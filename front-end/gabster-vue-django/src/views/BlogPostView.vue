<template>
  <v-container class="blog-post-list" v-model="postContent">
    <div class="blog-post" :key="`id_${blogPost.id}`" v-for="blogPost in posts">
      <h3>{{ blogPost.title }}</h3>
      <v-btn @click="logBlogContent(blogPost.content)">Soem</v-btn>
    </div></v-container
  >
  <!-- <v-container>This is blogPostList from data {{ username }}</v-container> -->
</template>
<script>
// Should see only his posts. For now this
// can be done in the front but this actually needs to get implemented in the server.
// Should /posts be only his posts, or /posts/me, or rather /posts/all are everyone's

import axios from "axios";
import consts from "../consts";
const { api } = consts;
export default {
  name: "BlogPost",
  props: { blogPostList: Array }, // Currently isn't passed
  methods: {
    async listBlogPosts() {
      const response = await axios.get(`${api}/posts`, {
        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
      });
      this.posts = response.data.posts;
    },
    logBlogContent(content) {
      this.PostLists[0].val++;
      console.log({ content });
    },
  },
  data: () => ({
    PostTitle: "",
    PostLists: [{ key: "gabster", val: 123 }],
    posts: [],
  }),
  computed: {
    username() {
      return this.PostLists[0].val;
    },
  },
  created() {
    console.log("init ");
    this.listBlogPosts();
  },
};
</script>

<style scoped>
.blog-post {
  display: flex;
  justify-content: center;
  align-items: center;
}

.blog-post-title {
  margin: 1rem;
}

.read-btn {
  margin: 1rem;
}

.post-btn {
  background-color: green;
}
</style>
