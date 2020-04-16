N = int(input())

for n in range(1, N+1):
    n = str(n)
    dec = n[:-1]
    one = n[-1]

    if dec =='3' or dec == '6' or dec == '9':
        if one == '3' or one == '6' or one == '9':
            print("--", end=' ')
            continue
        print("-", end=' ')
        continue

    if one =='3' or one == '6' or one == '9':
        print("-", end=' ')
        continue

    else:
        print(n, end = ' ')

    # if ('3' in n) or ('6' in n) or ('9' in n):
    #     print("-", end=' ')
    #
    # else:
    #     print(n, end=' ')

# 3,6,9가 여러번 나올 때 어떻게 처리
# 두번 혹은 세번 나오는게 다야