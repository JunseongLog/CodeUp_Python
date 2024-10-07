double_list = []

# 이차원 리스트 만들기

for i in range(19): # y축 만들기
    double_list.append([])

    for j in range(19): # 각각의 x축 0으로 초기화
        double_list[i].append(0)

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    double_list[x-1][y-1] = 1


for i in range(19):
    for j in range(19):
        print(double_list[i][j], end=" ")
    # 개행은 그냥 "print()"로 쓸 수 있는 듯    
    print()


