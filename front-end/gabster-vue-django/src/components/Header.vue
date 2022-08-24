<template>
  <v-toolbar dark color="#168830" style="height: 10vh">
    <v-toolbar-title class="white--text">
      <div class="mamae">
        <!-- <img class="logo" src="./gabster-logo.jpeg" width="50px" /> -->
      </div>
    </v-toolbar-title>

    <v-toolbar-items>
      <v-btn flat>Encontre</v-btn>
      <v-btn flat>publique</v-btn>
      <v-btn flat>sobre</v-btn>
    </v-toolbar-items>

    <v-spacer></v-spacer>

    <!-- <v-layout row align-center style="max-width: 30vw; min-width: 1vw">
      <v-text-field
        solo
        placeholder="Pesquisar..."
        single-line
        append-icon="search"
        background-color="#202d3f"
        color="white"
        hide-details
      ></v-text-field>
    </v-layout> -->
  </v-toolbar>
</template>
e
<script>
export default {
  name: "HeaderComponent",
  data() {
    return {};
  },
};
</script>

<style></style>
