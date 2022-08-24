<template>
  <div class="blog-post-list">
    <h3 class="blog-post-title">
      {{ contentToDisplay }}
    </h3>
    <v-btn class="read-btn" @click="logBlogContent(blogPost.content)">{{
      ReadBtnState
    }}</v-btn>
  </div>
</template>

<script>
export default {
  name: "BlogPost",
  props: { blogPost: Object },
  methods: {
    toggleDisplay() {
      this.displayTitle = !this.displayTitle;
    },
    logBlogContent(content) {
      // A different method called toggleDisplay should be called
      console.log("log blog content", this.something);
      this.displayTitle = !this.displayTitle;
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
  computed: {
    contentToDisplay() {
      return this.displayTitle ? this.blogPost.title : this.blogPost.content;
    },
    ReadBtnState() {
      return this.displayTitle ? "Read" : "Show blog post title";
    },
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
