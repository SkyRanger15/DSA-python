def optimal_bst(keys,freq,n):
    cost = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        cost[i][i] = freq[i]
    
    for length in range(2,n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')
            sum_freq = sum(freq[i:j+1])
            for k in range(i,j+1):
                temp_cost = sum_freq + (cost[i][k-1] if k>i else 0)+(cost[k+1][j] if k<j else 0)
                if temp_cost < cost[i][j]:
                    cost[i][j] = temp_cost
    return cost[0][n-1]

print("Enter the keys:")
keys = list(map(int, input().split()))
print("Enter the frequencies:")
freq = list(map(int, input().split()))
n = len(keys)

optimal_cost = optimal_bst(keys,freq,n)
print(f"Optimal cost of BST is {optimal_cost}")










# def optimal_bst(keys, freq, n):
#     # Create an auxiliary 2D matrix to store the cost of subproblems
#     cost = [[0 for _ in range(n)] for _ in range(n)]

#     # Cost when the tree contains only one key
#     for i in range(n):
#         cost[i][i] = freq[i]

#     # Fill the cost matrix in a bottom-up manner
#     for length in range(2, n + 1):  # length is the chain length
#         for i in range(n - length + 1):
#             j = i + length - 1
#             cost[i][j] = float('inf')

#             # Try making all keys in interval keys[i..j] as root
#             for r in range(i, j + 1):
#                 c = (cost[i][r - 1] if r > i else 0) + \
#                     (cost[r + 1][j] if r < j else 0) + \
#                     sum(freq[i:j + 1])
#                 if c < cost[i][j]:
#                     cost[i][j] = c

#     return cost[0][n - 1]

# # Example usage
# print("Enter the keys:")
# keys = list(map(int, input().split()))
# print("Enter the frequencies:")
# freq = list(map(int, input().split()))
# n = len(keys)

# optimal_cost = optimal_bst(keys, freq, n)
# print(f"The cost of the optimal BST is {optimal_cost}")