# -*- coding: utf-8 -*-
"""Lesson8_Bai00.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11sfYuOVQAfRsKW9R-cAORfXgLWk2u3tO
"""



"""Bài 00. Viết chương trình tính tích value của các phần tử trong một dict"""

my_dict = {
    1 : 3,
    2 : 5,
    3 : 6,
    4 : 10,
}
tich = 1
for value in my_dict.values():
  tich = tich * value
print(f"The multiplication of value is {value}")