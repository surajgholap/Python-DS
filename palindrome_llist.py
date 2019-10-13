class Node:
    """Node represents node of a linked list
    DS..data is the value of the node and .next
    stores the address of next node in the linked
    list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """LinkedList represents linked list DS with
    .head point to the start of the linked list."""

    def __init__(self):
        self.head = None

    def add_last(self, val):
        "Add a new node at the last position of the linked list."
        if not isinstance(val, Node):
            val = Node(val)
        if self.head is None:
            self.head = val
        else:
            point = self.head
            while point.next is not None:
                point = point.next
            point.next = val
        del(val)

    def is_palidrome(self):
        "Returns if a linked list is a palindrome."
        st = []
        point = self.head
        while True:
            st.append(point.data)
            if point.next is None:
                break
            point = point.next
        return st == st[::-1]

    def __str__(self):
        st = ""
        point = self.head
        while point:
            st += ("->{}".format(point.data))
            # if point.next is None:
            #     break
            point = point.next
        return st


if __name__ == "__main__":
    l_list = LinkedList()
    l_list.add_last(Node("A"))
    l_list.add_last(Node("B"))
    l_list.add_last(Node("C"))
    l_list.add_last(Node("B"))
    l_list.add_last(Node("A"))
    print(l_list.is_palidrome())
