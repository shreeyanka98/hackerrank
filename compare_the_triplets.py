def compareTriplets(a, b):
    alice=0
    bob=0
    for i in range(3):
        if a[i]>b[i]:
            alice+=1
        elif a[i]<b[i]:
            bob+=1
    print(alice,bob)

a=[5,6,7]
b=[3,6,10]
compareTriplets(a,b)
