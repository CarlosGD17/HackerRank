def migratoryBirds(arr):
    # Write your code here
    types = [1, 2, 3, 4, 5]
    count = []
    for t in types:
        count.append(arr.count(t))
    temp = 0
    type = 0
    for i in range(len(count)):
        if count[i] > temp:
            temp = count[i]
            type = i + 1
    print(type)
    
migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])
