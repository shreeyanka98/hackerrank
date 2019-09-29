def breakingRecords(scores):
    highest=scores[0]
    lowest=scores[0]
    count1=count2=0
    for i in range(1, len(scores)):
        if highest<scores[i]:
            highest=scores[i]
            count1+=1
        elif lowest>scores[i]:
            lowest=scores[i]
            count2+=1
    print(count1,count2)

scores=[10,5,20,20,4,5,2,25,1]
breakingRecords(scores)
