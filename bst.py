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

    def min_val(self, node):
        "Returns minimum value of the BST."
        curr = node
        while curr.left:
            curr = curr.left
        return curr

    def delete(self, key, r):
        "Deletes node from the BST."
        if r is None:
            return r
        if r.val < key:
            r.right = self.delete(key, r.right)
        elif r.val > key:
            r.left = self.delete(key, r.left)
        else:
            if r.left is None:
                temp = r.right
                r = None
                return temp
            elif r.right is None:
                temp = r.left
                r = None
                return temp
            temp = self.min_val(r.right)
            r.val = temp.val
            r.right = self.delete(temp.val, r.right)
        return r

    def search(self, r, value):
        "Returns whether value is present in BST."
        if not r:
            return False
        if r.val == value:
            return True
        elif r.val < value:
            return self.search(r.right, value)
        elif r.val > value:
            return self.search(r.left, value)

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
    bst.delete(2, bst.root)
    inord, preord, postord = bst.traversal()
    # print(unit_tests(inord, preord, postord))
    print("In-order traversal : {}, Pre-order traversal : {}, \
Post-order traversal : {}".format(inord, preord, postord))
    print(bst.search(bst.root, 44))
    print(bst.search(bst.root, 4))
