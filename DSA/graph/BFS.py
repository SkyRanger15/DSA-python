def bfs(adj,visited, node):

    queue= [node]
    visited[node] = 1

    while queue:
        vertex = queue.pop(0)
        print(vertex,end=" ")
    
        for neighbour in adj[vertex]:
            if visited[neighbour] == 0:
                queue.append(neighbour)
                visited[neighbour] = 1


n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
adj = [[] for _ in range(n)]
for i in range(m):
    print(f"Enter edge {i+1}: ")
    u,v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

print("Adjacency List:")
for i in range(n):  
    print(f"Vertex {i}: {adj[i]}")

visited = [0]*n


print("BFS algorithm : ")
bfs(adj,visited,0)