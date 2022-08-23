<template>
  <!-- <div class="blog-post"> -->
  <BlogPost
    v-for="blogPost in posts"
    :contentToDisplay="blogPost.title"
    :key="`id_${blogPost.id}`"
  />
  <!-- </div> -->
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
      console.log("listBlogPosts ~ response", response);
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
    // call the listBlogPosts function ?
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
