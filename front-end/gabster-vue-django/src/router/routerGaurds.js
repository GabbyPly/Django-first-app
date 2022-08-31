import router from "./index";

async function guardLoggedIn(...args) {
  const [to, from, next] = args;

  const store = { getters: {} };
  // notice: else is important here, next does not finish the scope

  // if (!store.getters.isLoggedIn) {
  if (to.matched.some((route) => route.meta.requiresAuth)) {
    if (!localStorage.token) {
      console.log("No token in local storage");
      console.log({ href: window.location.href, query: to.query });
      console.log({ to, from, next });
      console.log("from!!!", from);
      //   next("home/" + "return_to=" + to.fullPath);

      next({
        name: "home",
        query: { return_to: to.fullPath }, // || window.location.href, ...to.query
        // query: { nextUrl: to.fullPath }, // || window.location.href, ...to.query
      });
      //   router.push(to.path);
    } else {
      //   if (store.getters.user === null) {
      //     await store.dispatch("initUser");
      //   }

      // I Guess he's logged in ?
      console.log("First else, next()");
      next();
    }
  } else {
    // no auth required
    console.log("no auth required");
    next();
  }
}

export default { guardLoggedIn };
