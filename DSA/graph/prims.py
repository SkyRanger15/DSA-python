import heapq

class Solution:
    # def spanningTree(self, V, adj):
    #     pq = [(0,0, -1)]
    #     visited = [0]*V
    #     sum1 = 0
    #     mst = []
                
    #     while pq:
    #         wt,node, parent = heapq.heappop(pq)

    #         if visited[node] == 1:
    #             continue

    #         visited[node] = 1
    #         sum1 += wt

    #         if parent != -1:
    #             mst.append((parent,node))


    #         for adj_node,edge_wt in adj[node]:
    #             if not visited[adj_node]:
    #                 heapq.heappush(pq,(edge_wt,adj_node,node))
        
    #     return sum1, mst
    def spanningTree(self,V, adj):
        pq = [(0,0,-1)]
        visited = [0]*V
        sum1 = 0
        mst = []

        while pq:
            wt,curr_node,parent_node = heapq.heappop(pq)
            
            if visited[curr_node] == 1:
                continue
            
            visited[curr_node] = 1
            sum1 += wt
            if parent_node != -1:
                mst.append([parent_node,curr_node])
            
            for adj_node,edge_wt in adj[curr_node]:
                if not visited[adj_node]:
                    heapq.heappush(pq,(edge_wt,adj_node,curr_node))
        return sum1, mst

        

# Driver code
if __name__ == "__main__":
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    edges = []
    print("Enter the edges in the format 'u v w' where u and v are vertices and w is the weight:")
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])
    
    adj = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    obj = Solution()
    sum, mst = obj.spanningTree(V, adj)
    print("The sum of all the edge weights:", sum)
    print("The minimum spanning tree is : ", mst)