#
#  base_algorithm.py
#  Algorithm Base Class (Defining a Unified Interface)
#  AlgoVisual
#
#  Created by Z. Steve on 2025/3/23 21:52.
#

# 从 abc 模块导入 ABC（抽象基类）
from abc import ABC, abstractmethod


class BaseAlgorithm(ABC):
    def __init__(self, data):
        # 输入数据
        self.data = data

    # 执行算法，返回结果
    @abstractmethod
    def run(self):
        pass

    # 生成每一步的可视化数据
    @abstractmethod
    def visualize_step(self):
        pass
