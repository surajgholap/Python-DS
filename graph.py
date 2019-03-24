class GraphNode:
    """GraphNode represents node of any graph with
    .val as the value of the node and .adj as the
    list of adjacent nodes."""
    def __init__(self, val):
        self.val = val
        self.adj = set()

    def add_adjacent(self, new_val):
        "Add adjacent node of new_val value"
        self.adj.add(new_val)

    def get_adjacent(self):
        "Return all the adjacent nodes"
        return self.adj

    def remove_adj(self, val):
        "Removes adjacent node of val value"
        if val in self.adj:
            self.adj.remove(val)
            return str(self)
        return ("Node not present!")

    def __str__(self):
        # print(self.adj)
        return str(self.val) + str(self.adj)

    def __repr__(self):
        return str(self)


class Graph:
    """Graph represents the DS graph, .nodes is the
    list of nodes/vertices present in the graph."""
    def __init__(self):
        self.nodes = {}

    def add_node(self, new_node):
        "Add new node to the graph."
        if isinstance(new_node, GraphNode):
            self.nodes[new_node.val] = [i.val for i in new_node.adj]

    def graph_struct(self):
        "Returns graph structure."
        return self.nodes

    def recur_dfs(self, node):
        "DFS helper function."
        trav = []
        visited = {}
        self.dfs_traversal(node, visited, trav)
        return trav

    def dfs_traversal(self, node, visited, trav):
        "Traverses a graph in DFS method."
        if node is None:
            return None
        trav.append(node.val)
        visited[node] = 1
        for n in node.adj:
            if n not in visited.keys():
                self.dfs_traversal(n, visited, trav)

    def bfs(self, node):
        "BFS traversal of a graph."
        visited, queue = [], [node]
        visited.append(node)
        while queue:
            vertex = queue.pop(0)
            for w in self.nodes[vertex]:
                if w not in visited:
                    visited.append(w)
                    queue.append(w)
        return visited

if __name__ == "__main__":
    """
    5 __ 6
    | \
    2  4 __ 1 __ 9
       |
       8
    """
    graph = Graph()
    node1 = GraphNode(5)
    node2 = GraphNode(4)
    node3 = GraphNode(6)
    node4 = GraphNode(1)
    node5 = GraphNode(8)
    node6 = GraphNode(2)
    node7 = GraphNode(9)
    node1.add_adjacent(node2)
    node1.add_adjacent(node3)
    node1.add_adjacent(node6)
    node2.add_adjacent(node4)
    node2.add_adjacent(node1)
    node2.add_adjacent(node5)
    node3.add_adjacent(node1)
    node4.add_adjacent(node2)
    node4.add_adjacent(node7)
    node5.add_adjacent(node2)
    node6.add_adjacent(node1)
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    graph.add_node(node4)
    graph.add_node(node5)
    graph.add_node(node6)
    graph.add_node(node7)
    struc = graph.graph_struct()
    print(struc)
    print(graph.bfs(5))
    print(graph.recur_dfs(node1))
