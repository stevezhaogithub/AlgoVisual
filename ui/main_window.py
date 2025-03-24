#
#  main_window.py
#  AlgoVisual
#
#  Created by Z. Steve on 2025/3/23 21:54.
#
# 导入 tkinter 库，用于创建图形用户界面（GUI）
# Import the tkinter library for creating a graphical user interface (GUI)
import tkinter as tk
# 导入 importlib 模块，用于动态加载算法模块
# Import the importlib module for dynamically loading algorithm modules
from importlib import import_module
# 导入 os 模块，用于处理文件和目录操作
# Import the os module for handling file and directory operations
import os
# 导入 time 模块中的 sleep 函数，用于控制延迟（尽管这里未直接使用）
# Import the sleep function from the time module to control delays (though not directly used here)
from time import sleep

# 从当前包中导入 Visualizer 类，用于可视化排序过程
# Import the Visualizer class from the current package for visualizing the sorting process
from .visualizer import Visualizer


# 定义 MainWindow 类，作为算法可视化的主窗口
# Define the MainWindow class as the main window for algorithm visualization
class MainWindow():
    # 初始化方法：设置主窗口、加载算法列表、初始化可视化器并设置界面
    # __init__ method: Sets up the main window, loads the algorithm list, initializes the visualizer, and sets up the UI
    def __init__(self):
        # 创建 Tkinter 主窗口对象
        # Create a Tkinter root window object
        self.root = tk.Tk()
        # 设置窗口标题为 "Algorithm Visualizer"
        # Set the window title to "Algorithm Visualizer"
        self.root.title("Algorithm Visualizer")
        # 加载算法模块并存储在 self.algorithm_list 中
        # Load algorithm modules and store them in self.algorithm_list
        self.algorithm_list = self.load_algorithms()
        # 创建 Visualizer 实例，传入主窗口对象
        # Create a Visualizer instance, passing the root window object
        self.visualizer = Visualizer(self.root)
        # 设置用户界面（按钮等）
        # Set up the user interface (buttons, etc.)
        self.setup_ui()

    # load_algorithms 方法：动态加载 algorithms 目录下的算法模块
    # load_algorithms method: Dynamically loads algorithm modules from the "algorithms" directory
    def load_algorithms(self):
        # 创建空字典，用于存储算法名称和对应的类
        # Create an empty dictionary to store algorithm names and their corresponding classes
        algorithms = {}
        # 指定算法模块所在的目录
        # Specify the directory where algorithm modules are located
        algo_dir = "algorithms"
        # 遍历 algorithms 目录下的所有文件
        # Iterate over all files in the "algorithms" directory
        for file in os.listdir(algo_dir):
            # 检查文件是否以 .py 结尾，且不是 __init__.py 或 base_algorithm.py
            # Check if the file ends with .py and is neither __init__.py nor base_algorithm.py
            if file.endswith(".py") and file not in ["__init__.py", "base_algorithm.py"]:
                # 提取模块名，去掉 .py 后缀
                # Extract the module name by removing the .py suffix
                module_name = file[:-3]
                try:
                    # 动态导入模块，例如 "algorithms.bubble_sort"
                    # Dynamically import the module, e.g., "algorithms.bubble_sort"
                    module = import_module(f"algorithms.{module_name}")
                    # 获取模块中的类名（首字母大写，去掉下划线，例如 BubbleSort）
                    # Get the class name from the module (capitalized, underscores removed, e.g., BubbleSort)
                    algo_class = getattr(module, module_name.title().replace("_", ""))
                    # 将模块名和类存储到字典中
                    # Store the module name and class in the dictionary
                    algorithms[module_name] = algo_class
                except (ImportError, AttributeError) as e:
                    # 捕获导入或属性错误，打印错误信息并跳过
                    # Catch import or attribute errors, print the error, and skip
                    print(f"Error loading algorithm {module_name}: {e}")
        # 返回算法字典
        # Return the dictionary of algorithms
        return algorithms

    # setup_ui 方法：设置用户界面，创建按钮并绑定算法运行命令
    # setup_ui method: Sets up the user interface, creates buttons, and binds them to algorithm execution commands
    def setup_ui(self):
        # 遍历算法列表，创建对应按钮
        # Iterate over the algorithm list to create corresponding buttons
        for name, algo_class in self.algorithm_list.items():
            # 创建按钮，文本为算法名称（去掉下划线并首字母大写），绑定 run_algorithm 方法
            # Create a button with the algorithm name (underscores removed, title case), binding it to the run_algorithm method
            btn = tk.Button(self.root, text=name.replace("_", "").title(),
                            command=lambda a=algo_class: self.run_algorithm(a))
            # 将按钮添加到界面中，设置 5 像素的垂直间距
            # Add the button to the interface with a 5-pixel vertical padding
            btn.pack(pady=5)
        # 启动 Tkinter 的事件循环，保持窗口运行
        # Start the Tkinter event loop to keep the window running
        self.root.mainloop()

    # run_algorithm 方法：运行选定的算法并启动可视化
    # run_algorithm method: Runs the selected algorithm and starts the visualization
    def run_algorithm(self, algo_class):
        # 定义示例数据（可替换为用户输入）
        # Define example data (can be replaced with user input)
        data = self.load_data()
        try:
            # 使用示例数据实例化算法类
            # Instantiate the algorithm class with the example data
            algorithm = algo_class(data)
            # 调用可视化器的 start 方法，开始展示算法执行过程
            # Call the visualizer's start method to display the algorithm execution process
            self.visualizer.start(algorithm)
        except Exception as e:
            # 捕获运行时的异常，打印错误信息
            # Catch runtime exceptions and print error information
            print(f"Error running algorithm: {e}")

    # load_data 方法：从指定文件中读取数据并转换为整数列表（可选方法，未在当前实现中使用）
    # load_data method: Reads data from a specified file and converts it into a list of integers (optional method, not used in current implementation)
    def load_data(self, filepath="assets/sample_data.txt"):
        # 以只读模式打开文件
        # Open the file in read-only mode
        with open(filepath, "r") as f:
            # 读取文件内容，去除首尾空白字符，按空格分割，并将每个字符串转换为整数
            # Read the file content, strip leading/trailing whitespace, split by spaces, and convert each string to an integer
            data = [int(x) for x in f.read().strip().split(" ")]
        # 返回加载的数据列表
        # Return the loaded data list
        return data
