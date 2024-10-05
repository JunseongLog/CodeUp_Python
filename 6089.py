start, gap, order = map(int, input().split())

sum = start

for i in range(1, order):
    sum *= gap

print(sum)