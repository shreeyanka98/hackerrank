def bonAppetit(bill, k, b):
    sum=add=0
    for i in range(len(bill)):
        add+=bill[i]
    sum=(add-bill[k])//2
    if b==sum:
        print("Bon Appetit")
    else:
        print(b-sum)

bill=[3,10,2,9]
bonAppetit(bill,1,12)        
