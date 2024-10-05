a, b, c = map(int, input().split())
day = 1
while(not((day % a == 0) and(day % b == 0) and (day % c == 0))):
    day += 1

print(day)

"""
3개의 날이 중복되는 날을 구하는 문제임. 1씩 더하면서 모든 숫자의 나눗셈의 나머지가 0이면
다 베수인 숫자이기 때문에 최소공배수를 구할 수 있음.
"""