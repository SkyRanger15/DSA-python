n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
adj = [[] for _ in range(n + 1)]
for i in range(m):
    print(f"Enter edge {i+1}: ")
    u,v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

print("Adjacency List:")
for i in range(1, n + 1):  
    print(f"Vertex {i}: {adj[i]}")

#This is 1 based indexed