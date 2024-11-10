# def bellman_ford(V,edges,src):
#     dist = [float('inf')]*V
#     dist[src]=0
    
#     for _ in range(V):
#         for u,v,w in edges:
#             if dist[u] != float('inf') and dist[u]+w < dist[v]:
#                 dist[v] = dist[u] + w
    
#     for u,v,w in edges:
#             if dist[u] != float('inf') and dist[u]+w < dist[v]:
#                 print("Graph have a negative cycle:") 
#                 return None
           
#     return dist

def bellman_ford(V,edges,src):
    dist = [float('inf')]*V
    dist[src] = 0

    for _ in range(V):
        for curr_node,adj_node,wt in edges:
            if dist[curr_node] != float('inf') and dist[curr_node] + wt < dist[adj_node]:
                dist[adj_node] = dist[curr_node] + wt 
    return dist


V=int(input("Enter No of Vertices"))
E=int(input("Enter No of Edges"))
edges = []
print("Enter in u,v,w format")
for _ in range(E):
    u,v,w = map(int,input().split())
    edges.append([u,v,w])

adj = [[] for _ in range(V)]
for u,v,w in edges:
    adj[u].append([v,w])
    adj[v].append([u,w])

distances = bellman_ford(V,edges,0)   
for i in range(V):
    print(f"Vertex{i}:{distances[i]}")