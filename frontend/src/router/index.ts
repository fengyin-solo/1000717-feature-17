import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const PvZone = () => import('@/views/pv_zone/index.vue')
const Inverter = () => import('@/views/inverter/index.vue')
const Combiner = () => import('@/views/combiner/index.vue')
const ModuleArray = () => import('@/views/module_array/index.vue')
const Generation = () => import('@/views/generation/index.vue')
const Inspect = () => import('@/views/inspect/index.vue')
const Fault = () => import('@/views/fault/index.vue')
const Cleaning = () => import('@/views/cleaning/index.vue')
const GridConnect = () => import('@/views/grid_connect/index.vue')
const Transformer = () => import('@/views/transformer/index.vue')
const Metering = () => import('@/views/metering/index.vue')
const Environment = () => import('@/views/environment/index.vue')
const Crew = () => import('@/views/crew/index.vue')
const SafetyTool = () => import('@/views/safety_tool/index.vue')
const Relay = () => import('@/views/relay/index.vue')
const Cable = () => import('@/views/cable/index.vue')
const DutyLog = () => import('@/views/duty_log/index.vue')
const OperTicket = () => import('@/views/oper_ticket/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/pv_zone', name: 'pv_zone', component: PvZone },
    { path: '/inverter', name: 'inverter', component: Inverter },
    { path: '/combiner', name: 'combiner', component: Combiner },
    { path: '/module_array', name: 'module_array', component: ModuleArray },
    { path: '/generation', name: 'generation', component: Generation },
    { path: '/inspect', name: 'inspect', component: Inspect },
    { path: '/fault', name: 'fault', component: Fault },
    { path: '/cleaning', name: 'cleaning', component: Cleaning },
    { path: '/grid_connect', name: 'grid_connect', component: GridConnect },
    { path: '/transformer', name: 'transformer', component: Transformer },
    { path: '/metering', name: 'metering', component: Metering },
    { path: '/environment', name: 'environment', component: Environment },
    { path: '/crew', name: 'crew', component: Crew },
    { path: '/safety_tool', name: 'safety_tool', component: SafetyTool },
    { path: '/relay', name: 'relay', component: Relay },
    { path: '/cable', name: 'cable', component: Cable },
    { path: '/duty_log', name: 'duty_log', component: DutyLog },
    { path: '/oper_ticket', name: 'oper_ticket', component: OperTicket },
  ],
})

export default router
