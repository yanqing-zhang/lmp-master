import service from "./axios";
interface ResponseData{
    code:number,
    data:any,
    massage:string
}

function get(url:string, params?:any):Promise<ResponseData>{
    return service.get(url, {params})
}

function post(url:string, data?:any):Promise<ResponseData>{

    return service.post(url, data)
}

export {get, post}