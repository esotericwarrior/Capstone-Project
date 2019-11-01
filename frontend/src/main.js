import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faBell,
  faComment,
  faHeart,
  faHome,
  faSearch,
  faUserCircle
} from "@fortawesome/free-solid-svg-icons";

// Import the Icons used in the Application
library.add(
  faBell,
  faComment,
  faHeart,
  faHome,
  faSearch,
  faUserCircle
);


Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount("#app");
