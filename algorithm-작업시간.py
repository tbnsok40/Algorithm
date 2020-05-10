
dictionary = {i:int(t) for i, t in (input().split() for _ in range(4))}


print(dictionary)
# 이문제는 딕셔너리 접근 괜찮나? value(작업시간)은 중복되어도 상관없으니까?

import operator
sdict= sorted(dictionary.items(), key=operator.itemgetter(1))
print(sdict)
