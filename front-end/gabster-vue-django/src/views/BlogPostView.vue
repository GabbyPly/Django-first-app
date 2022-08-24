<template>
  <BlogPostList></BlogPostList>
</template>

<script>
/* 
Implement a 'Written by' text in the front
*/

import BlogPostList from "@/components/BlogPostList.vue";
export default {
  name: "BlogPostView",
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
    PostLists: [], // Not in use
    displayTitle: true, // Should pass to child components
  }),
  computed: {
    username() {
      return this.PostLists[0].val; // Not in use
    },
  },
  created() {
    console.log("Created Lidor (Blog post view)");
  },
  components: { BlogPostList },
};
</script>

<style scoped></style>
