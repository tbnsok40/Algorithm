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
    # p행렬(number x number) 생성
    # p = []
    # a = [0 for i in range(number)]
    # for j in range(number):
    #     p.append(a)

    # 여기가 문제였네(위에 코드) 여기서 뭐가 오류가 났는지,,,p가 엉망으로 나왔는데, p를 그냥 함수의 인자로 받으니까 바로 해결된다.

    for k in range(number): # 중간에 거치는 노드
        for i in range(number): # 출발 노드
            for j in range(number): # 목적지 노드
                if arr[i][k] + arr[k][j] < arr[i][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]
                    p[i][j] = k
                    # print('%s 번째'%k, p[i][j])

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