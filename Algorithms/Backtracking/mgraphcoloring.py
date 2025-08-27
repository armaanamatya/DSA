def is_safe(node, graph, colors, color, n):
    for i in range(n):
        if graph[node][i] == 1 and colors[i] == color:
            return False
    return True

def graph_coloring_util(graph, m, colors, node, n):
    if node == n:
        return True

    for color in range(1, m+1):
        if is_safe(node, graph, colors, color, n):
            colors[node] = color
            if graph_coloring_util(graph, m, colors, node+1, n):
                return True
            colors[node] = 0

    return False

def graph_coloring(graph, m):
    n = len(graph)
    colors = [0] * n
    if not graph_coloring_util(graph, m, colors, 0, n):
        return "Solution does not exist"
    return colors

# Driver code
if __name__ == "__main__":
    # Example 1
    graph1 = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    m1 = 3
    print("Solution for Example 1:", graph_coloring(graph1, m1))

    # Example 2
    graph2 = [
        [0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0]
    ]
    m2 = 2
    print("Solution for Example 2:", graph_coloring(graph2, m2))
