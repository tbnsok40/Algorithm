number = int(input())
inf = 100000 # inf: infinity는 대략 10만으로 선언
arr = [[0,4,inf,inf,inf,10,inf],
       [3,0,inf,18,inf,inf,inf],
       [inf,6,0,inf,inf,inf,inf],
       [inf,5,15,0,2,19,5],
       [inf,inf,12,1,0,inf,inf],
       [inf,inf,inf,inf,inf,0,10],
       [inf,inf,inf,8,inf,inf,0]] #기존 D행렬(7x7)

def floyd(arr):
    # p행렬(number x number) 생성
    p = []
    a = [0 for i in range(number)]
    for j in range(number):
        p.append(a)

    print('Original p 행렬:')
    for i in range(number):
        for j in range(number):
            print('%2d' %p[i][j], end=' ')
        print('\n')

    for k in range(number): # 중간에 거치는 노드
        for i in range(number): # 출발 노드
            for j in range(number): # 목적지 노드
                if arr[i][k] + arr[k][j] < arr[i][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]
                    p[i][j] = k

    print('arr 행렬:')
    for i in range(number):
        for j in range(number):
            print('%2d' %arr[i][j], end=' ')
        print('\n')

    print('수정된 p 행렬:')
    for i in range(number):
        for j in range(number):
            print('%2d' %p[i][j], end=' ')
        print('\n')
floyd(arr)
