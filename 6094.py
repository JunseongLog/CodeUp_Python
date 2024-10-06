n = int(input())
num_list = input().split()

for i in range(n):
    num_list[i] = int(num_list[i])


print(min(num_list))