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


class BST:
    """BST represents binary search tree DS and
    .root is the root of the tree."""
    def __init__(self, root):
        self.root = root

    def insert(self, node, r):
        "Inserts node into BST."
        if r is None:
            r = node
        else:
            if node.val > r.val:
                if r.right is None:
                    r.right = node
                else:
                    self.insert(node, r.right)
            elif node.val <= r.val:
                if r.left is None:
                    r.left = node
                else:
                    self.insert(node, r.left)

    def delete(self, node):
        "Deletes node from the BST."
        pass

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


def unit_tests(in_list, pre_list, post_list):
    assert in_list == [1, 2, 3, 4, 6]
    assert pre_list == [3, 1, 2, 6, 4]
    assert post_list == [2, 1, 4, 6, 3]
    return "Passed all unit tests"


if __name__ == "__main__":
    nodeA = Node(3)
    nodeB = Node(6)
    nodeC = Node(1)
    nodeD = Node(2)
    nodeE = Node(4)
    nodeF = Node(9)
    bst = BST(nodeA)
    bst.insert(nodeB, bst.root)
    bst.insert(nodeC, bst.root)
    bst.insert(nodeD, bst.root)
    bst.insert(nodeE, bst.root)
    inord, preord, postord = bst.traversal()
    print(unit_tests(inord, preord, postord))
    print("In-order traversal : {}, Pre-order traversal : {}, \
Post-order traversal : {}".format(inord, preord, postord))
