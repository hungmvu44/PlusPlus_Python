# -*- coding: utf-8 -*-
"""Lesson6_Bai00.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hfhwZ2vDrY2NttCmcxl7WC5wxGaVRWUi
"""



"""Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.

"""

import random

my_list = [1,10,50,40,23,46,87,12]

my_random_list = random.sample(my_list, 5)
print(f"new list which contains 5 numbers are: {my_random_list}")

