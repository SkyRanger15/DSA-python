def floyd_warshall(V,adj):
    dist = [row[:] for row in adj]

    for via in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][via] + dist[via][j]:
                    dist[i][j] = dist[i][via] + dist[via][j]

    return dist



V = int(input("Enter Number of Vertices: "))
E = int(input("Enter Number of Edges: "))
adj = [[float('inf')]*V for _ in range(V)]

for i in range(V):
    adj[i][i] = 0

print("Enter in u,v,w format")
for i in range(E):
    
    u,v,w = map(int,input().split())
    adj[u][v] = w

distances = floyd_warshall(V,adj)

for i in range(V):
    for j in range(V):
        if distances[i][j]==float('inf'):
            print("Inf",end=" ")
        else:
            print(distances[i][j],end=" ")
    print()