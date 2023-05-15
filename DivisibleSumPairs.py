def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for j in range(n-1, -1, -1):
        for i in range(j):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

print(divisibleSumPairs(6, 5, [1, 2, 3, 4, 5, 6]))
