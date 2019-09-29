def plusMinus(arr):
    neg=pos=zero=0
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
        else:
            zero+=1
    count1=pos/n
    count2=neg/n
    count3=zero/n
    print("{0:.6f}".format(count1))
    print("{0:.6f}".format(count2))
    print("{0:.6f}".format(count3))

arr=[1,2,0,5,-8]
n=len(arr)
plusMinus(arr)
