<template>
  <v-container class="blog-post-list" v-model="postContent">
    <div
      class="blog-post"
      :key="`id_${blogPost.id}`"
      v-for="blogPost in computedBlogPostList"
    >
      <h3>{{ blogPost.title }}</h3>
      <v-btn @click="logBlogContent(blogPost.content)">Soem</v-btn>
    </div></v-container
  >
  <!-- <v-container>This is blogPostList from data {{ username }}</v-container> -->
</template>
<script>
import axios from "axios";
import consts from "../consts";
const { api } = consts;
console.log(localStorage);
export default {
  name: "BlogPost",
  props: { blogPostList: Array }, // Currently isn't passed
  methods: {
    async computedBlogPostList() {
      localStorage.setItem("token", "0a022e3ab35ddfa5a1ed6c900a3491822dec6d66");
      const response = await axios.get(`${api}/posts`, {
        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
      });
      console.log("resp", response);
      this.results = response.results;
    },
    logBlogContent(content) {
      this.PostLists[0].val++;
      console.log({ content });
    },
  },
  data: () => ({
    PostTitle: "",
    PostLists: [{ key: "gabster", val: 123 }],
    BlogPostList: [
      // {
      //   id: 123,
      //   title: "My hardcoded title",
      //   content: "Content isn't supposed to be hardcoded eh",
      // },
    ],
    results: [],
  }),
  computed: {
    username() {
      return this.PostLists[0].val;
    },
  },
  created() {
    console.log("init ");
    this.computedBlogPostList();
  },
};
</script>

<style scoped>
template {
  /* align-content: center; */
  /* display: flex;
  justify-content: center; */
}
.post-content {
  /* pass */
}
.post-btn {
  background-color: green;
}
</style>
