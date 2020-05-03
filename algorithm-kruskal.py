parent = dict()
rank = dict()
graph ={
    'vertices': ['v1','v2','v3','v4','v5'],
    'edges' : [(1,'v1','v2'),
               (3,'v1','v3'),
               (1,'v2','v1'),
               (3,'v2','v3'),
               (6,'v2','v4'),
               (3,'v3','v1'),
               (3,'v3','v2'),
               (4,'v3','v4'),
               (6,'v4','v2'),
               (4,'v4','v3'),
               (5,'v4','v5'),
               (2,'v5','v3'),
               (5,'v5','v4')]
}

def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph):
    mst = list()

    # 1. 초기화
    for node in graph['vertices']:
        make_set(node)

    # 2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    # 3. 간선 연결 (사이클 없는)
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst

print(kruskal(graph))