def countApplesAndOranges(s, t, a, b, apples, oranges):
    count1=count2=0
    ran1=[]
    ran2=[]
    for i in apples:
        ran1.append(a+i)
    for item in ran1:
        if item in range(s,t+1):
            count1+=1
    for i in oranges:
        ran2.append(b+i)
    for item in ran2:
        if item in range(s,t+1):
            count2+=1
    print(count1)
    print(count2)

apples=[2,3,-4]
oranges=[3,-2,-4]
countApplesAndOranges(7,10,4,12,apples,oranges)
