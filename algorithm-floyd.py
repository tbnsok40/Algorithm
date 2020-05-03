number = int(input())
inf = 10000000 # inf: infinity는 대략 10만으로 선언
arr = [[0,4,inf,inf,inf,10,inf],
       [3,0,inf,18,inf,inf,inf],
       [inf,6,0,inf,inf,inf,inf],
       [inf,5,15,0,2,19,5],
       [inf,inf,12,1,0,inf,inf],
       [inf,inf,inf,inf,inf,0,10],
       [inf,inf,inf,8,inf,inf,0]] #기존 D행렬(7x7)

p = [[0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0]]

##################################### 중요 #####################################
# p = []
# a = [0 for i in range(number)]
# for j in range(number):
#     p.append(a)
#     # 파이썬 pointer문제, append 되는 a가 모두 같은 놈들이기 때문에 오류가 발생한 것
# print(p)
##################################### 중요 #####################################

def floyd(arr,p):
    for k in range(number): # 중간에 거치는 노드
        for i in range(number): # 출발 노드
            for j in range(number): # 목적지 노드
                if arr[i][k] + arr[k][j] < arr[i][j]: # 이게 좌변이 더 작다는 것은, i에서j를 바로 가는 것보다 k를 거쳐가는 것이 더 짧다는 뜻
                    # 그리고 중간에 거치는 노드가 꼭 하나라는 보장이 없다. 2개 이상일 수도 있는데,
                    arr[i][j] = arr[i][k] + arr[k][j]
                    p[i][j] = k # (0,0)부터 (num,num)까지 차례로 올라가면서, 거쳐가는 k를 저장한다.즉 i에서j를 가는데 k를 거쳐야한다면 P배열에 저장한다.
                    # 근데 노드를 2개 거쳐서 갈 수도 있자나. 하지만 k가 가장 바깥 루프에 존재하기에 결국 가장 큰 k 노드가 p행렬에 저장된다. 즉 거쳐야하는 노드 중 가장 인덱스가 높은 값이 저장된다.

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

def path(s,d):
    if(p[s][d] != 0):
        path(s, p[s][d])
        print('→',p[s][d])
        path(p[s][d], d)

floyd(arr,p)
path(6,2)