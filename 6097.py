# 리스트 하나 만들기
double_list = []

# 리스트 크기 받기
h, w = map(int, input().split())

# 리스트 크기 만큼 0으로 초기화
for i in range(h):
    double_list.append([])
    for j in range(w):
        double_list[i].append(0)

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())

    for j in range(l):
        if (d == 0):
            double_list[x-1][y-1+j] = 1
        else:
            double_list[x-1+j][y-1] = 1

# 출력
for i in range(h):
    for j in range(w):
        print(double_list[i][j], end=" ")
    print()