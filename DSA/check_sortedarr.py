#Time Complexity O(n logn)
#Space Complexity O(n)

# def ifsorted(arr):
#     s_arr = sorted(arr)
#     if(arr == s_arr):
#         return True
#     else:
#         return False

#Time Complexity O(n)
#Space Complexity O(1)

def ifsorted(arr, n):
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            return False


    return True





n = int(input("Total Elements: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
print(arr)
ans = ifsorted(arr,n)
print(ans)