T = int(input())
for t in range(1,T+1):
    lis = sorted(list(map(int, input().split())))
    # lis = sorted(lis)

    sum2 = sum(lis[1:len(lis) - 1])
    print('#%d'%t,end=' ')
    print(round(sum2/(len(lis)-2)))

