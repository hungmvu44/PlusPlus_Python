# -*- coding: utf-8 -*-
"""Lesson7_Bai11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GTqa7PiP3DxkgoSBuM9ejASFbZfeBHXT
"""



"""Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím."""

str = input("Enter the string: ").split()
print(str)
longest_word = str[0]
for word in str:
  if longest_word < word:
    longest_word = word
print(f"the longest word of string is : {longest_word}")