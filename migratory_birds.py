def migratoryBirds(arr):
    ar=[0]*5
    for i in arr:
        if i==1:
            ar[0]+=1
        elif i==2:
            ar[1]+=1
        elif i==3:
            ar[2]+=1
        elif i==4:
            ar[3]+=1
        elif i==5:
            ar[4]+=1
    s=ar.index(max(ar))+1
    print(s)

arr=[1,4,4,4,5,3]
migratoryBirds(arr)
