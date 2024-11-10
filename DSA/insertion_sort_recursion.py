def insertionsort_rec(arr,n,i):
    if i == n:
        return
    j=i
    while(j>0 and arr[j]<arr[j-1]):
        arr[j],arr[j-1] = arr[j-1],arr[j]
        j -=1

    insertionsort_rec(arr,n,i+1)
    return arr






n = int(input())
arr=[]

for i in range(n):
    element = int(input())
    arr.append(element)



print(arr)

arr = insertionsort_rec(arr,n,1)
print(arr)

