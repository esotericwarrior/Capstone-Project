import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import Vue from "vue";
import Vuetify from "vuetify/lib";
import { library } from '@fortawesome/fontawesome-svg-core'
import {
  faBell,
  faCamera,
  faCog,
  faComment,
  faEdit,
  faHeart,
  faHome,
  faPen,
  faPlusSquare,
  faSearch,
  faStar,
  faTimes,
  faTrash,
  faUserCircle
} from "@fortawesome/free-solid-svg-icons";

// Import the Icons used in the Application
library.add(
  faBell,
  faCamera,
  faCog,
  faComment,
  faEdit,
  faHeart,
  faHome,
  faPen,
  faPlusSquare,
  faSearch,
  faStar,
  faTimes,
  faTrash,
  faUserCircle
);

// Override Vuetify Icons with Custom FA Font Library
const CUSTOM_ICONS = {
  edit: "fas fa-edit",
}

Vue.component('font-awesome-icon', FontAwesomeIcon) // Register component globally

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: 'fa',
    values: CUSTOM_ICONS,
  },
});
