#Recursive Implementation
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex)  # Process the current node (e.g., print it)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


# Starting DFS from vertex 'A'
dfs_recursive(graph, 'A')

#Iterative Implementation
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)  # Process the current node (e.g., print it)
            stack.extend(reversed(graph[vertex]))  # Add neighbors to the stack

# Starting DFS from vertex 'A' using iterative approach
dfs_iterative(graph, 'A')
