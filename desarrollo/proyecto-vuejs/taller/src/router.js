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
      path: "/departamento",
      name: "departamento",
      component: () => import("./components/DepartamentosList.vue")
    },
    {
      path: "/create_departamento",
      name: "create_departamento",
      component: () => import("./components/CreateDepartamento.vue")
    },
    {
       path: "/edit_departamento/:id",
       name: "edit_departamento",
       component: () => import("./components/EditDepartamento.vue")
     },
  ]
});
