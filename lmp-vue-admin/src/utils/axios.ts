import axios, {AxiosError} from "axios";
import type {AxiosInstance, InternalAxiosRequestConfig, AxiosResponse} from "axios";
import { ElNotification } from "element-plus";
const service: AxiosInstance=axios.create({
    baseURL:"/api",
    timeout:5000
})

service.interceptors.request.use((config:InternalAxiosRequestConfig)=>{
    return config
},(error:AxiosError)=>{
    ElNotification({
        title:"Error",
        message:error.message,
        type:"error",
    });
    return Promise.reject(error)
})

service.interceptors.response.use((response:AxiosResponse)=>{
    if(response.data.code!=200){
        ElNotification({
            title:"Error",
            message:response.data.message,
            type:"error",
        });
    }else{
        return response.data
    }
},(error:AxiosError)=>{
    ElNotification({
        title:"Error",
        message:error.message,
        type:"error",
    });
    return Promise.reject(error)
})

export default service