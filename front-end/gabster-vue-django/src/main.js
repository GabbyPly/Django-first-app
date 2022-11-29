import { createApp } from "vue";
// import { createStore } from "vuex";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import { loadFonts } from "./plugins/webfontloader";
import CodeMirrorComponent from "./views/CodeMirrorView.vue";

loadFonts();

// createApp(App).use(router).use(vuetify).mount("#app");

const app = createApp(App);
app.use(router);
app.use(vuetify);

app.component("CodeMirrorComponent", CodeMirrorComponent);
const mountedApp = app.mount("#app");
