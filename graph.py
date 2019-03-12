class GraphNode:
    """GraphNode represents node of any graph with
    .val as the value of the node and .adj as the
    list of adjacent nodes."""
    def __init__(self, val):
        self.val = val
        self.adj = []

    def add_node(self, new_val):
        "Add adjacent node of new_val value"
        self.adj.append(new_val)

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

new_node = GraphNode(5)
node1 = GraphNode(4)
new_node.add_node(node1.val)
# new_node.add_node(6)
print(new_node)
print(node1)
print(new_node.remove_adj(node1.val))
print(new_node.remove_adj(3))
print(new_node.get_adjacent())
print(GraphNode.__dict__)
