# -*- coding: utf-8 -*-
"""Lesson9_Bai02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1surLI-GvVOnRvUvg4o4M8-tTYE8BiDiS
"""



"""Bài 02. Viết hàm
        def reverse_string(str)
 trả lại chuỗi đảo ngược của chuỗi str 
"""

def reverse_string(string):
  str1 = ""
  for char in string:
    str1 = char + str1
  return str1


reverse_string('hungmanhvu')