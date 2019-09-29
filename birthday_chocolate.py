def birthday(s, d, m):
    count=0
    sum=0
    for i in range(len(s)):
        ar=s[i:i+m]
        for j in ar:
            sum+=j
        if sum==d:
            count+=1
        sum=0
    print(count)

sr=[2,2,1,3,2]
birthday(sr,4,2)
