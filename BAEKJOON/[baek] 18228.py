# Num = int(input())
# lists = list(map(int, input().split()))
# for i in range(len(lists)):
#     if lists[i] == -1:
#         index = i
# left = min(lists[:index])
# right = min(lists[index+1:])
# print(left+right)


name, gender_pref, max_dist = input().split()
max_dist = int(max_dist)
# if gender_pref == 'MF' or 'FM':
#     gender_pref = 'MF'

answer = []
for _ in range(int(input())):
    partners_name, gender, dist = input().split()
    # if gender == 'MF' or 'FM':
    #     gender = 'MF'
    dist = int(dist)
    if ((gender_pref == gender) or (gender in gender_pref)) & (max_dist>dist):
        answer.append(partners_name)
if answer == []:
    print("No one yet")
else:
    for i in range(len(answer)):
        print(answer[i])

# gen1 = 'MF'
# gen2 = 'FM'
# if gen1 in gen2:
#     print(True)
