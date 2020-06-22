class Tree(object):
    def __init__(self, x, l=None, r=None):
        self.x = x
        self.l = l
        self.r = r
T = Tree(4, Tree(5, Tree(4, Tree(5))), Tree(6, Tree(1), Tree(6)))


def solution(T):
    distinct = {1: set([])}
    stack = [(T, [T], set([T.x]))] # 말 그대로 스택, [T]는 리스트...이건 왜 필요하지?
    i = 1  # number of path
    while stack:  # DFS
        tree, path, value = stack.pop()
        if (tree.l == None) and (tree.r == None):  # leaf node
            # 이 조건은, 자식 노드가 아무것도 없는 노드에 해당

            print('i: ', i, 'value: ', value)
            distinct[i] = value # value는 set으로 중복된 값이 없는 집합이다.
            i += 1 # 즉, dfs 에서 하나의 깊이를 다 팠으니, 다른 깊이(가지)로 넘어간다는 뜻
        else:
            if tree.r != None:
                print('tree.r.x:',set([tree.r.x]))
                stack.append((tree.r, path + [tree.r], value | set([tree.r.x])))

            # 아래 조건이, elif 나 else 가 아닌 이유는 곧, 위의 조건문과 상관없다는 뜻
            if tree.l != None:
                print('tree.l.x: ',set([tree.l.x]))
                stack.append((tree.l, path + [tree.l], value | set([tree.l.x])))

    answer = 1
    for key in distinct.keys():
        temp = len(distinct[key])
        if temp > answer:
            answer = temp
    print('distinct: ', distinct)
    return answer

print(solution(T))

# # stack=[(1,3,4)]
# # print(type(stack[0])) # this is Tuple, 이 스택은 튜플을 저장한다. 그 튜플에는 tree, path, value가 포함돼있다.