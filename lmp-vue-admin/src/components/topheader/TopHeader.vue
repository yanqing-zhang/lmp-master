<template>
  <div class="header">
    <div class="personal">
      <el-badge :is-dot="info > 0" class="item">
        <el-icon>
          <Bell />
        </el-icon>
      </el-badge>
      <el-avatar :src="avatar_tou" class="ml mr"/>
      <el-dropdown @command="handleCommand">
                <span class="el-dropdown-link">
                    欢迎你, {{ username }}
                    <el-icon class="el-icon--right">
                        <arrow-down/>
                    </el-icon>
                </span>
        <template #dropdown>
          <el-dropdown-item icon="User" command="user">个人中心</el-dropdown-item>
          <el-dropdown-item icon="SwitchButton" command="logout">退出登录</el-dropdown-item>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script setup lang="ts">
import avatar_tou from "@/assets/avatar/tou-2.png"
import { ref } from "vue"
import { useUserStore } from "@/store/auth";
import { storeToRefs } from "pinia";
import {useRouter} from "vue-router"
const router=useRouter()
const userStore=useUserStore();
const {username}=storeToRefs(userStore)
const info = ref(5)

const handleCommand=(command:string)=>{
  if(command=="user"){
    router.push("/personal")
  }else{
    userStore.logout()
    router.push("/login")
  }
}
</script>

<style lang="less">
.header{
  background-color: white;
  height: 60px;
  padding: 0 20px;
  .personal{
    float: right;
    display: flex;
    height: 60px;
    align-items: center;
    .item{
      margin-top: 10px;
    }
  }
}
</style>