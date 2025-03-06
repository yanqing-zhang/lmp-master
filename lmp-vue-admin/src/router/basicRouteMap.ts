import type { RouteRecordRaw } from 'vue-router';

const routes:RouteRecordRaw[]=[
    {
        path:"/",
        name:"Home",
        component:()=>import("@/layouts/DefaultLayout.vue"),
        redirect:"/dashboard",
        children:[
            {
                path:"/dashboard",
                name:"dashboard",
                component:()=>import("@/views/dashboard/Index.vue")
            },
            {
                path:"/permission",
                name:"permission",
                component:()=>import("@/views/permission/Index.vue"),
                meta:{
                    needAuth:["admin"]
                }
            },
            {
                path:"/profile",
                name:"profile",
                component:()=>import("@/views/profile/Index.vue")
            },
        ]
    },
    {
        path:"/login",
        name:"Login",
        component:()=>import("@/views/Login.vue")
    },
    {
        path:"/:pathMatch(.*)*",
        name:"NotFound",
        component:()=>import("@/views/NotFound.vue")
    }
]

export default routes