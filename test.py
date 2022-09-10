class Graph:
        
    def __init__(self, graph = {}):
        self.__graph = graph
    
    def edges(self):
        return [(node, neighbor) 
                 for node in self.__graph 
                 for neighbor in self.__graph[node]]
    
    def nodes(self):
        return list(self.__graph.keys())

    def isolated_nodes(self):
        return [node for node in self.__graph if not self.__graph[node]]
    
    def add_node(self, node):
        if node not in self.__graph:
            self.__graph[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.__graph:
            self.add_node(node1)
        if node2 not in self.__graph:
            self.add_node(node2)

        self.__graph[node1].append(node2)
        self.__graph[node2].append(node1)

    # Let's begin with the method that returns all the paths 
    # between two nodes.    
    # The optional path parameter is set to an empty list, so that
    # we start with an empty path by default. 
    def all_paths(self, node1, node2, path = []):
        # We add node1 to the path.
        path = path + [node1]
        
        # If node1 is not in the graph, the function returns an empty list.
        if node1 not in self.__graph:
            return []

        # If node1 and node2 are one and the same node, we can return 
        # the path now.
        if node1 == node2:
            return [path]

        # Let's create an empty list that will store the paths.
        paths = []

        # Now we'll take each node adjacent to node1 and recursively 
        # call the all_paths method for them to find all the paths
        # from the adjacent node to node2.
        # The adjacent nodes are the ones in the value lists in 
        # the graph dictionary.        
        for node in self.__graph[node1]:
            if node not in path:

                subpaths = self.all_paths(node, node2, path)

                for subpath in subpaths:
                    paths.append(subpath)

        return paths

    # And now the other method that returns the shortest path.
    # We'll just use the method that finds all the paths and then
    # select the one with the minimum number of nodes.
    # If there are more than one path with the minimum number of nodes,
    # the first one will be returned.
    def shortest_path(self, node1, node2):
        return sorted(self.all_paths(node1, node2), key = len)[0]


    def all_shortest_paths(self, node1, node2):
        n = self.all_paths(node1, node2)
        maxlen = len(self.shortest_path(node1, node2))
        i = []
        for j in range(len(n)):
            if maxlen == len(n[j]):
                i.append(n[j])
        return i




KARNAUGH_MAP = {
    '0': ['1', '4', '8', '2'],
    '1': ['0', '3', '9', '5'],
    '3': ['1', '2', '7', 'B'],
    '2': ['3', '0', 'A', '6'],

    '4': ['0', 'C', '5', '6'],
    '5': ['1', 'D', '4', '7'],
    '7': ['3', 'F', '5', '6'],
    '6': ['2', 'E', '7', '4'],

    'C': ['4', '8', 'E', 'D'],
    'D': ['C', 'F', '5', '9'],
    'F': ['7', 'B', 'D', 'E'],
    'E': ['C', 'F', '6', 'A'],

    '8': ['A', '9', '0', 'C'],
    '9': ['8', 'B', '1', 'D'],
    'B': ['9', 'A', '3', 'F'],
    'A': ['E', '2', 'B', '8']
}


g = Graph(KARNAUGH_MAP)

a = '0'
b = '7'

print(f"\nAll shortest paths from {a} to {b}:")
print(g.all_shortest_paths(a, b))
print("The shortest path: ", g.shortest_path(a, b))
