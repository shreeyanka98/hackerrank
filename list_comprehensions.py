x=1
y=1
z=1
N=2
ar = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k!=N):
                ar.append([i,j,k])
print(ar)
