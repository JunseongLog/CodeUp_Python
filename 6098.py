# 빈 리스트 하나 만들기
ant_list = []

# 이차원 리스트로 입력받기
for i in range(10):
    ant_list.append([])
    ant_list[i] = list(map(int, input().split()))

x = 1
y = 1

while(True):
    
    # 반복이 끝나는 경우
    if (ant_list[x][y+1] == 1 and ant_list[x+1][y] == 1): # 둘 다 막혀있는 경우
        ant_list[x][y] = 9
        break
    elif (ant_list[x][y+1] == 2): # 오른쪽에 먹이(2)가 있는 경우
        ant_list[x][y+1] = 9
        break
    elif (ant_list[x+1][y] == 2 and ant_list[x][y+1] == 1): # 왼쪽에 먹이(2)가 있는 경우
        ant_list[x+1][y] = 9
        break
    elif (x ==  8 and y == 8): # 끝점에 도달한 경우
        ant_list[8][8] = 9
        break


    # 진행 코드 [시작점]
    if (ant_list[x][y] == 0):
        ant_list[x][y] = 9
    elif (ant_list[x][y] == 1):
        break
    elif (ant_list[x][y] == 2):
        ant_list[x][y] = 9
        break


    # 진행 코드 [시작점 이후]
    if (ant_list[x][y+1] == 0):
        ant_list[x][y+1] = 9 
        y += 1
    elif (ant_list[x][y+1] == 1 and ant_list[x+1][y] == 0):
        ant_list[x+1][y] = 9
        x += 1
    
# 출력     
for i in range(10):
    for j in range(10):
        print(ant_list[i][j], end=" ")
    print()

