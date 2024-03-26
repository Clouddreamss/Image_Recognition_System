<template>
    <div>
        <el-menu
            default-active="home"
            class="el-menu-vertical-demo"
            background-color="#545c64"
            text-color="#fff"
            @select="changeSidebar"
            active-text-color="#ffd04b"
        >
            <!-- 点击菜单 -->
            <el-menu-item index="home">
                <i class="el-icon-menu"></i>
                <span slot="title">首页</span>
            </el-menu-item>

            <!-- 可展开菜单 -->
            <el-submenu index="system">
                <template slot="title">
                    <i class="el-icon-location"></i>
                    <span>系统管理</span>
                </template>
                <el-menu-item index="userManagement">
                    <i class="el-icon-document"></i>
                    <span slot="title">用户管理</span>
                </el-menu-item>
                <el-menu-item index="productManagement">
                    <i class="el-icon-document"></i>
                    <span slot="title">产品管理</span>
                </el-menu-item>
            </el-submenu>
        </el-menu>
    </div>
</template>

<script>
export default {
    data() {
        return {}
    },

    mounted() {
        this.sidebarItem = this.$route.name
    },
    methods: {
        changeSidebar(path) {
            this.$router.push(path)
        }
    }
}
</script>
