def countingValleys(n, s):
    count=base=0
    for i in s:
        if i=="D":
            count-=1
        else:
            count+=1
        if count==0 and i=="U":
            base+=1
    print(base)

countingValleys(8,"UDDDUDUU")    
