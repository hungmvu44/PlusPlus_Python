{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Lesson8_Bai07.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyN+R7kPzHw9DyfUvgnei4Ka",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/hungmvu44/PlusPlus_Python/blob/main/Lesson8_Bai07.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qR9wVJE4_TuH"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dcnSqfE2_V95"
      },
      "source": [
        "Bài 07. Viết hàm đếm số lần xuất hiện các ký tự trong một String"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R_vGQNQx_Wnz",
        "outputId": "10a8cef6-903e-4b0b-dcac-b2bd78be36b9"
      },
      "source": [
        "str = input(\"Enter the string: \")\n",
        "\n",
        "dict1 = {}\n",
        "for char in str:\n",
        "  my_dict = dict1.values()\n",
        "  if char in my_dict:\n",
        "    dict1[char] += 1\n",
        "  else:\n",
        "    dict1[char] = 1\n",
        "print(dict1) \n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the string: trang dep gai\n",
            "{'t': 1, 'r': 1, 'a': 1, 'n': 1, 'g': 1, ' ': 1, 'd': 1, 'e': 1, 'p': 1, 'i': 1}\n"
          ]
        }
      ]
    }
  ]
}