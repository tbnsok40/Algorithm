
T = int(input())

# arr = []
# arr.append(int(input().split()))
#
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
#     # ///////////////////////////////////////////////////////////////////////////////////
#
# arr = sorted(arr)
# mid = len(arr) // 2
# print(arr[mid])
#
#
#     # ///////////////////////////////////////////////////////////////////////////////////

inputs = map(int, input().split())
arr = sorted(list(inputs))
mid = len(arr) // 2
print(arr[mid])
