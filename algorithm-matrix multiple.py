import sys

d = [7, 2, 3, 2, 6]
M = [[0 for x in range(5)] for y in range(5)]
for diag in range(1, 5):
    for i in range(1, 5 - diag):
        j = i + diag
        M[i][j] = sys.maxsize
        for k in range(i, j):

            if M[i][j] > (M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j]):
                print('k: ',k)
            print('minimum is',min(M[i][j], M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j]))

            M[i][j] = min(M[i][j],M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j]) # min안의 M[i][j]는 이전 단계 루프에서 저장된 값
            print('i: %d'%i, 'j: %d'%j)



for j in range(1,len(M[0])):
    for i in range(1,len(M[0])):
        print('%6d' %M[j][i], end=' ')
    print()
    print()

# 이건 결과값만 나오게하고, 과정을 몰라.
# 최소로 곱하는 결과값만 알뿐,