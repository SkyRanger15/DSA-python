import heapq

# def djik(V,adj,src):
#     dist = [float('inf')]*V
#     dist[src] = 0
#     pq = [(0,src)]

#     while pq:
#         curr_dist,u = heapq.heappop(pq)

#         if curr_dist > dist[u]:
#             continue

#         for v,w in adj[u]:
#             distance = curr_dist+w
#             if distance<dist[v]:
#                 dist[v] = distance
#                 heapq.heappush(pq,(distance,v))
#         return dist

def djik(V,adj,src):
    dist = [float('inf')]*V
    dist[src] = 0
    pq = [(0,src)]

    while pq:
        curr_dist,curr_node = heapq.heappop(pq)
        if curr_dist > dist[curr_node]:
            continue
        for adj_node,wt in adj[curr_node]:
            distance = curr_dist + wt
            if distance < dist[adj_node]:
                dist[adj_node] = distance
                heapq.heappush(pq,(distance,adj_node))
    return dist


V= int(input())
E= int(input())
edges = []
for _ in range(E):
    u,v,w = map(int, input().split())
    edges.append([u,v,w])

adj = [[] for _ in range(V)]
for u,v,w in edges:
    adj[u].append([v,w])    
    adj[v].append([u,w])    

distances = djik(V,adj,0)
for i in range(V):
    print(f"Vertex {i} : {distances[i]}")