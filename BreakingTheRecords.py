def breakingRecords(scores):
    # Write your code here
    maxCount = 0
    minCount = 0
    
    maxScore = scores[0]
    minScore = scores[0]
    
    for i in scores[1:]:
        if i > maxScore:
            maxScore = i
            maxCount += 1
        if i < minScore:
            minScore = i
            minCount += 1
    
    return [maxCount, minCount]

print(breakingRecords([12, 24, 10, 24]))
