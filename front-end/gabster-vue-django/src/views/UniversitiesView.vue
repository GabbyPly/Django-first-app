<template>
  <div class="home">
    <Button @isr-uni="loadUnis" />
    <UniversitiesList @delete-uny="deleteUny" :universities="unis" />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import Button from "../components/Button.vue";
import UniversitiesList from "../components/UniversitiesList.vue";

export default {
  name: "HomeView",
  methods: {
    loadUnis(allUnis) {
      this.$data.unis = allUnis;
    },
    deleteUny(unyToDelete) {
      confirm(`Are you sure you want to delete ${unyToDelete}?`);
      this.$data.unis = this.$data.unis.filter(
        (uny) => uny.name !== unyToDelete
      );
    },
  },
  components: {
    // HelloWorld,
    Button,
    UniversitiesList,
  },
  data() {
    return {
      unis: [],
    };
  },
};
</script>
