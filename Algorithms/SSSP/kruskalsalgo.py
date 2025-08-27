class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskals_algorithm(graph, num_vertices):
    # Sort edges by weight
    edges = sorted(graph, key=lambda edge: edge[2])

    # Create a disjoint set for the vertices
    disjoint_set = DisjointSet(num_vertices)

    mst_weight = 0
    mst_edges = []

    for u, v, weight in edges:
        # Check if the current edge forms a cycle
        if disjoint_set.find(u) != disjoint_set.find(v):
            # If not, include this edge in the MST
            disjoint_set.union(u, v)
            mst_weight += weight
            mst_edges.append((u, v, weight))

    return mst_weight, mst_edges

# Example usage:
# Graph represented as a list of edges (u, v, weight)
graph = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9),
]

num_vertices = 5  # Number of vertices in the graph
result = kruskals_algorithm(graph, num_vertices)

print(f"Total weight of MST: {result[0]}")
print("Edges in the MST:", result[1])
