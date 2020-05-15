# a, b = map(int,input().split())
# 노소수 = list()
# 소수 = list()
# for j in range(a,b+1):
#     for i in range(2,j):
#         if (j % i) == 0:
#             노소수.append(j) #여기 들어간 j는 소수다.?
#             break
#     else:
#         소수.append(j)
#
# # 1. 소수가 아닌 것들 판별(소수가 아닌 애들이 후보)
# # 2. 얘들은 소인수분해했을때 x개의 소인수가 나오는데, 그 x가 소수여야한다.
# # 3. 그럼 이 x에 대해서 step1에서 했던 검사를 해주면 되는데, 처음 step1에서 메모리제이션을 해주면 어떨까?
# print(노소수)
# print(소수)
# count =0
# answer = []
# for i in range(len(노소수)):
#     a = 노소수[i]
#     for j in range(2,a):
#         if a // j ==0:
#             if a // j*j == 0:
#                 count += 2
#                 continue
#             count +=1
#     if count in 소수:
#         answer.append(a)

# n번의 논문 제출: len(n)
n = int(input())
papers =list(map(int, input().split()))
# for _ in range(n):
#     papers.append(int(input()))
# [8, 4, 5, 3, 10]
# [3,4,5,8,10]
papers = sorted(papers)
# step1) k번 이상 인용된 논물이 k편 이상: n[i] > n[j] ==> count ++ ==> count <= k
# for i in range(n):
#     for j in range(papers[i+1:]):
#         if papers[i] < j:
#             count += 1
#             # if count == papers[i]:
#             #     break
#     if count >= papers[i]: #step1 충족
#
#         for k in range(papers[:i]):
#             if k
#


qindex = 0
# step2) 나머지 n-k(>=0)편의 논문들 인용횟수가 k이하이면 인덱스는 k.
for i in range(n):
    print(i)
    if papers[i] <= len(papers[i:]): #step1 satisfied
        print(papers[i], papers[i:])
        for j in (papers[:i]):
            print('papers[:%d],'%i ,papers[:i])
            print('j:',j)
            if j <= papers[i]:
                qindex = papers[i]
                print('qindex:',qindex)
print(qindex)
print(papers)