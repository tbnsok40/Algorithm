letter = sorted(input())
# print(letter)
sum = 1
tmp = 0
for i in range(len(letter)-1):

    if letter[i] == letter[i+1]:
        sum += 1
    else:
        if tmp < sum:
            tmp = sum
            answer = letter[i]
        if tmp == sum:
            answer = '?'
        sum = 1

print(answer.upper())