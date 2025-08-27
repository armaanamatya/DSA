from collections import deque

def bfs(graph, start):
    # Create a queue for BFS and mark the start node as visited
    queue = deque([start])
    visited = {start: True}
    
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()
        print(vertex)  # Process the current node (e.g., print it)

        # Get all adjacent vertices of the dequeued vertex
        # If an adjacent vertex hasn't been visited, mark it as visited and enqueue it
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited[neighbor] = True
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting BFS from vertex 'A'
bfs(graph, 'A')
