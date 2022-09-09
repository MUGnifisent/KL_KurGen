from dijkstar import Graph, find_path

graph = Graph ()
graph.add_edge(1, 3, 2)
graph.add_edge(3, 4, 4)
graph.add_edge(4, 6, 10)
graph.add_edge(4, 7, 1)
graph.add_edge(1, 7, 3)

shortest_path = find_path(graph, 1, 4)

print(graph)
print(shortest_path)

n = shortest_path.costs
print(n)