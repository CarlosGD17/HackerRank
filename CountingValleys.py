def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    if path[0] == 'U':
        level = 1
    if path[0] == 'D':
        level = -1
    for i in range(1, steps):
        temp = level
        if path[i] == 'U':
            level += 1
        if path[i] == 'D':
            level -= 1
        if temp == -1 and level == 0:
            valleys += 1
    return valleys

print(countingValleys(8, "UDDDUDUU"))
