n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
adj = [[0]*n for _ in range(n)]
for i in range(m):
    print(f"Enter edge {i+ 1} :", end=" ")
    u,v = map(int, input().split())
    u -= 1  # Comment 7 and 8 to make it 0 based indexed
    v -= 1
    adj[u][v] = 1 
    adj[v][u] = 1

for row in adj:
    print(row)

# This is 1 based Indexed