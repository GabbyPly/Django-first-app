<template>
  <div
    class="margin uni"
    :key="`name_${uni.name}_site_${uni?.web_pages?.[0]}`"
    v-for="uni in universities"
  >
    <h3>{{ uni.name }}</h3>
    <i @click="deleteUny(uni.name)" class="fas fa-times"></i>
  </div>
</template>

<script>
export default {
  name: "UniversitiesList",
  emits: ["delete-uny"],
  methods: {
    deleteUny(uniName) {
      console.log(uniName, "- deleted");
      this.$emit("delete-uny", uniName);
    },
  },
  props: { universities: Array },
};
</script>

<style scoped>
template {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
i {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.fas {
  color: red;
}

.uni {
  display: flex;
  flex-wrap: wrap-reverse;
}

.margin {
  margin: 2rem;
}
</style>
