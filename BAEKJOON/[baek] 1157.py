letter = sorted(input().upper())
editted_letter = letter + ['.']

tmp, sum = None, 1
bag = {}
for elements in editted_letter:
    if tmp==None:
        tmp = elements
        continue

    elif tmp == elements:
        sum += 1

    else:
        bag.update({tmp:sum})

        tmp = elements
        sum = 1

print(bag)
def f1(x):
    return bag[x]
key_max = max(bag.keys(), key=f1)
print(key_max)
max_key = (max(bag.keys()))
print(max_key)

lambda x: bag.keys(), print()