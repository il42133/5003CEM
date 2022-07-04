# Code adapted from https://github.com/stamd/graphs_in_python


class Node:
    def __init__(self, name, id=-1):
        self.m_id = id
        self.m_name = str(name)

    def __str__(self):
        return self.m_name

    def __repr__(self):
        return self.m_name

    def get_name(self):
        return self.m_name

    def __eq__(self, other):
        return self.m_name == other.m_name

    def __hash__(self):
        return hash(self.m_name)


class Graph:
    def __init__(self, num_of_nodes):
        return

    def __str__(self):
        return

    def add_edge(self, node1, node2, weight):
        return


class AdjListGraph(Graph):

    ###################################
    # Constructor
    ###################################
    def __init__(self, num_of_nodes, directed):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = []

        self.m_directed = directed

        self.m_graph = {}

    ###################################
    # Add edge to a graph
    ###################################
    def add_edge(self, node1_name, node2_name, weight):
        node1 = Node(node1_name)
        node2 = Node(node2_name)
        if node1 not in self.m_nodes:
            self.m_nodes.append(node1)
            self.m_graph[node1_name] = []
        else:
            node1 = self.get_node_by_name(node1_name)

        if node2 not in self.m_nodes:
            self.m_nodes.append(node2)
            self.m_graph[node2_name] = []
        else:
            node2 = self.get_node_by_name(node2_name)

        self.m_graph[node1_name].append((node2, weight))

        if not self.m_directed:
            self.m_graph[node2_name].append((node1, weight))

    ###################################
    # Find node in a graph using its name
    ###################################
    def get_node_by_name(self, name):
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
        return None

    ###################################
    # Print a graph representation
    ###################################
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out += "node " + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out

    def get_nodes(self):
        return self.m_nodes

    ###################################
    # DFS Search
    ###################################
    def dfs(self, start_node_name, target_node_name, path=None, visited=None):
        if path is None:
            path = []
        if visited is None:
            visited = set()
        start_node = self.get_node_by_name(start_node_name)
        target_node = self.get_node_by_name(target_node_name)
        path.append(start_node)
        visited.add(start_node)
        if start_node == target_node:
            return path
        for (neighbour, weight) in self.m_graph[start_node_name]:
            if neighbour not in visited:
                result = self.dfs(neighbour.get_name(), target_node_name, path, visited)
                if result is not None:
                    return result
        path.pop()
        return None

    def adjacent(self, start_node, end_node):
        path = self.dfs(start_node, end_node)
        for x in g.m_graph:
            if x == start_node:
                for y in g.m_graph[x]:
                    if y[0].m_name == end_node:
                        print("Node {} and {} are next to each other, with distance {}m\n".format(start_node, end_node,
                                                                                                  y[1]))
                        return True
        print("The path from {} to {} is {}\n".format(start_node, end_node, path))
        return False


g = AdjListGraph(6, False)
g.add_edge("A", "B", 32)
g.add_edge("A", "C", 8)
g.add_edge("A", "D", 22)
g.add_edge("A", "E", 48)
g.add_edge("B", "C", 70)
g.add_edge("D", "F", 18)

print(g)

while True:
    new = input("Enter 2 nodes from [A, B, C, D, E, F] in format node1, node2: ")
    try:
        nd = new.split(", ")
    except IndexError:
        print("Please enter the nodes in a valid format.")
        continue
    if len(nd) != 2:
        print("Please enter the nodes in a valid format.")
        continue
    g.adjacent(nd[0].upper(), nd[1].upper())
