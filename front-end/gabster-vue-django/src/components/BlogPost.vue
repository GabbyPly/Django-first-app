<template>
  <div class="blog-post-list">
    <h3 class="blog-post-title">
      {{ contentToDisplay || displayBlogPost(blogPost) || blogPost.title }}
    </h3>
    <v-btn class="read-btn" @click="logBlogContent(blogPost.content)"
      >Read</v-btn
    >
  </div>
</template>

<script>
// import axios from "axios";
// import consts from "../consts";
// const { api } = consts;
export default {
  name: "BlogPost",
  props: { contentToDisplay: String },
  methods: {
    toggleDisplay() {
      this.displayTitle = !this.displayTitle;
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
  components: {},
  data() {
    return {
      displayTitle: true,
    };
  },
  created() {
    console.log("init blogPost component");
    // this.listBlogPosts();
  },
};
</script>

<style scoped>
.blog-post-list {
  display: flex;
  justify-content: center;
  align-items: center;
}
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
