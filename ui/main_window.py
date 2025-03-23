#
#  main_window.py
#  AlgoVisual
#
#  Created by Z. Steve on 2025/3/23 21:54.
#

import tkinter as tk
from importlib import import_module
import os
from time import sleep

from .visualizer import Visualizer


class MainWindow():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Algorithm Visualizer")
        self.algorithm_list = self.load_algorithms()
        self.visualizer = Visualizer(self.root)
        self.setup_ui()

    def load_algorithms(self):
        algorithms = {}
        algo_dir = "algorithms"
        for file in os.listdir(algo_dir):
            if file.endswith(".py") and file not in ["__init__.py", "base_algorithm.py"]:
                module_name = file[:-3]  # 去掉 .py
                module = import_module(f"algorithms.{module_name}")
                algo_class = getattr(module, module_name.title().replace("_", ""))
                algorithms[module_name] = algo_class
        return algorithms

    def setup_ui(self):
        for name, algo_class in self.algorithm_list.items():
            btn = tk.Button(self.root, text=name.replace("_", "").title(),
                            command=lambda a=algo_class: self.run_algorithm(a))
            btn.pack(pady=5)
        self.root.mainloop()

    def run_algorithm(self, algo_class):
        data = [5, 2, 8, 1, 9]  # 示例数据，可改为用户输入
        algorithm = algo_class(data)
        self.visualizer.start(algorithm)
