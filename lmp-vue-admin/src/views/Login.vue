<template>
  <div class="bg">
    <div class="login_content">
      <div class="login">
        <div class="logo">
          <img :src="logo" alt="" width="70px" height="70px"/>
          <h2 class="ml" style="color: #FF6014;">大模型实验平台</h2>
        </div>
        <el-form :model="ruleForm" :rules="rules" ref="formRef">
          <el-form-item prop="username">
            <el-input v-model="ruleForm.username" placeholder="请输入用户名" prefix-icon="User"/>
          </el-form-item>
          <el-form-item prop="password">
            <el-input v-model="ruleForm.password" placeholder="请输入密码" prefix-icon="Lock" type="password"/>
          </el-form-item>
          <el-form-item>
            <el-button plain type="warning" style="width: 100%;" @click="handleLogin">登录</el-button>
          </el-form-item>
        </el-form>
      </div>
      <img class="bgImg" src="../assets/right-img-5.png" alt=""/>
    </div>
  </div>
</template>

<script setup lang="ts">
import logo from "@/assets/giteeai.svg"
import { reactive,ref } from "vue";
import type { FormRules,FormInstance } from 'element-plus'
import {useUserStore} from "@/store/auth.ts"
import { useRouter } from "vue-router";
interface RuleForm{
  username: string;
  password: string;
}
const ruleForm: RuleForm = reactive({
  username: "",
  password: ""
})
const rules = reactive<FormRules<RuleForm>>({
  username:[
    {required: true, message: "用户名不能为空", trigger: "blur"},
    {min: 4, max: 8, message: "用户名要求4-8位数字字母组合", trigger: "blur"}
  ],
  password:[
    {required: true, message: "密码不能为空", trigger: "blur"}
  ]
})
const formRef = ref<FormInstance>();
const userStore=useUserStore()
const router=useRouter()
const handleLogin=()=>{
  formRef.value?.validate(async (valid:boolean)=>{
    if(valid){
      await userStore.login(ruleForm);
      router.push("/")
    }
  })
}
</script>

<style lang="less" scoped>
.bg {
  background-image: url("../assets/bgx.png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 100vh;
  .login_content {
    width: 1042px;
    height: 500px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 2;
    box-shadow: 10px 10px 36px #88532d1a;
    border-radius: 10px;
    overflow: hidden;
    display: flex;

    .login {
      flex: 1;
      height: 100%;
      background: #fff;
      padding: 114px 81px 0;
      box-sizing: border-box;
      position: relative;
      .bgImg{
        width: 580px;
        height: 100%;
      }
      .logo {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 40px;
        h1 {
          color: rgb(255, 96, 20);
        }
      }
    }
  }

}
</style>