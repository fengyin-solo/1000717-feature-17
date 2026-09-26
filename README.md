# 光伏电站智能运维管理平台

覆盖光伏区、逆变器、汇流箱、组件阵列、并网调度及抢修清洗的全流程光伏电站运维后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 光伏区管理 | `pv_zone` | 光伏区 | 区号、装机容量、组件类型 |
| 逆变器运行 | `inverter` | 逆变器 | 逆变器编号、额定功率、直流输入电压 |
| 汇流箱监测 | `combiner` | 汇流箱 | 汇流箱编号、所属组串、输入路数 |
| 组件阵列 | `module_array` | 光伏组件 | 组件编号、组件型号、峰值功率 |
| 发电量统计 | `generation` | 发电记录 | 记录日期、日发电量、峰值功率时刻 |
| 巡检任务 | `inspect` | 巡检任务 | 任务编号、巡检区域、巡检类型 |
| 故障抢修 | `fault` | 故障记录 | 故障编号、故障设备、故障现象 |
| 清洗计划 | `cleaning` | 清洗任务 | 清洗编号、清洗区域、清洗方式 |
| 并网调度 | `grid_connect` | 并网记录 | 记录编号、并网时间、并网功率 |
| 变压器运行 | `transformer` | 变压器 | 变压器编号、额定容量、电压等级 |
| 电量计量 | `metering` | 计量点 | 计量点编号、计量方式、正向有功电量 |
| 环境监测 | `environment` | 环境数据 | 监测站点、辐照强度、环境温度 |
| 运维班组 | `crew` | 运维人员 | 人员编号、姓名、岗位工种 |
| 安全工器具 | `safety_tool` | 安全工器具 | 器具编号、器具名称、器具类别 |
| 继电保护 | `relay` | 保护装置 | 装置编号、保护类型、定值区号 |
| 电缆线路 | `cable` | 电缆 | 电缆编号、电压等级、起止位置 |
| 值班日志 | `duty_log` | 值班记录 | 日志编号、值班日期、值班人员 |
| 操作票管理 | `oper_ticket` | 操作票 | 票号、操作任务、操作人 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
