List = [[6, 5, 3], [1, 2, [4, [2, 3], [2, 2], 2], 3], [4], [1, 2], [2, 4], [5, 5, 5], [7]]
count = 0


def find(obj):
    global count
    for i in range(len(obj)):
        if isinstance(obj[i], list):
            if len(obj[i]) == 2:
                count += 1
            find(obj[i])


find(List)
print(count)


