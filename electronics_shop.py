def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    arr=[]
    for i in keyboards:
        for j in drives:
            arr.append(i+j)
    arr=[item for item in arr if item<=b]
    if len(arr)==0:
        print(-1)
    else:
        print(max(arr))

keyboards=[40,50,60]
drives=[5,8,12]
getMoneySpent(keyboards,drives,60)
