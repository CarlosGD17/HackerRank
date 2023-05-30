def pickingNumbers(a):
    # Write your code here
    sub = []
    for i in a:
        temp = [i]
        for j in a:
            if abs(i - j) <= 1:
                temp.append(j)
        temp = temp[1:].copy()
        
        if abs(max(temp) - min(temp)) > 1:
            m1 = [t for t in temp if t < max(temp)]
            m2 = [t for t in temp if t > min(temp)]
            if len(m1) > len(m2):
                temp = m1.copy()
            else:
                temp = m2.copy()
        if len(temp) > len(sub):
            sub = temp.copy()
        print(temp)
    #print(sub)
    return len(sub)
