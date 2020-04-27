class Tree(object):
    def __init__(self, i):
        self.left = None
        self.right = None
        self.data = None

def optimalBST_build(i,j,R, keys):
    k = R[i][j]
    if k == 0:
        return
    else:
        node = Tree(keys[k-1])
        node.left = optimalBST_build(i,k-1,R,keys)
        node.right = optimalBST_build(k+1, j, R, keys)
        return node

def optsearchtree(n,p):
    A = [[0 for x in range(0, n+1)]for y in range(0,n+2)]
    R = [[0 for x in range(0, n+1)] for y in range(0, n + 2)]

    for i in range(1,n+1):
        A[i-1][i] = 0
        A[i][i] = p[i]
        R[i][i] = i
        R[i-1][i] = 0

    for diagonal in range(1, n):
        for i in range(1, n-diagonal+1):
            j = i + diagonal
            minval = 999999
            for k in range(i, j+1):
                if (A[i][k-1] + A[k+1][j]) < minval:
                    minval = A[i][k-1] + A[k+1][j]
                    k_min = k
            R[i][j] = k_min
            sum = p[i]
            for s in range(i+1, j+1):
                sum = sum + p[s]
            A[i][j] = minval + sum

    optimalBST_build(1,3,R,['don','isabelle','ralph','wally'])

    return A, R
print(optsearchtree(4, [0, 3/8, 3/8, 1/8, 1/8]))

