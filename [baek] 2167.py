N, M = map(int, input().split())

a = []
for _ in range(N):
    li = list(map(int, input().split()))
    a.append(li)

num = int(input())
for _ in range(num):
    i,j,x,y = map(int, input().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1
    sum = 0

    for n in range(i, x+1):
        for m in range(j, y+1):
            sum += a[n][m]
            # print(n,m,sum)
    print('sum: ',sum)


