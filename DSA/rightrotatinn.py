def rightrotation(arr,k):
    n = len(arr)
    k = k % n
    temp = arr[n-k:n]
    for i in range(n-1,k-1,-1):
        arr[i] = arr[i-k]
    
    for i in range(k):
        arr[i] = temp[i-k]
    return arr

# Time complexity O(n)
# Space Complexity O(n)



#9 3 2 1 4 2 7 4
arr = [1,4,2,7,4,9,3,2]
k  = 3
arr = rightrotation(arr,k)
print(arr)