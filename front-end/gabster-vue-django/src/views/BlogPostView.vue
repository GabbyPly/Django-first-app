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
  <v-btn class="post-btn">Post</v-btn>
</template>
<script>
export default {
  name: "BlogPost",
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
};
</script>

<style scoped>
template {
  /* align-content: center; */
  /* display: flex;
  justify-content: center; */
}
.post-content {
}
.post-btn {
  background-color: green;
}
</style>
