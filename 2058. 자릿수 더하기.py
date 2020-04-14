T = str(input())
sum = 0
for t in range(1,len(T)+1):
    sum += int(T[-t])
print(sum)

#고수의 풀이
print(sum(map(int,input())))
# 대박