T = int(input())
for t in range(1,T+1):

    N,m = map(int, input().split())

    lis = []
    for l in range(N):
        n = list(map(int, input().split()))
        lis.append(n)

    max = -1
    for c in range(0, (N - m) + 1):
        for r in range(0, (N - m) + 1):

            box = 0
            for sr in range(r, r + m):
                box += (sum(lis[sr][c:c + m]))
            if max < box:
                max = box

    print('#%d' %t, max)
#
# # 첫번째 오류: index를 하나만 설정하여, 작은 사각형이 대각선으로만 움직임
# # 두번째 오류: 작은 사각형의 꼭지점은 설정했지만 그 사이의 원소들은 생각못함