#
#  bubble_sort.py
#  AlgoVisual
#
#  Created by Z. Steve on 2025/3/23 21:51.
#

# 导入基类 BaseAlgorithm，用于定义排序算法的通用接口和方法
# Import the base class BaseAlgorithm, which defines a common interface and methods for sorting algorithms
from .base_algorithm import BaseAlgorithm


# 定义冒泡排序类，继承自 BaseAlgorithm
# Define the BubbleSort class, inheriting from BaseAlgorithm
class BubbleSort(BaseAlgorithm):
    # 初始化方法：继承自 BaseAlgorithm，接受传入的数据
    # __init__ method: Inherited from BaseAlgorithm, accepts the provided data
    def __init__(self, data):
        # 调用父类的初始化方法，将传入的数据赋值给 self.data
        # Call the parent class's __init__ method to assign the provided data to self.data
        super().__init__(data)
        # 确保使用数据的副本，避免修改原始数据
        # Ensure a copy of the data is used to avoid modifying the original data
        self.data = data.copy()

    # run 方法：实现冒泡排序的核心逻辑，并支持逐步返回中间状态
    # run method: Implements the core logic of bubble sort and supports yielding intermediate states step-by-step
    def run(self):
        # 获取数组长度
        # Get the length of the array
        n = len(self.data)
        # 外层循环，控制排序的轮数（每轮将一个最大值“冒泡”到末尾）
        # Outer loop: Controls the number of sorting passes (each pass "bubbles" the largest value to the end)
        for i in range(n):
            # 内层循环，比较相邻元素并交换位置，逐渐减少比较范围
            # Inner loop: Compares adjacent elements and swaps them, gradually reducing the comparison range
            for j in range(n - i - 1):
                # 第一步：仅比较，不交换，显示两个数字为红色
                yield (self.data.copy(), [j, j + 1], (0, n - i))
                # 如果当前元素大于下一个元素，则交换两者位置
                # If the current element is greater than the next element, swap their positions
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                # 返回当前数组状态、当前比较的索引对、已排序范围
                # Return current array state, current comparison indices, and sorted range
                # - self.data.copy(): 当前数组状态的副本
                # - [j, j+1]: 当前比较的两个索引
                # - (0, n-i-1): 已排序范围（从开头到未排序部分的起点）
                yield (self.data.copy(), [j, j + 1], (0, n - i))
        # 排序完成后，额外生成最终状态，所有元素都在已排序范围内
        yield (self.data.copy(), [], (0, 0))  # current_indices 为空，sorted_range 覆盖整个数组

    # visualize_step 方法：提供生成器接口，用于逐步展示排序过程
    # visualize_step method: Provides a generator interface to display the sorting process step-by-step
    def visualize_step(self):
        # 直接调用 run 方法并返回其生成器
        # Directly call the run method and return its generator
        return self.run()
