N = int(input())
for n in range(N):
    problem_num = int(input())
    lis = sorted(list(map(int, input().split())))
    max, sum = -1, 1
    for i in range(len(lis) - 1):
        if lis[i] == lis[i + 1]:
            sum += 1

            if max < sum:
                max = sum
                num = lis[i]

            elif max == sum:
                num = lis[i]



        else:
            sum = 1

    print('#%d' %problem_num, end = ' ')
    print(num)

# 최빈수가 여러개면 더 높은 점수를 출력해야한다.


# lis = sorted(list(map(int, input().split())))
# max, sum = -1, 1
#
#
# for i in range(len(lis)-1):
#     if lis[i] == lis[i+1]:
#         sum += 1
#
#         if max < sum:
#             max = sum
#             num = lis[i]
#
#     else:
#         sum = 1
# print(max, num)
#
