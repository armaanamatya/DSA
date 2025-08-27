# with open('C:\\Users\\armaa\\OneDrive\\Desktop\\DSA\\Algorithms\\SSSP\\dijkstraData.txt') as f:
#     # process the file

#     #dijkstraData
#     #a = [[int(x) for x in ln.split()] for ln in f]
#     data = []
#     list_data = []
#     node_list = []
#     u = []
#     v = []
#     data_u = []
#     data_v = []
#     dict_nested = {}
#     list_nested = []
#     for ln in f:
#         #print ln
#         #print type(ln)
#         #print len(ln)
#         if len(ln) >1:
#             data = ln.split()
#             #print data
#             list_data.append(data)           
#             #print list_data

#     for i in range(len(list_data)):
#         node_list.append(i+1)
#         del list_data[i][0]
        
#         for j in range(len(list_data[i])):
#             u,v = list_data[i][j].split(',')            
#             #print u,v
#             #print type(u)
#             data_u.append(int(u))
#             data_v.append(int(v))
#         #print data_u,data_v
#         list_nested.append(dict(zip(data_u,data_v)))
#         #print list_nested
#         data_u,data_v = [],[]
#     #print node_list
#     #print list_nested    
#     dict_nested = dict(zip(node_list,list_nested))
#     #print dict_nested
    
# f.close()

# def dijkstra():
#     scores = []
#     #print node_list
#     V = node_list
#     #print V
#     X = [1]
#     #print type(X)
#     A = {}
#     A[1] = 0
#     #print A
#     data_v = []
#     data_w = []
    
#     while X != V:
#         for v in X:
#             for w in dict_nested[v].keys():
#                 #print w
#                 if w not in A:
#                     data_v.append(v)
#                     data_w.append(w)
#                     scores.append(A[v] + dict_nested[v][w])
                    
#         #print "scores: "+str(scores)
#         #print "data_w: "+str(data_w)
#         find_w = 0
#         find_w = data_w[scores.index(min(scores))]
#         #print "w: "+ str(find_w)
#         X.append(find_w)
#         #print "X: "+str(X)
#         A[find_w] = min(scores)
#         #print "A[w],w: " +str(A[find_w])+" "+str(find_w)
#         X.sort()
#         scores = []
#         data_v = []
#         data_w = []                   
#     #print A
#     tmp = []
#     for keys in [7,37,59,82,99,115,133,165,188,197]:
#         #print A[keys]
#         #print type(A[keys])
#         tmp.append(A[keys])
#     print (sorted(tmp))



# dijkstra()

import heapq
from typing import Dict, List

INF = float('inf')

# Function to create an edge
def add_edge(graph, u, v, w):
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(graph, src, V):
    # Priority queue to act as a min-heap
    pq = []
    # Distance vector
    dist = [INF] * V
    # Push the source node onto the priority queue with distance 0
    heapq.heappush(pq, (0, src))
    dist[src] = 0

    while pq:
        # Extract the node with the minimum distance
        u_dist, u = heapq.heappop(pq)
        
        # If the distance to u is greater than the recorded shortest distance, continue
        if u_dist > dist[u]:
            continue

        # Traverse all neighbors of u
        for v, wt in graph[u]:
            # If there's a shorter path to v through u
            if dist[v] > dist[u] + wt:
                dist[v] = dist[u] + wt
                heapq.heappush(pq, (dist[v], v))

    print("Vertex   Distance from src")
    for i in range(V):
        print(f"{i}\t{dist[i]}")

# Main function
def main():
    V = 9
    graph = [[] for _ in range(V)]
    add_edge(graph, 0, 1, 4)
    add_edge(graph, 0, 7, 8)
    add_edge(graph, 1, 2, 8)
    add_edge(graph, 1, 7, 11)
    add_edge(graph, 2, 3, 7)
    add_edge(graph, 2, 8, 2)
    add_edge(graph, 2, 5, 4)
    add_edge(graph, 3, 4, 9)
    add_edge(graph, 3, 5, 14)
    add_edge(graph, 4, 5, 10)
    add_edge(graph, 5, 6, 2)
    add_edge(graph, 6, 7, 1)
    add_edge(graph, 6, 8, 6)
    add_edge(graph, 7, 8, 7)

    dijkstra(graph, 0, V)

if __name__ == "__main__":
    main()

# #Neetcode
# https://www.youtube.com/watch?v=XEb7_z5dG3c
# Dijkstra's Algorithm
# Implement Dijkstra's shortest path algorithm.

# Given a weighted, directed graph, and a starting vertex, return the shortest distance from the starting vertex to every vertex in the graph.

# Input:

# n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.
# edges - a list of tuples, each representing a directed edge in the form (u, v, w), where u is the source vertex, v is the destination vertex, and w is the weight of the edge, where (1 <= w <= 10).
# src - the source vertex from which to start the algorithm, where (0 <= src < n).
# Note: If a vertex is unreachable from the source vertex, the shortest path distance for the unreachable vertex should be -1.

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
            
        for s,d, weight in edges:
            adj[s].append([d, weight])
        
        shortest = {}
        minHeap = [[0,src]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest: 
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])
            
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
                
        return shortest