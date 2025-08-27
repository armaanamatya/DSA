import heapq

def prims_algorithm(graph):
    # Number of vertices in the graph
    num_vertices = len(graph)

    # To keep track of vertices included in the MST
    in_mst = [False] * num_vertices

    # Priority queue to pick the minimum weight edge at every step
    # Format: (weight, vertex)
    priority_queue = [(0, 0)]  # Start with vertex 0 and weight 0
    total_weight = 0

    while priority_queue:
        # Get the edge with the minimum weight
        weight, current_vertex = heapq.heappop(priority_queue)

        # If the vertex is already included in the MST, skip it
        if in_mst[current_vertex]:
            continue

        # Include the vertex in the MST
        in_mst[current_vertex] = True
        total_weight += weight

        # Look at all the adjacent vertices of the current vertex
        for neighbor, weight in graph[current_vertex]:
            if not in_mst[neighbor]:
                # Push the adjacent vertex and its edge weight to the priority queue
                heapq.heappush(priority_queue, (weight, neighbor))

    return total_weight

# Example usage:
# Graph represented as an adjacency list
# Each entry is a list of tuples (neighbor, weight)
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)],
}

result = prims_algorithm(graph)
print(f"Total weight of MST: {result}")
