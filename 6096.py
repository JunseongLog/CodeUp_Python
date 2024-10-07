double_list = []

# 리스트 안에 리스트를 하나씩 추가하면서 입력 받기
# list() 함수를 쓰면, map함수로 값을 모두 int로 바꾼 것을 리스트로 만들어줌
# 리스트로 입력받는 경우, list() 함수를 안쓰면, map함수를 못씀. 문자로 입력 다 받고 나중에 따로 반복문으로 하나씩 int형변환해야함.
for i in range(19):
    double_list.append([])
    double_list[i] = list(map(int, input().split()))


n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        # y좌표만 인덱스 0부터 18까지 값 바꾸기
        if (double_list[x-1][j] == 1):
            double_list[x-1][j] = 0
        else:
            double_list[x-1][j] = 1
        # x좌표만 인덱스 0부터 18까지 값 바꾸기
        if (double_list[j][y-1] == 1):
            double_list[j][y-1] = 0
        else:
            double_list[j][y-1] = 1

# 출력
for i in range(19):
    for j in range(19):
        print(double_list[i][j], end=" ")
    print()