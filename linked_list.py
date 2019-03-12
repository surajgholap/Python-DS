class Node:
    """Node represents a node of a linked list.
    .data contains the value of the node and .next
    contains the address of next node."""
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class Linkedlist:
    """Linkenlist represents linked list data structure.
    .head points to the start of the linked list."""
    def __init__(self):
        self.head = None

    def add_front(self, val):
        "Add a new node with val as the value in the front."
        if type(val) != Node:
            val = Node(val)
        if self.head is None:
            self.head = val
        else:
            val.next = self.head
            self.head = val
        del(val)

    def add_last(self, val):
        "Add a new node at the last position of the linked list."
        if type(val) != Node:
            val = Node(val)
        if self.head is None:
            self.head = val
        else:
            point = self.head
            while point.next is not None:
                point = point.next
            point.next = val
        del(val)

    def add_after(self, val, new_val):
        "Add a new node with new_val after node with val."
        point = self.head
        if type(new_val) != Node:
            new_val = Node(new_val)
        while point.data != val:
            point = point.next
        new_val.next = point.next
        point.next = new_val
        del(new_val)

    def remove_nth(self, n):
        "Removes the nth node from the linked list"
        point = self.head
        count = 1
        while True:
            if point.next is None and count < n:
                return "Index overflow, Linked list's length is {}"\
                    .format(count)
            elif count == n - 1 and point.next is not None:
                temp = point.next
                point.next = temp.next
                del temp
            count += 1
            point = point.next

    def find_nth(self, n):
        "Return nth element in the list"
        count = 1
        point = self.head
        while True:
            if point.next is None and count < n:
                return "Index overflow, Linked list's length is {}"\
                    .format(count)
            elif count == n:
                return point.data
            point = point.next
            count += 1

    def __str__(self):
        st = ""
        point = self.head
        while True:
            st += ("->{}".format(point.data))
            if point.next is None:
                break
            point = point.next
        return st

if __name__ == "__main__":
    linked_list = Linkedlist()
    node1 = Node(8)
    linked_list.add_front(2)
    linked_list.add_front(3)
    linked_list.add_front(4)
    linked_list.add_after(4, 6)
    linked_list.add_last(5)
    # linked_list.add_last(node1)
    linked_list.add_after(3, node1)
    print(linked_list.find_nth(3))
    print(linked_list.remove_nth(3))
    print(linked_list)
