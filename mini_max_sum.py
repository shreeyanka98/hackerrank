def miniMaxSum(arr):
    maximum=minimum=0
    arr.sort()
    for i in range(len(arr)-1):
        minimum+=arr[i]
    for i in range(1,len(arr)):
        maximum+=arr[i]
    print(minimum,maximum)

arr=[1,2,3,4,5]
miniMaxSum(arr)
