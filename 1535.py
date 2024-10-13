def max(num_list):
    order = 0
    for i in range(n):
        
        max_number = num_list[0]
        if (num_list[i] > max_number ):
            max_number = num_list[i]
            order = i + 1
    
    return order

n = int(input())
num_list = []
num_list = list(map(int, input().split()))

print(max(num_list))

