n = int(input())
sum = 0
i = 1

while (sum < n):
    sum = sum + i
    if (sum >= n):
        break
    i += 1


print(i)