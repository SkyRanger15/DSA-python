def knapsack(W,n,weights,profits):
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,W+1):
            if W < weights[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]]+profits[i-1])


    return dp[n][W]



n = int(input("Enter Total No of Items: ")) 
W = int(input("Enter Total Weight: ")) 
weights= []
profits = []
for i in range(n):
    weight = int(input(f"Enter weight of Item {i+1}: "))
    profit = int(input(f"Enter profit of Item {i+1}: "))
    weights.append(weight)
    profits.append(profit)

max_profit = knapsack(W,n,weights,profits)
print(f"Profit : {max_profit}")