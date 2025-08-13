from math import sin

start = -10
end = 10.3
gap = 0.25

x_i = [start + gap * i for i in range(int((end - start) / gap))]

y__ = [round(sin(k), 1) for k in x_i]
y_k = list(set(y__))
y_k.sort(reverse=True)

# 그래프 틀
y_left = ["++", "+ "] + ["++", "| "] * 8 + ["++", "+ ", "++"]
y_right = ["++", " +"] + ["++", " |"] * 8 + ["++", " +", "++"]
ordinate1 = "".join(y_left)
ordinate2 = "".join(y_right)

# ' '으로 채워진 빈 이중 list
graph = [[" " for width in range(len(x_i))] for length in range(len(y_k))]

high = len(y_k)  # 중복되는 y값 제외한 값 개수: 21개(1.0 ~ -1.0)
width = len(x_i)  # 출력되는 x값 개수: 81개
y_max = 1.0
y_min = -1.0

xy_list = [[x, y] for x, y in zip(x_i, y__)]  # x와 y가 일대일 대응 됨.


# x값에 대한 인덱스 구하는 함수
def index_x(x):
    return int(abs(start - x) / gap)


# y값에 대한 인덱스 구하는 함수
def index_y(y):
    return int(round((high - 1) / (y_max - y_min) * (y_max - y), 1))


# y인덱스와 그에 맞는 x 인덱스 위치에 'x' 찍음: list 속 list
for x, y in xy_list:
    row = index_y(y)  # y축 index
    col = index_x(x)  # x축 index
    graph[row][0] = ordinate1[row * 2 : 2 + row * 2]

    graph[0][col] = "-"
    graph[20][col] = "-"

    graph[0][80] = "++"
    graph[20][80] = "++"

    graph[row][80] = ordinate2[row * 2 : 2 + row * 2]
    graph[row][col] = "x"
    graph[1][64:77] = "sin(x) xxxxxx"


for i in range(len(graph)):
    if i % 2 == 0:
        y_num = "{:>4.1f} ".format(y_k[i])
        print(y_num, end="")
    else:
        print("     ", end="")
    print("".join(graph[i]))


# x축 숫자
print("      ", end="")
for x, y in xy_list:
    if index_x(x) % 20 == 0:  # index_x(x)%20==0 은 range(-10,11,5) 와 동일한 결과 출력
        print("{:<20d}".format(int(x)), end="")
print()
