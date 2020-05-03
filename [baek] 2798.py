# N = [5,6,7,8,9]
N = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]
max = 500
min = 999999
for i in range(len(N)-2):
    for j in range(i+1,len(N)-1):
        for k in range(j + 1, len(N)):
            sum = N[i] + N[j] + N[k]
            diff = max - sum
            if diff < 0:
                continue
            if min >= diff:
                min = diff
                final_sum = sum
print(final_sum)


