import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      redirect: '/index'
    },
    {
       path: "/create",
       name: "create",
       component: () => import("./components/Create.vue")
    },
    {
       path: "/edit/:id",
       name: "edit",
       component: () => import("./components/Edit.vue")
     },
    {
      path: "/index",
      name: "index",
      component: () => import("./components/Index.vue")
    },
    {
      path: "/telefonos",
      name: "telefonos",
      component: () => import("./components/TelefonosList.vue")
    },
    {
      path: "/create_telefono",
      name: "create_telefono",
      component: () => import("./components/CreateTelefono.vue")
    },
    {
       path: "/edit_telefono/:id",
       name: "edit_telefono",
       component: () => import("./components/EditTelefono.vue")
     },
  ]
});
