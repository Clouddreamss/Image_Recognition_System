import Vue from "vue";
import VueRouter from "vue-router";
import Layouts from "../layouts";

Vue.use(VueRouter);

const routes = [
  {
    path: "",
    redirect: "home",
    component: Layouts,
    children: [
      {
        path: "/home",
        meta: { title: "首页", icon: "el-icon-s-home" },
        component: () => import("../views/home"),
      },
      {
        path: "/system",
        meta: { title: "系统管理", icon: "el-icon-s-home" },
        component: Layouts,
        children: [
          {
            path: "/userManagement",
            meta: { title: "用户管理", icon: "el-icon-s-home" },
            component: () => import("../views/system/userManagement"),
          },
          {
            path: "/productManagement",
            meta: { title: "产品管理", icon: "el-icon-s-home" },
            component: () => import("../views/system/productManagement"),
          },
        ],
      },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

// 前置路由拦截器
router.beforeEach((to, from, next) => {
  // 设置当前页签名称
  document.title = to.meta.title;
  next();
});

export default router;
