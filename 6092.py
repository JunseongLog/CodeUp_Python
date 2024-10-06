result_list = []

# append는 그냥 리스트 뒤에 붙여주는 함수이기 때문에 인덱스 참조 필요없이 단순 횟수 반복만 해도 됨. 
for i in range(23):
    result_list.append(0)

n = int(input())
random_list = input().split()

# 그냥 input으로 리스트를 받아도 각각의 값이 다 문자로 인식하기 때문에 하나씩 정수화 시켜야함
# random_list를 처음에 입력받을때 map함수로 정수형리스트를 받을 수는 없나? - 해보니까 안됨.
for i in range(n):
    random_list[i] = int(random_list[i])

    
# 이게 좀 어려움. range대신 리스트를 사용하면, i에 리스트의 "값"이 차례대로 참조되는 방식임.'
# 이게 출석번호를 부르는 걸 카운트하는 것이기 때문에 "2"번이라고 부르면, list[2-1]값에 저장하고 출력하면 됨.
for i in random_list:
    result_list[i-1] += 1

for i in result_list:
    print(i, end=" ")
