n = [1, 4, 3, 5, 6, 3, 2, 9, 6]


def remove_duplicate(list):
    return set(list)


def remove_duplicute1(num):
    list = []
    for i in num:
        if i not in list:
            list.append(i)
    return list


print(remove_duplicate(n))
print(remove_duplicute1(n))
