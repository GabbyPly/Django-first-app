<template>
  <BlogPost
    v-for="blogPost in posts"
    :blogPost="blogPost"
    :key="`id_${blogPost.id}`"
  />
</template>

<script>
import axios from "axios";
const { api } = consts;
import consts from "../consts";
import BlogPost from "./BlogPost.vue";
export default {
  name: "BlogPostList",
  //   props: { list: Array },
  methods: {
    async listBlogPosts() {
      const response = await axios.get(`${api}/posts`, {
        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
      });
      this.posts = response.data.posts;
    },
    displayBlogPost() {
      return;
    },
  },
  components: { BlogPost },
  data() {
    return { posts: [] };
  },
  created() {
    console.log("blog post list created");
    this.listBlogPosts();
  },
};
</script>

<style scoped></style>
