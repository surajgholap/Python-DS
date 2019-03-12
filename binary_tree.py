class Node:
    """Node represents any node of a tree and
    .val is the value of the node and .left and
    .right are the left and right children of the
    node."""
    def __init__(self, val):
        if val is None:
            raise ValueError("Node value cannot be null")
        self.val = val
        self.left = None
        self.right = None


class Tree:
    """Tree represents tree DS and .root is the root of the tree."""
    def __init__(self, root):
        self.root = root

    def traversal(self):
        "Returns inorder, preorder and postorder traversal of nodes."
        node = self.root
        inord_list = []
        inorder_trav(node, inord_list)
        preord_list = []
        preorder_trav(node, preord_list)
        postord_list = []
        postorder_trav(node, postord_list)
        return inord_list, preord_list, postord_list


def inorder_trav(node, lis):
    "In-order traversal of nodes."
    if node:
        inorder_trav(node.left, lis)
        lis.append(node.val)
        inorder_trav(node.right, lis)


def preorder_trav(node, lis):
    "Pre-order traversal of nodes."
    if node:
        lis.append(node.val)
        preorder_trav(node.left, lis)
        preorder_trav(node.right, lis)


def postorder_trav(node, lis):
    "Post-order traversal of nodes."
    if node:
        postorder_trav(node.left, lis)
        postorder_trav(node.right, lis)
        lis.append(node.val)

if __name__ == "__main__":
    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    nodeD = Node('D')
    nodeE = Node('E')
    nodeF = Node('F')
    tree = Tree(nodeA)
    nodeA.left = nodeB
    nodeA.right = nodeC
    nodeB.left = nodeD
    nodeB.right = nodeE
    nodeC.left = nodeF
    # nodeB.right = Node(C)
    inord, preord, postord = tree.traversal()
    print("Inorder traversal: ", inord)
    print("Preorder traversal: ", preord)
    print("Postorder traversal: ", postord)
    assert inord == ['D', 'B', 'E', 'A', 'F', 'C']
