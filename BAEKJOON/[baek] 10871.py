a, b = map(int, input().split())
# num_list = list()
num_list = list(map(int, input().split()))
for i in range(len(num_list)):
    if b > num_list[i]:
        print(num_list[i], end=' ')