# encoding: UTF-8

# 从language模块导入常量定义
from language import constant

# 将常量定义添加到vtConstant.py的局部字典中3
d = locals()
for name in dir(constant):
    if '__' not in name:
        d[name] = constant.__getattribute__(name)
