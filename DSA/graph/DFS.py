def dfs(adj, visited, node):
    visited[node] = 1
    print(node, end=" ")
    
    for neighbour in adj[node]:
        if visited[neighbour] == 0:
            dfs(adj, visited, neighbour)

n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
adj = [[] for _ in range(n)]
for i in range(m):
    print(f"Enter edge {i+1}: ")
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

print("Adjacency List:")
for i in range(n):
    print(f"Vertex {i}: {adj[i]}")

visited = [0] * n

print("DFS algorithm:")
dfs(adj, visited, 0)
