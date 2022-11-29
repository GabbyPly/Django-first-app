<template>
  <textarea class="what" name="" id="some" cols="30" rows="10"></textarea>
</template>

<script>
import "codemirror/addon/edit/matchbrackets";
import "codemirror/lib/codemirror.css";
import "codemirror/mode/javascript/javascript";
import CM from "codemirror";
console.log("CM", CM);
console.log("CM.fromTextArea", CM.fromTextArea);
const myCodeMirror = CM.fromTextArea(document.getElementById("some"), {
  value: "function myScript(){return 100;}\n",
  mode: "javascript", // { name: "javascript", json: true }
  theme: "darcula",
  lineNumbers: true,
  // lineWrapping: true,
});
console.log("hey created  myCodeMirror", myCodeMirror);

import { defineComponent } from "vue";

import "codemirror/theme/darcula.css";

export default {
  components: {}, // Codemirror,
  // created() {
  //   const myCodeMirror = CM.fromTextArea(document.getElementById("some"), {
  //     value: "function myScript(){return 100;}\n",
  //     mode: "javascript", // { name: "javascript", json: true }
  //     theme: "darcula",
  //     lineNumbers: true,
  //     // lineWrapping: true,
  //   });
  //   console.log("hey created  myCodeMirror", myCodeMirror);
  // },
};
</script>
<style lang="css" scoped>
#some {
  text-align: left !important;
}
.CodeMirror-scroll {
  color: brown;
  /* text-align: left !important; */
}
</style>
