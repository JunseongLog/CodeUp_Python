n = int(input())
num_list = input().split()

for i in range(n):
    num_list[i] = int(num_list[i])

# reverse()는 리스트를 역순으로 바꾸는 함수
num_list.reverse()

for i in num_list:
    print(i, end=" ")
