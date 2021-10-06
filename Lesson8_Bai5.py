{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Lesson8_Bai5.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyN/Qma+roofUGG6RyMUOlfG",
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
        "<a href=\"https://colab.research.google.com/github/hungmvu44/PlusPlus_Python/blob/main/Lesson8_Bai5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rNiaWxNlvUSM"
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
        "id": "xtRb5Cvfvnns"
      },
      "source": [
        "Bài 05. Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9dFYThA9vqYE",
        "outputId": "244de33f-f466-4b0f-a6ca-05bf99c358e2"
      },
      "source": [
        "sampleDict = {\"name\": \"Kelly\",\n",
        "              \"age\":25,\n",
        "              \"salary\": 8000,\n",
        "              \"city\": \"New york\"\n",
        "}\n",
        "keys = ['name','salary']\n",
        "result = {k: sampleDict[k] for k in keys}\n",
        "print(result)\n",
        "\n",
        "\n",
        "  \n"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'name': 'Kelly', 'salary': 8000}\n"
          ]
        }
      ]
    }
  ]
}