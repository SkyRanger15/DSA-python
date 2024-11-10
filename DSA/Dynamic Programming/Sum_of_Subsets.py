# def is_subset_sum(arr,n,target_sum):
#     dp =[[False]*(target_sum+1) for _ in range(n+1)]
#     for i in range(n+1):
#         dp[i][0] = True
#     for i in range(1,n+1):
#         for j in range(1,target_sum+1):
#             if j < arr[i-1]:
#                 dp[i][j] = dp[i-1][j]
#             else:
#                 dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
#     return dp[n][target_sum]

def is_subset_sum(arr,n,target_sum):
    dp = [[False]*(target_sum+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1,n+1):
        for j in range(target_sum+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]
    return dp[n][target_sum]


print("Enter Elements")
arr = list(map(int,input().split()))
target_sum = int(input("Enter Target Sum: "))
n =  len(arr)

if is_subset_sum(arr, n, target_sum):
    print(f"There is a subset with sum {target_sum}")
else:
    print(f"There is no subset with sum {target_sum}")