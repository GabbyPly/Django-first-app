<template>
  <div
    :key="`name_${uni.name}_site_${uni?.web_pages?.[0]}`"
    v-for="uni in universities"
  >
    <h3>{{ uni.name }}</h3>
  </div>
</template>

<script>
export default {
  name: "UniversitiesList",
  methods: {},
  props: { universities: Array },
  // data() {
  //   return {this.universities};
  // },
};
</script>

<style scoped></style>
