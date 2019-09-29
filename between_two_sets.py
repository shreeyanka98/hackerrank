def getTotalX(a, b):
    # Write your code here
    count=0
    for i in range(max(arr),min(brr)+1,max(arr)):
        if all(True if i%x==0  else False for x in arr):
            if all(True if y%i==0 else False for y in brr):
                count+=1
    print(count)

arr=[2,4]
brr=[16,32,96]
getTotalX(arr,brr)    
