def sockMerchant(n, ar):
    uniques=[]
    count=0
    for i in ar:
        if i not in uniques:
            uniques.append(i)
        else:
            count+=1
            uniques.remove(i)
    print(count)

n=9
arr=[10,20,20,10,10,30,50,10,20]
sockMerchant(n,arr)
