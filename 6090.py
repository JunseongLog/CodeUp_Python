start, gap, plus, order = map(int, input().split())

sum = start

for i in range(1, order):
    sum = (sum * gap) + plus 

print(sum)