<!-- <v-btn @click="listBlogPosts">click</v-btn> -->
<!-- v-model="postContent" Is a former attribute of the v-container-->
<template>
  <!-- <div class="blog-post-list"> -->
  <BlogPostList class="blog-post-list"> </BlogPostList>
  <!-- </div> -->
  <!-- <BlogPost
      :contentToDisplay="blogPost.title"
      :key="`id_${blogPost.id}`"
      v-for="blogPost in posts"
    /> -->
  <!-- <div class="blog-post" :key="`id_${blogPost.id}`" v-for="blogPost in posts">
      <h3 class="blog-post-title">
        {{ displayBlogPost(blogPost) || blogPost.title }}
      </h3>
      <v-btn class="read-btn" @click="logBlogContent(blogPost.content)"
        >Read</v-btn
      ></div> -->
</template>
<script>
// Should see only his posts. For now this
// can be done in the front but this actually needs to get implemented in the server.
// Should /posts be only his posts, or /posts/me, or rather /posts/all are everyone's

import axios from "axios";
import consts from "../consts";
import BlogPostList from "@/components/BlogPostList.vue";
const { api } = consts;
export default {
  name: "BlogPost",
  // props: { blogPostList: Array },
  methods: {
    async listBlogPosts() {
      const response = await axios.get(`${api}/posts`, {
        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
      });
      console.log("listBlogPosts ~ response", response);
      this.posts = response.data.posts;
    },
    logBlogContent(content) {
      console.log({ content });
      // A different method called toggleDisplay should be called
      this.displayTitle = !this.displayTitle;
      console.log("something", this.something);
    },
    displayBlogPost(blogPost) {
      console.log("displayBlogPost ~ blogPost", blogPost);
      return this.displayTitle ? blogPost.title : blogPost.content;
    },
  },
  data: () => ({
    PostTitle: "",
    PostLists: [{ key: "gabster", val: 123 }],
    posts: [],
    displayTitle: true,
    // something: this.posts.map((x) => ({ ...x, con: "con" })),
  }),
  computed: {
    username() {
      return this.PostLists[0].val;
    },
  },
  beforeMount() {
    console.log("init  blog post view");
    // this.listBlogPosts();
  },
  components: { BlogPostList },
};
</script>

<style scoped>
.blog-post-list {
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
