N=5
list1=[]
p=[]
s0=["insert",0,5]
s1=["insert",1,10]
s2=["insert",0,6]
s3="sort"
s4="print"
for i in range(N):
    p=s[i]
    cmd=p[0]
    args=p[1:]
    if cmd!="print":
        cmd+="("+",".join(args)+")"
        eval("list1."+cmd)
    else:
        print(list1)
