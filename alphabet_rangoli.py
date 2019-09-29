import string
def print_rangoli(size):
    # your code goes here
    alpha=string.ascii_lowercase
    l=[]
    for i in range(n):
        s="-".join(alpha[i:n])
        l.append((s[::-1]+s[1:]).center(4*n-3,"-"))
    print("\n".join(l[::-1]+l[1:]))

n=5
print_rangoli(n)    
