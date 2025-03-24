#
#  visualizer.py
#  可视化组件 Visualization Component
#  AlgoVisual
#
#  Created by Z. Steve on 2025/3/23 21:54.
#
# 导入 tkinter 库，用于创建图形用户界面（GUI）
# Import the tkinter library for creating a graphical user interface (GUI)
import tkinter as tk
# 导入 time 模块，用于控制动画的延迟时间
# Import the time module to control the delay in animation
import time


# 定义 Visualizer 类，用于可视化排序算法的执行过程
# Define the Visualizer class to visualize the execution process of sorting algorithms
class Visualizer:
    # 初始化方法：设置画布并将其添加到主窗口中
    # __init__ method: Sets up the canvas and adds it to the main window
    def __init__(self, root):
        # 创建一个 Canvas 对象，指定宽度为 400 像素，高度为 300 像素
        # Create a Canvas object with a width of 400 pixels and a height of 300 pixels
        self.canvas = tk.Canvas(root, width=600, height=400)
        # 将画布打包到主窗口中，使其显示出来
        # Pack the canvas into the main window to make it visible
        self.canvas.pack()

    # start 方法：启动可视化过程，逐步展示算法的每一步
    # start method: Starts the visualization process, displaying each step of the algorithm
    def start(self, algorithm):
        # 清空画布上的所有内容，为新的可视化做准备
        # Clear all content on the canvas to prepare for a new visualization
        self.canvas.delete("all")
        # 显示初始状态，所有元素为蓝色
        initial_data = algorithm.data.copy()
        self.draw(initial_data, [], (0, len(initial_data)))  # 初始时没有比较索引，未排序范围覆盖全部
        self.canvas.update()
        time.sleep(0.5)  # 等待 0.5 秒再开始排序

        try:
            # 遍历算法的 visualize_step 方法返回的每一步数据
            # Iterate over each step of data returned by the algorithm's visualize_step method
            for step in algorithm.visualize_step():
                # 解包步骤数据：数组状态、当前比较索引、已排序范围
                # Unpack step data: array state, current comparison indices, sorted range
                data, current_indices, sorted_range = step
                # 绘制当前步骤的数据
                # Draw the data for the current step
                self.draw(data, current_indices, sorted_range)
                # 更新画布以显示绘制的内容
                # Update the canvas to display the drawn content
                self.canvas.update()
                # 暂停 0.5 秒，控制动画速度，使可视化过程更易观察
                # Pause for 0.5 seconds to control animation speed, making the visualization easier to observe
                time.sleep(0.5)
        except ValueError as e:
            # 捕获解包错误，可能是算法未正确返回元组
            # Catch unpacking errors, possibly due to the algorithm not returning a proper tuple
            print(f"Error in visualization: {e}. Expected (data, current_indices, sorted_range) from algorithm.")
        except Exception as e:
            # 捕获其他异常，打印错误信息
            # Catch other exceptions and print error information
            print(f"Unexpected error in visualization: {e}")

    # draw 方法：根据数据在画布上绘制矩形，表示当前数组状态
    # draw method: Draws rectangles on the canvas based on the data, representing the current array state
    def draw(self, data, current_indices, sorted_range):
        # 清空画布上的所有内容，避免旧的图形残留
        # Clear all content on the canvas to prevent remnants of old graphics
        self.canvas.delete("all")
        # 遍历数据列表，使用索引和值来绘制矩形
        # Iterate over the data list, using the index and value to draw rectangles
        for i, val in enumerate(data):
            # 根据索引确定矩形的颜色
            # Determine the rectangle color based on the index
            if i in current_indices:  # 当前正在比较的元素用红色表示
                # Elements currently being compared are shown in red
                color = "red"
            elif sorted_range[0] <= i < sorted_range[1]:  # 未排序的元素用蓝色表示
                # Elements in the unsorted range are shown in blue
                color = "blue"
            else:  # 已排序的元素用绿色表示
                # Elements already sorted are shown in green
                color = "green"
            # 创建矩形：左上角坐标 (50 + i * 30, 300 - val * 30)，右下角坐标 (80 + i * 30, 300)
            # Create a rectangle: top-left (50 + i * 30, 300 - val * 30), bottom-right (80 + i * 30, 300)
            self.canvas.create_rectangle(50 + i * 30, 300 - val * 30, 80 + i * 30, 300, fill=color)