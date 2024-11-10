class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

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


# Example usage
if __name__ == "__main__":
    V = 7  # Number of elements
    dsu = DisjointSetUnion(V)

    # Perform some union operations
    dsu.unionByRank(0, 1)
    dsu.unionByRank(1, 2)
    dsu.unionByRank(3, 4)
    dsu.unionByRank(4, 5)
    dsu.unionByRank(5, 6)

    # Find operations to check the ultimate parent
    print(dsu.findUPar(0))  # Output: 0
    print(dsu.findUPar(1))  # Output: 0
    print(dsu.findUPar(2))  # Output: 0
    print(dsu.findUPar(3))  # Output: 3
    print(dsu.findUPar(4))  # Output: 3
    print(dsu.findUPar(5))  # Output: 3
    print(dsu.findUPar(6))  # Output: 3

    # Union two sets
    dsu.unionByRank(2, 3)

    # Check the ultimate parent after union
    print(dsu.findUPar(0))  # Output: 0
    print(dsu.findUPar(3))  # Output: 0
    print(dsu.findUPar(6))  # Output: 0