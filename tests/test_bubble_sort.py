#
#  test_bubble_sort.py
#  AlgoVisual
#
#  Created by Z. Steve on 2025/3/23 22:00.
#
import unittest
from algorithms.bubble_sort import BubbleSort

class TestBubbleSort(unittest.TestCase):
    def test_sorting(self):
        data = [5, 2, 8, 1, 9]
        algo = BubbleSort(data)
        sorted_data = list(algo.run())[-1]  # 取最后一步的结果
        self.assertEqual(sorted_data, [1, 2, 5, 8, 9])

    def test_empty_list(self):
        data = []
        algo = BubbleSort(data)
        sorted_data = list(algo.run())[-1]
        self.assertEqual(sorted_data, [])

if __name__ == '__main__':
    unittest.main()