#
#  bubble_sort.py
#  AlgoVisual
#
#  Created by Z. Steve on 2025/3/23 21:51.
#

from .base_algorithm import BaseAlgorithm


class BubbleSort(BaseAlgorithm):
    def run(self):
        self.data = self.load_data()
        for i in range(len(self.data)):
            for j in range(len(self.data) - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                # 返回当前数组的状态（self.data）,每一步生成当前状态
                # 这允许外部代码（例如可视化组件）逐步获取排序过程中的中间结果，而不是等到整个排序完成。
                yield self.data

    def visualize_step(self):
        # 返回生成器，用于逐步展示
        return self.run()

    def load_data(self, filepath="assets/sample_data.txt"):
        with open(filepath, "r") as f:
            data = [int(x) for x in f.read().strip().split(" ")]
        return data
