import { createRouter, createWebHistory } from "vue-router";
import UniversitiesView from "../views/UniversitiesView.vue";
import HomeView from "../views/HomeView.vue";
import SignUpView from "../views/SignUpView.vue";
import BlogPostView from "../views/BlogPostView.vue";
import CreatePostView from "../views/CreatePostView.vue";
import LogOutView from "../views/LogOutView.vue";
import CodeMirrorView from "../views/CodeMirrorView.vue";
import Guards from "./routerGaurds";

const allowedWithoutAuthRoutes = [
  {
    path: "/home",
    // path: "/home/:id",
    name: "home",
    component: HomeView,
    props: (route) => {
      console.log("route!!!", route);
      return { return_to: route?.redirectedFrom?.fullPath };
      // return { return_to: route.query.token };
    },
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: SignUpView,
  },
];

const requiredAuthRoutes = [
  {
    path: "/blog-post",
    name: "BlogPost",
    component: BlogPostView,
  },
  {
    path: "/create-post",
    name: "CreatePost",
    component: CreatePostView,
  },
  {
    path: "/universities",
    name: "universities",
    component: UniversitiesView,
  },
  {
    path: "/log-out",
    name: "LogOut",
    component: LogOutView,
  },
  {
    path: "/code-mirror",
    name: "CodeMirror",
    component: CodeMirrorView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
];

function setRoutesAuthRequirements() {
  const routes = [];
  routes.push(
    ...allowedWithoutAuthRoutes.map((x) => addRequiredAuth(x, false))
  );
  routes.push(...requiredAuthRoutes.map((x) => addRequiredAuth(x, true)));
  return routes;
}

function addRequiredAuth(route, value) {
  if (route.meta) {
    route.meta.requiresAuth = value;
  } else {
    route.meta = { requiresAuth: value };
  }
  return route;
}

const routes = setRoutesAuthRequirements();

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  // routes,
});

router.beforeEach(Guards.guardLoggedIn);

export default router;
