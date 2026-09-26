<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">光伏电站智能运维管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">覆盖光伏区、逆变器、汇流箱、组件阵列、并网调度及抢修清洗的全流程光伏电站运维后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "光伏区管理", path: "/pv_zone" }, { label: "逆变器运行", path: "/inverter" }, { label: "汇流箱监测", path: "/combiner" }, { label: "组件阵列", path: "/module_array" }, { label: "发电量统计", path: "/generation" }, { label: "巡检任务", path: "/inspect" }, { label: "故障抢修", path: "/fault" }, { label: "清洗计划", path: "/cleaning" }, { label: "并网调度", path: "/grid_connect" }, { label: "变压器运行", path: "/transformer" }, { label: "电量计量", path: "/metering" }, { label: "环境监测", path: "/environment" }, { label: "运维班组", path: "/crew" }, { label: "安全工器具", path: "/safety_tool" }, { label: "继电保护", path: "/relay" }, { label: "电缆线路", path: "/cable" }, { label: "值班日志", path: "/duty_log" }, { label: "操作票管理", path: "/oper_ticket" }]
</script>
