def getTotalX(a, b):
    # Write your code here
    # b.sort()
    minB = b[0]
    matriz = []
    count = 0
    for e in a:
        temp = set()
        for i in range(e, minB + 1, e):
            temp.add(i)
        matriz.append(temp)

    temp = matriz[0]
    for i in range(1, len(matriz)):
        temp = temp.intersection(matriz[i])

    # print(temp)
    # print(b)
    for numero in list(temp):
        esMultiplo = True
        for i in b:
            esMultiplo = esMultiplo and i % numero == 0
        if esMultiplo:
            count+=1
    # print(count)
    return count

print(getTotalX([2, 4], [16, 32, 96]))
