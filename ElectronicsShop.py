def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    if min(keyboards) + min(drives) > b:
        return -1

    temp = []
    for i in keyboards:
        for j in drives:
            if i + j <= b:
                temp.append(i + j)

    return max(temp)


print(getMoneySpent([4, 5, 2, 5], [1, 6, 3, 9, 5], 13))
