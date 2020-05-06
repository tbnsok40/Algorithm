# # li = ['ji','ga','mi','ji','my','ji','ga']
# #
# # W = 20
# # L = -15
# # dict = {
# # }
# #
# # name, wl = (input().split())
# # if wl == 'W':
# #     wl = 20
# # else:
# #     wl = -15
# #
# # dict.setdefault(name, wl)
# # print(dict)
#
dict={}
N, P = input().split()
W, L, max = input().split()
for n in range(int(P)):
    name, wl = (input().split())
    if wl == 'W':
        wl = 20
    else:
        wl = -15
    dict.setdefault(name,wl)

sum = 0
li = []
for n in range(int(N)):
    name = input()
    li.append(name)

for i in range(len(li)):
    name = str(li[i])

    if name in dict:
        sum += dict[name]

        if sum == 100:
            print('I AM NOT IRONMAN!!')
            break
        else:
            if sum < 0:
                sum = 0
            else:
                if i == (len(li) - 1):
                    print('I AM IRONMAN!!')


    else:
        sum = sum - 15
        if sum < 0:
            sum = 0

        if i == (len(li) - 1):
            print('I AM IRONMAN!!')
