#
#  visualizer.py
#  可视化组件 Visualization Component
#  AlgoVisual
#
#  Created by Z. Steve on 2025/3/23 21:54.
#

import tkinter as tk
import time


class Visualizer:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()

    def start(self, algorithm):
        self.canvas.delete("all")
        for step in algorithm.visualize_step():
            self.draw(step)
            self.canvas.update()
            time.sleep(0.5)  # 控制动画速度

    def draw(self, data):
        self.canvas.delete("all")
        for i, val in enumerate(data):
            self.canvas.create_rectangle(50 + i * 30, 300 - val * 30, 80 + i * 30, 300, fill="blue")
