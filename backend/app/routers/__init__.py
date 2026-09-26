"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import pv_zone as router_pv_zone
from app.routers import inverter as router_inverter
from app.routers import combiner as router_combiner
from app.routers import module_array as router_module_array
from app.routers import generation as router_generation
from app.routers import inspect as router_inspect
from app.routers import fault as router_fault
from app.routers import cleaning as router_cleaning
from app.routers import grid_connect as router_grid_connect
from app.routers import transformer as router_transformer
from app.routers import metering as router_metering
from app.routers import environment as router_environment
from app.routers import crew as router_crew
from app.routers import safety_tool as router_safety_tool
from app.routers import relay as router_relay
from app.routers import cable as router_cable
from app.routers import duty_log as router_duty_log
from app.routers import oper_ticket as router_oper_ticket

ROUTERS = [router_pv_zone, router_inverter, router_combiner, router_module_array, router_generation, router_inspect, router_fault, router_cleaning, router_grid_connect, router_transformer, router_metering, router_environment, router_crew, router_safety_tool, router_relay, router_cable, router_duty_log, router_oper_ticket]
