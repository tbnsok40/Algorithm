
# base 개념은 이러하다
# names = input()
# for idx,val in enumerate(names):
#
#     print(idx+1,val,end=' ')
#     for i in val:
#         print(ord(i)-64,end=',')
#     print()

# 문제를 풀어보자
# input을 받자
alphabet = (input())
for i in alphabet:
    print(ord(i)-64, end=" ")

# ord() 메서드는 alphabet의 아스키코드 return
# 그에 맞춰서 64를 빼준다.



