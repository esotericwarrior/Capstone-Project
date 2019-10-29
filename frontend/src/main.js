import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faBell,
  faUserCircle
} from '@fortawesome/free-solid-svg-icons';

library.add(
  faBell,
  faUserCircle
);


Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount("#app");
