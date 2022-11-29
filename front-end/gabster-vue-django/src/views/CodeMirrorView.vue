<template>
  <textarea
    v-model="code"
    class="what"
    name=""
    ref="editor"
    id="editor"
    cols="30"
    rows="10"
  ></textarea>
</template>

<script>
import "codemirror/addon/edit/matchbrackets";
import "codemirror/addon/edit/closebrackets";
import "codemirror/lib/codemirror.css";
import "codemirror/mode/javascript/javascript";
import CM from "codemirror";
/*
// created() {
  //   const myCodeMirror = CM.fromTextArea(document.getElementById("editor"), {
  //     value: "function myScript(){return 100;}\n",
  //     mode: "javascript", // { name: "javascript", json: true }
  //     theme: "darcula",
  //     lineNumbers: true,
  //     lineWrapping: true,
  //   });
  //   console.log("hey created  myCodeMirror", myCodeMirror);
  // },
*/

import { defineComponent } from "vue";

import "codemirror/theme/darcula.css";

export default defineComponent({
  components: {}, // Codemirror,
  created() {
    const editor = document.getElementById("editor");
    console.log("created  editor", editor);
  },
  computed: {
    code() {
      return "function myScript(){return 100;}\n";
    },
  },
  mounted() {
    console.log("mounted");
    console.log("refs", this.$refs);
    const editor = this.$refs.editor;
    if (editor) {
      // document
      //   .getElementsByClassName("CodeMirror-scroll")
      //   .style.setProperty("text-align", "left"); // left !important
      console.log("mounted  scroll", scroll);
      const myCodeMirror = CM.fromTextArea(editor, {
        value: "function myScript(){return 100;}\n",
        mode: "javascript", // { name: "javascript", json: true }
        theme: "darcula",
        lineNumbers: true,
        spellcheck: true,
        matchingbrackets: true,
        autoCloseBrackets: true,
        // lineWrapping: true,
      });
      myCodeMirror.setOption("closebrackets", true);
      console.log({ CM });
      console.log("hey created  myCodeMirror", myCodeMirror);
    }
  },
  // created() {
  //   const myCodeMirror = CM.fromTextArea(document.getElementById("editor"), {
  //     value: "function myScript(){return 100;}\n",
  //     mode: "javascript", // { name: "javascript", json: true }
  //     theme: "darcula",
  //     lineNumbers: true,
  //     // lineWrapping: true,
  //   });
  //   console.log("hey created  myCodeMirror", myCodeMirror);
  // },
});
</script>
<style lang="css" scoped>
.what {
  text-align: left !important;
}
</style>
