start, gap, order = map(int, input().split())

sum = start

for i in range(1, order+1):
    sum += gap

print(sum - gap)