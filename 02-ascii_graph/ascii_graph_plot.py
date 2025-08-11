from collections import deque
from math import isclose, pi, sin

# ____그래프를 그리기 위한 설정______________________

start = -10
end = 10.3
gap = 0.25

count = (end - start) / gap

x_i = [start + gap * i for i in range(int(count))]
print(x_i)


y__ = [round(sin(xx), 1) for xx in x_i]
y_k = list(set(y__))
y_k.sort(reverse=True)
print(y_k)

# ____그래프_________________________________________
# x축

x_ = ["+----------------"] * 4
x_result = deque(x_)
x_result.append("++")
x_result.appendleft("+")

abscissa = "".join(x_result)
print(abscissa)


# y축
ordinate = ["++", "+"] + ["++", "|"] * 8 + ["++", "+", "++"]
print(ordinate)
print()


for index_y, y in enumerate(y_k):
    if index_y % 2 == 0:
        graph = "{:>4}{:>3}".format(round(y, 1), ordinate[index_y])
    else:
        graph = "{:>6}{:>1}".format(ordinate[index_y], "")

    for index_x, x in enumerate(x_i):
        x_about = round(sin(x), 1)

        if isclose(x_about, y, abs_tol=1e-9):
            graph += "*"

        elif index_y == 0:
            graph += "-"
        elif index_y == len(y_k) - 1:
            graph += "-"

        else:
            graph += " "

    if index_y % 2 == 0:
        graph += ordinate[index_y]
    else:
        graph += ordinate[index_y]

    print(graph)

# y축

under_num = list(range(-5, 11, 5))
print("{:>7.0f}".format(-10), end="")
for h in under_num:
    print("{:>21.0f}".format(h), end="")
print()
