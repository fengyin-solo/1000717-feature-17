"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class PvZoneEntry(BaseModel):
    """光伏区明细结构。"""

    field_0: str | None = None  # 区号
    field_1: str | None = None  # 装机容量
    field_2: str | None = None  # 组件类型
    field_3: str | None = None  # 安装倾角
    field_4: str | None = None  # 并网日期
    field_5: str | None = None  # 占地面积
    field_6: str | None = None  # 所属升压站
    field_7: str | None = None  # 区域状态

class InverterEntry(BaseModel):
    """逆变器明细结构。"""

    field_0: str | None = None  # 逆变器编号
    field_1: str | None = None  # 额定功率
    field_2: str | None = None  # 直流输入电压
    field_3: str | None = None  # 交流输出电压
    field_4: str | None = None  # 运行温度
    field_5: str | None = None  # 转换效率
    field_6: str | None = None  # 投运日期
    field_7: str | None = None  # 运行状态

class CombinerEntry(BaseModel):
    """汇流箱明细结构。"""

    field_0: str | None = None  # 汇流箱编号
    field_1: str | None = None  # 所属组串
    field_2: str | None = None  # 输入路数
    field_3: str | None = None  # 最大电流
    field_4: str | None = None  # 防雷等级
    field_5: str | None = None  # 外壳防护等级
    field_6: str | None = None  # 通讯协议
    field_7: str | None = None  # 监测状态

class ModuleArrayEntry(BaseModel):
    """光伏组件明细结构。"""

    field_0: str | None = None  # 组件编号
    field_1: str | None = None  # 组件型号
    field_2: str | None = None  # 峰值功率
    field_3: str | None = None  # 开路电压
    field_4: str | None = None  # 短路电流
    field_5: str | None = None  # 填充因子
    field_6: str | None = None  # 安装方位角
    field_7: str | None = None  # 组件状态

class GenerationEntry(BaseModel):
    """发电记录明细结构。"""

    field_0: str | None = None  # 记录日期
    field_1: str | None = None  # 日发电量
    field_2: str | None = None  # 峰值功率时刻
    field_3: str | None = None  # 等效利用小时
    field_4: str | None = None  # 月累计发电量
    field_5: str | None = None  # 辐照总量
    field_6: str | None = None  # 弃光电量
    field_7: str | None = None  # 记录状态

class InspectEntry(BaseModel):
    """巡检任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 巡检区域
    field_2: str | None = None  # 巡检类型
    field_3: str | None = None  # 巡检人员
    field_4: str | None = None  # 计划日期
    field_5: str | None = None  # 完成日期
    field_6: str | None = None  # 异常发现
    field_7: str | None = None  # 任务状态

class FaultEntry(BaseModel):
    """故障记录明细结构。"""

    field_0: str | None = None  # 故障编号
    field_1: str | None = None  # 故障设备
    field_2: str | None = None  # 故障现象
    field_3: str | None = None  # 发生时间
    field_4: str | None = None  # 影响容量
    field_5: str | None = None  # 抢修班组
    field_6: str | None = None  # 恢复时间
    field_7: str | None = None  # 故障状态

class CleaningEntry(BaseModel):
    """清洗任务明细结构。"""

    field_0: str | None = None  # 清洗编号
    field_1: str | None = None  # 清洗区域
    field_2: str | None = None  # 清洗方式
    field_3: str | None = None  # 计划日期
    field_4: str | None = None  # 用水量
    field_5: str | None = None  # 清洗班组
    field_6: str | None = None  # 洁净度评估
    field_7: str | None = None  # 清洗状态

class GridConnectEntry(BaseModel):
    """并网记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 并网时间
    field_2: str | None = None  # 并网功率
    field_3: str | None = None  # 调度指令内容
    field_4: str | None = None  # 解列原因
    field_5: str | None = None  # 调度值班员
    field_6: str | None = None  # 解列时间
    field_7: str | None = None  # 并网状态

class TransformerEntry(BaseModel):
    """变压器明细结构。"""

    field_0: str | None = None  # 变压器编号
    field_1: str | None = None  # 额定容量
    field_2: str | None = None  # 电压等级
    field_3: str | None = None  # 顶层油温
    field_4: str | None = None  # 绕组温度
    field_5: str | None = None  # 油位指示
    field_6: str | None = None  # 冷却方式
    field_7: str | None = None  # 运行状态

class MeteringEntry(BaseModel):
    """计量点明细结构。"""

    field_0: str | None = None  # 计量点编号
    field_1: str | None = None  # 计量方式
    field_2: str | None = None  # 正向有功电量
    field_3: str | None = None  # 反向有功电量
    field_4: str | None = None  # 无功电量
    field_5: str | None = None  # 倍率
    field_6: str | None = None  # 表计型号
    field_7: str | None = None  # 计量状态

class EnvironmentEntry(BaseModel):
    """环境数据明细结构。"""

    field_0: str | None = None  # 监测站点
    field_1: str | None = None  # 辐照强度
    field_2: str | None = None  # 环境温度
    field_3: str | None = None  # 风速
    field_4: str | None = None  # 风向
    field_5: str | None = None  # 相对湿度
    field_6: str | None = None  # 降雨量
    field_7: str | None = None  # 数据状态

class CrewEntry(BaseModel):
    """运维人员明细结构。"""

    field_0: str | None = None  # 人员编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 岗位工种
    field_3: str | None = None  # 资质证书
    field_4: str | None = None  # 联系电话
    field_5: str | None = None  # 所属班组
    field_6: str | None = None  # 值班排班
    field_7: str | None = None  # 在岗状态

class SafetyToolEntry(BaseModel):
    """安全工器具明细结构。"""

    field_0: str | None = None  # 器具编号
    field_1: str | None = None  # 器具名称
    field_2: str | None = None  # 器具类别
    field_3: str | None = None  # 检定日期
    field_4: str | None = None  # 有效期至
    field_5: str | None = None  # 保管人
    field_6: str | None = None  # 存放位置
    field_7: str | None = None  # 使用状态

class RelayEntry(BaseModel):
    """保护装置明细结构。"""

    field_0: str | None = None  # 装置编号
    field_1: str | None = None  # 保护类型
    field_2: str | None = None  # 定值区号
    field_3: str | None = None  # 投运日期
    field_4: str | None = None  # 最近校验日
    field_5: str | None = None  # 动作次数
    field_6: str | None = None  # 通讯状态
    field_7: str | None = None  # 装置状态

class CableEntry(BaseModel):
    """电缆明细结构。"""

    field_0: str | None = None  # 电缆编号
    field_1: str | None = None  # 电压等级
    field_2: str | None = None  # 起止位置
    field_3: str | None = None  # 敷设方式
    field_4: str | None = None  # 截面面积
    field_5: str | None = None  # 长度
    field_6: str | None = None  # 投运日期
    field_7: str | None = None  # 运行状态

class DutyLogEntry(BaseModel):
    """值班记录明细结构。"""

    field_0: str | None = None  # 日志编号
    field_1: str | None = None  # 值班日期
    field_2: str | None = None  # 值班人员
    field_3: str | None = None  # 气象概况
    field_4: str | None = None  # 运行方式
    field_5: str | None = None  # 异常情况
    field_6: str | None = None  # 交接事项
    field_7: str | None = None  # 记录状态

class OperTicketEntry(BaseModel):
    """操作票明细结构。"""

    field_0: str | None = None  # 票号
    field_1: str | None = None  # 操作任务
    field_2: str | None = None  # 操作人
    field_3: str | None = None  # 监护人
    field_4: str | None = None  # 操作时间
    field_5: str | None = None  # 操作步骤数
    field_6: str | None = None  # 危险点分析
    field_7: str | None = None  # 票状态
