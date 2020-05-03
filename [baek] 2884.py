hour = int(input())
min = int(input())

if (min-45) < 0:
    res = min-45
    min = 60 + res
    hour -= 1

    if (hour) < 0:
        hour = 23
print(hour, min)
        