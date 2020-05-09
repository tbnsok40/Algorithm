# N = 1 일 때 케이스 생각해주어야 한다.
# test = int(input())
N = int(input())
arr = [0]
for _ in range(N):
    arr.append(int(input()))
print(arr)
cnt = 0
for i in range(N+1):
    cnt += 1

    if arr[i] == N:
        print(arr[i-1])
        break
    else:
        pass

