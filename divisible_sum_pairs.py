def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(0,len(ar)):
        for j in range(0,len(ar)):
            if i<j and (ar[i]+ar[j])%k==0:
                count+=1
    print(count)

arr=[1,3,2,6,1,2]
divisibleSumPairs(6,3,arr)
