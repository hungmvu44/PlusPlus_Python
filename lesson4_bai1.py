# -*- coding: utf-8 -*-
"""Lesson4_Bai1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15DHIY9LdcsNtJkljGAcM0E2ullOu_wAL
"""

Bài 01. Lập chương trình thực hiện công việc sau:
    1. Nhập ba số a, b, c bất kì từ bàn phím
    2. Giải nghiệm phương trình bậc 2: ax^2 + bx + c = 0  (Xét tất cả các trường hợp có thể xảy ra)

Bài 01. Lập chương trình thực hiện công việc sau:
    1. Nhập ba số a, b, c bất kì từ bàn phím
    2. Giải nghiệm phương trình bậc 2: ax^2 + bx + c = 0  (Xét tất cả các trường hợp có thể xảy ra)

import math
a = float(input("Enter number a: "))
if a != 0 :
  b = float(input("Enter number b: "))
  c = float(input("Enter number c: "))
  delta = math.pow(b,2)- 4* (a*c)
  if delta > 0:
    x1 = float((-b + math.sqrt(delta)) / (2 *a))
    x1 = float((-b - math.sqrt(delta)) / (2 *a))
  elif delta == 0:
    print("Phuong trinh nghiem kep")
  else:
    print("Phuong trinh vo nghiem")
elif a == 0 and b == 0 and c == 0:
  print("phuong trinh vo nghiem")