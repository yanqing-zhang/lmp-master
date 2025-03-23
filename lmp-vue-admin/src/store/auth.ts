import { defineStore } from "pinia";
import { loginApi } from "@/api/user";
interface LoginParams {
    username: string;
    password: string
}

export const useUserStore = defineStore("user", {
    state: () => ({
        token: sessionStorage.getItem("token") || "",
        roles: sessionStorage.getItem("roles") ? JSON.parse(sessionStorage.getItem("roles")!) : [],
        username: sessionStorage.getItem("username") || "",
        menu: sessionStorage.getItem("menu") ? JSON.parse(sessionStorage.getItem("menu")!) : [],
    }),
    actions: {
        async login(data: LoginParams) {
            try {
                let res = await loginApi(data);
                console.log(res)
                const { data: { token, user: { username, roles }, menulist } } = res

               console.log(token, roles, menulist)
                this.token = token
                this.roles = roles
                this.menu = menulist
                this.username = username;
                sessionStorage.setItem("token", token)
                sessionStorage.setItem("roles", JSON.stringify(roles))
                sessionStorage.setItem("username", username)
                sessionStorage.setItem("menu", JSON.stringify(menulist))
            } catch (error) {

            }
        },
        logout() {
            this.token=""
            this.roles=[];
            this.username=""
            this.menu=[];
            sessionStorage.clear()

        }
    }
})