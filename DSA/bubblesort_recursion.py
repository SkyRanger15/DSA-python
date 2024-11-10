def bublesort(arr,n):
    if(n==1):
        return
    for j in range(n-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
    bublesort(arr,n-1)
    return arr





n = int(input())
arr=[]

for i in range(n):
    element = int(input())
    arr.append(element)



print(arr)

arr = bublesort(arr,n)
print(arr)

