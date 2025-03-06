import router from "./index";
import { useUserStore } from "@/store/auth";
router.beforeEach((to)=>{
    const userStore=useUserStore()
    const isLogin=userStore.token;
    if(!isLogin){
        if(to.path!=="/login"){
            return {path:"/login"}
        }
    }else{
        if(to.path==="/login"){
            return {path:"/"}
        }
        if(to.meta?.needAuth&&!userStore.roles.some((role:string)=>(to.meta.needAuth as string[]).includes(role))){
            return {path:"/"}
        }
    }
})