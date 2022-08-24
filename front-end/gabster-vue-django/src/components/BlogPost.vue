<template>
  <div class="blog-post">
    <h3 class="blog-post-title">
      {{ contentToDisplay }}
    </h3>
    <v-btn class="read-btn" @click="toggleDisplay">{{ ReadBtnState }}</v-btn>
    <h5>By {{ blogPost.author_username }}</h5>
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
  },
  components: {},
  data() {
    return {
      displayTitle: true,
    };
  },
  created() {
    console.log("init blogPost component");
  },
  computed: {
    contentToDisplay() {
      return this.displayTitle ? this.blogPost.title : this.blogPost.content;
    },
    ReadBtnState() {
      return this.displayTitle ? "Read whole story" : "Show blog post title";
    },
  },
};
</script>

<style scoped>
.blog-post {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  margin: 1rem;
  border: solid;
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
