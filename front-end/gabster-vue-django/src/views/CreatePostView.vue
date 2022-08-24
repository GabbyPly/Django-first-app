<template>
  <v-form class="form" v-model="valid">
    <v-container>
      <v-row>
        <v-col cols="12" md="4">
          <v-text-field
            v-model="PostTitle"
            :rules="titleRules"
            :counter="10"
            label="Post title"
            required
          ></v-text-field>
        </v-col>

        <v-col cols="12" md="12">
          <v-text-field
            class="post-content"
            v-model="postContent"
            :rules="postRules"
            :counter="1000"
            label="Post content"
            required
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
  <v-btn @click="createPost" class="post-btn">Post</v-btn>
</template>
<script>
import axios from "axios";
import consts from "../consts";
const { api } = consts;
export default {
  name: "CreatePost",
  data: () => ({
    valid: false,
    PostTitle: "",
    postContent: "",
    titleRules: [
      (v) => !!v || "Title is required",
      (v) => v.length <= 10 || "Title must be less than 10 characters",
    ],
    email: "",
    postRules: [
      (v) => !!v || "Post body is required",
      (v) => v.length <= 1000 || "Post body must be less than 10 characters",
    ],
  }),
  methods: {
    async createPost() {
      const token = localStorage.getItem("token");
      const body = {
        title: this.PostTitle,
        content: this.postContent,
      };

      /* const { data: post } = */ await axios.post(`${api}/posts/`, body, {
        headers: { Authorization: `Bearer ${token}` },
      });
      this.PostTitle = "";
      this.postContent = "";
    },
  },
};
</script>

<style scoped>
.post-btn {
  background-color: green;
  margin-left: 50vw;
}
</style>
