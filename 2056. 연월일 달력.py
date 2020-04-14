T = int(input())

# inputs = map(int, input().split())
# li = []
# li.append(inputs)
# # li = list((inputs))
# print(li)

for t in range(1,T+1):
    li = input()
    year = int(li[0:4])
    month = int(li[4:6])
    day = int(li[6:8])

    print('#%d'%t, end=' ')
    if (1 <= month <= 12):
        if month == 2:
            if not (1<= day <= 28):
                print(-1)

            else:
                print('%s/%s/%s' % (li[0:4], li[4:6], li[6:8]))


        else:
            if not (1 <= day <= 31):
                print(-1)
                break

            else:
                print('%s/%s/%s' % (li[0:4], li[4:6], li[6:8]))
    else:
        print(-1)

# li = input()
# year = int(li[0:4])
# month = int(li[4:6])
# day = int(li[6:8])
# print('%s/%s/%s' %(li[0:4], li[4:6], li[6:8]))
# print('%d/%d/%d' %year %month %day) //이래서 틀렸음


# 저게 엔터를 치고 한번씩 들어가는 거니까, 5번 입력되게 for문 안에 넣으면 돼