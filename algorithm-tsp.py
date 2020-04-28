# 얘는 다시 출발점으로 돌아오는 최소경로를 구하는 것
# 출발점으로 돌아오지 않는 것은 어떻게 설계할 것인지.
def tsp(dists):
    N = len(dists)
    VISITED_ALL = (1 << N) - 1
    cache = [[None] * (1 << N) for _ in range(N)]
    INF = float('inf')

    def find_path(last, visited):
        if visited == VISITED_ALL:
            return dists[last][0] or INF

        if cache[last][visited] is not None:
            return cache[last][visited]

        tmp = INF
        for city in range(N):
            if visited & (1 << city) == 0 and dists[last][city] != 0:
                tmp = min(tmp,
                          find_path(city, visited | (1 << city)) + dists[last][city])

        cache[last][visited] = tmp
        return tmp

    return find_path(0, 1 << 0)

dists = [[0,20,28,30],[25,0,27,28],[30,35,0,29],[280,29,27,0]]
print(tsp(dists))


# 아래 코드는 출발점에서 출발하여 모든 노드를 다 순회하는 알고리즘(출발점으로 돌아오지 않는다.)
# 출발점으로 돌아오게 하려면 어떻게 할 것인가
def tsp(node, costSum, count):
    visited[node] = True
    city[count-1] = node;
    min = -1
    if count == N:
        for i in range(N):
            print('%d' %city[i], end=' ')
        print(' : %d' %costSum)
        visited[node] = False
        city[count -1] = -1


    for i in range(N):
        if (visited[i] == False) & (W[node][i] != 0 ):
            tsp(i, costSum + W[node][i], count + 1)
    visited[node] = False
    city[count - 1] = -1

N = int(input())


for i in range(N):
    visited = [False,False,False,False]
    city = [-1,-1,-1,-1]
    W = [[0,20,28,30],[25,0,27,28],[30,35,0,29],[280,29,27,0]]
    (tsp(i, 0, 1))

    print()