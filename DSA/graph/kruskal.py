class DSU:
    def __init__(self, V):
        self.parent = [i for i in range(V)]
        self.rank = [0] * V
    
    def findUPar(self, node):
        if self.parent[node] == node:
            return node
        # Path compression
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def unionByRank(self, u, v):
        ult_U = self.findUPar(u)
        ult_V = self.findUPar(v)
        
        if ult_U != ult_V:
            # Union by rank
            if self.rank[ult_U] > self.rank[ult_V]:
                self.parent[ult_V] = ult_U
            elif self.rank[ult_U] < self.rank[ult_V]:
                self.parent[ult_U] = ult_V
            else:
                self.parent[ult_V] = ult_U
                self.rank[ult_U] += 1

class Solution:
    def kruskalMST(self, V, edges):
        # Sort edges based on weight
        edges.sort(key=lambda x: x[2])
        
        dsu = DSU(V)
        mst = []
        mst_weight = 0
        
        for u, v, wt in edges:
            if dsu.findUPar(u) != dsu.findUPar(v):
                dsu.unionByRank(u, v)
                mst.append((u, v))
                mst_weight += wt
        
        return mst_weight, mst

# Driver code
if __name__ == "__main__":
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    edges = []
    print("Enter the edges in the format 'u v w' where u and v are vertices and w is the weight:")
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])
    
    obj = Solution()
    mst_weight, mst = obj.kruskalMST(V, edges)
    print("The sum of all the edge weights in the MST:", mst_weight)
    print("The minimum spanning tree is:", mst)
