def sockMerchant(n, ar):
    # Write your code here
    count = 0
    temp = []
    for i in ar:
        if i not in temp:
            temp.append(i)
            count += ar.count(i) // 2
    print(count)
    
sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
