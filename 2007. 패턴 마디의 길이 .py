
for t in range(1,int(input())+1):
    sentences =input()
    print('#%d'%t,end=' ')
    for n in range(1,10):
        if sentences[:n] == sentences[n:n+n]:
            print(n)
            break
    continue
