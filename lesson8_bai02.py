# -*- coding: utf-8 -*-
"""Lesson8_Bai02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UE9rigBiA4gfu5hGyyiabvAgvj8-Y96J
"""



"""Bài 02. Viết chương trình tìm ra top 3 phần tử của dict có key lớn nhất"""

my_dict = {
    1: 3,
    2: 4,
    3: 9,
    10: 11,
    5: 20
}

top3key = sorted(my_dict, key = my_dict.get, reverse = True)[:3]
print(top3key)

