# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 12:00:00 2025

@author: ascii_sin(x) 함수
"""

from math import isclose, pi, sin


x_i = [
    0,
    pi / 6,
    pi / 4,
    pi / 3,
    pi / 2,
    2 * pi / 3,
    3 * pi / 4,
    5 * pi / 6,
    pi,
    7 * pi / 6,
    5 * pi / 4,
    4 * pi / 3,
    3 * pi / 2,
    5 * pi / 3,
    7 * pi / 4,
    11 * pi / 6,
    2 * pi,
]


y_k = [sin(k) for k in x_i]
y_k.sort(reverse=True)

print("{:^50}".format("< 202401009 정선경_ ascii graph 그리기 >"))

for index_y, y in enumerate(y_k):
    if index_y % 2 == 0:
        if index_y == 8:
            graph = "{:>4}{:>3}".format(round(y, 1), "++")
        else:
            graph = "{:>4}{:>3}".format(round(y, 1), "++")  # y축 왼쪽 그래프틀(정렬)
    else:
        graph = "{:>7}".format("|")

    for index_x, x in enumerate(x_i):
        if isclose(sin(x), y, abs_tol=0.001):  # abs_tol 절대허용오차: 0.1%
            if index_y % 2 == 0:
                if (
                    isclose(x, 0, abs_tol=0.001)
                    or isclose(x, pi, abs_tol=0.001)
                    or isclose(x, 2 * pi, abs_tol=0.001)
                ):
                    graph += "**"
                else:
                    graph += "*"
        elif abs(y) == 1:
            graph += "---"

        elif y == 0:
            graph += "---"

        elif index_y == 1:  # sin 마크 표시
            if index_x == 10:
                graph = "{:>6}{:>50}".format("|", "sin(x)  |")

        else:
            if index_y % 2 == 1:
                graph = "{:>6}{:>50}".format("|", "|")
            graph += "   "

    if index_y % 2 == 0:
        if index_y == 8:
            graph += "+"
        else:
            graph += "++"
    print(graph)

# x축 라벨
print("{:9.1f}".format(0.0), end="")
for id_x, x_label in enumerate(x_i):
    if id_x % 2 == 0 and x_label != 0:
        print("{:6.1f}".format(x_label), end="")
