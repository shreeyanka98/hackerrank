def diagonalDifference(arr):
    # Write your code here
    sum1=0
    sum2=0
    for i in range(n):
        sum1+=arr[i][i]
    for i in range(n):
        sum2+=arr[i][n-1-i]
    return abs(sum1-sum2)

arr=[11,2,4
     4,5,6
     10,8,-12]
diagonalDifference(arr)    
