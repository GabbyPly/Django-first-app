<template>
  <div class="count">
    <button @click="increaseCounter">Click me to increase</button>
    <button @click="decreaseCounter">Click me to decrease</button>
    <h3>The count is {{ count }}!</h3>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count: 0,
    };
  },
  methods: {
    increaseCounter() {
      this.count++;
    },
    decreaseCounter() {
      this.count--;
    },
  },
};
</script>
