# -*- coding: utf-8 -*-
"""Lesson7_Bai08.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1agP8Km7y57sQxJ-vXn_vt87hKf6apl4W
"""



"""Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không."""

a = (1, 3, 5, 6, 7)
b = (1, 4, 6, 5, 10)

for item in a:
  if item in b:
    print(f"duplicate items of 2 tuple are : {item}")