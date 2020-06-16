import heapq
# 탐색할 그래프와 시작 정점을 인수로 전달받습니다.
def dijkstra(graph, start, end):
    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성하고, 무한대(inf)로 초기화합니다.
    distances = {vertex: [float('inf'), start] for vertex in graph}

    # 그래프의 시작 정점의 거리는 0으로 초기화 해줌
    distances[start] = [0, start]

    # 모든 정점이 저장될 큐를 생성합니다.
    queue = []

    # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
    heapq.heappush(queue, [distances[start][0], start])

    while queue:

        # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트합니다.
        current_distance, current_vertex = heapq.heappop(queue)

        # 더 짧은 경로가 있다면 무시한다.
        if distances[current_vertex][0] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우에는
            if distance < distances[adjacent][0]:
                # 거리를 업데이트합니다.
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])

    path = end
    path_output = end + '->'
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]
    path_output += start
    print(path_output)
    return distances


# 방향 그래프
mygraph = { 'v1' : {'v2':32, 'v4':17},
        'v2' : {'v1': 32,'v5':45},
        'v3' : {'v4':18,'v7':5},
        'v4' : {'v1':17, 'v3':18,'v5':10, 'v8':3},
        'v5' : {'v2':45,'v4':10,'v6':28,'v9':25},
        'v6' : {'v5':28, 'v10':6},
        'v7' : {'v3':5 ,'v8':59},
        'v8' : {'v4':3, 'v7':59, 'v9':4},
        'v9' : {'v5':25, 'v8':4, 'v10':12},
        'v10' : {'v6':6,'v9':12}}
print(dijkstra(mygraph, 'v1', 'v10'))