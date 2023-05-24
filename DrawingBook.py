def pageCount(n, p):
    # Write your code here
    right = p // 2
    if n % 2 == 0:
        left = (1 + n - p) // 2
    else:
        left = (n - p) // 2
    if right < left:
        return right
    return left

print(pageCount(6, 5))
