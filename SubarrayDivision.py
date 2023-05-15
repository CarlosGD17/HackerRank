def birthday(s, d, m):
    # Write your code here
    count = 0
    for i in range(len(s) - m + 1):
        sum = 0
        for j in range(m):
            sum += s[i + j]
        if sum == d:
            count += 1
    return count

print(birthday([1, 2, 1, 3, 2], 3, 2))
