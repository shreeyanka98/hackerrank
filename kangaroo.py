def kangaroo(x1, v1, x2, v2):
    if abs(v1-v2)!=0:
        if abs(x1-x2)%abs(v1-v2)==0 and (x1<x2 and v1<v2)!=True:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

kangaroo(0,3,4,2)
