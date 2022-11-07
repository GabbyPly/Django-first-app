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
  methods: {},
  data: () => ({}),
  computed: {},
  created() {
    console.log("Created Lidor (Blog post view)");
  },
  components: { BlogPostList },
};
</script>

<style scoped></style>
