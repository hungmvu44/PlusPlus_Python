# -*- coding: utf-8 -*-
"""Lesson9_Bai05.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ULJijhV1u_QVJSuW1jfDZ98MdfSXGodW
"""



"""Bài 05. Viết hàm
        def count_upper_lower(str)
    trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
"""

def count_upper_lower(string):
  """Count many upper and lower char in string"""
  lower_string, upper_string = 0, 0
  for char in string:
    if char >='a' and char <= 'z':
      lower_string += 1
      
    elif char >= 'A' and char <= 'Z':
      upper_string += 1
  print(f"There are {upper_string} chars and {lower_string} chars in string ")
      


count_upper_lower('Hung Manh Vu')