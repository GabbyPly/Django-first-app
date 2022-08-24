<template>
  <BlogPostList class="blog-post-list"> </BlogPostList>
</template>

<script>
/* 
This is an old comment and probably not true:
// Should see only his posts. For now this
// can be done in the front but this actually needs to get implemented in the server.
// Should /posts be only his posts, or /posts/me, or rather /posts/all are everyone's
*/

// import axios from "axios";
// const { api } = consts;
// import consts from "../consts";
import BlogPostList from "@/components/BlogPostList.vue";
export default {
  name: "BlogPostView",
  // props: { blogPostList: Array },
  methods: {
    logBlogContent(content) {
      // A different method called toggleDisplay should be called
      console.log("Blog post view log blog content");
      this.displayTitle = !this.displayTitle;
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
  created() {
    console.log("Created Lidor");
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
