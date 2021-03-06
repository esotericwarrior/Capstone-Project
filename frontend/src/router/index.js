import Vue from "vue";
import VueRouter from "vue-router";
import About from "../views/About.vue";
import CommentEditor from "../views/CommentEditor.vue";
// import { CommentEditor } from "@/components/Application/Comment";
import Home from "../views/Home.vue";
import Post from "../views/Post.vue";
import Profile from "../views/Profile.vue";
import { PostEditor } from "@/components/Application/Posts";
import Support from "../views/Support.vue";

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      component: Home,
      name: "Home"
    },
    {
      path: "/about",
      component: About,
      name: "About"
    },
    {
      path: "/comment/:id",
      name: "comment-editor",
      component: CommentEditor,
      props: true
    },
    {
      path: "/createpost/:slug?",
      name: "post-editor",
      component: PostEditor,
      props: true
    },
    {
      path: "/post/:slug",
      name: "post",
      component: Post,
      props: true
    },
    {
      path: "/profile/:username",
      name: "profile",
      component: Profile,
      props: true
    },
    {
      path: "/support",
      component: Support,
      name: "Support"
    }
  ]
});
