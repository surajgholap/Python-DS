class Node:
    """Node represents node of a linked list
    DS..data is the value of the node and .next
    stores the address of next node in the linked
    list"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """LinkedList represents linked list DS with
    .head point to the start of the linked list"""

    def __init__(self):
        self.head = None

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

    def start_cycle(self):
        "Returns if the linked list has cycles"
        point = self.head
        dic = {}
        while point.next is not None:
            if point not in dic.keys():
                dic[point] = 1
            else:
                return point.data
            point = point.next
        return False

    def has_cycle_hash(self):
        "Returns if the linked list has cycles"
        point = self.head
        dic = {}
        while point.next is not None:
            if point not in dic.keys():
                dic[point] = 1
            else:
                return True
            point = point.next
        return False

    def cycle_2pointer(self):
        "Returns if the linked list has cycles with 2 pointers"
        fast = slow = self.head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

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
    l_list = LinkedList()
    l_list.add_last(Node(4))
    l_list.add_last(Node(5))
    l_list.add_last(Node(6))
    l_list.add_last(Node(7))
    l_list.add_last(l_list.head.next)
    print(l_list.has_cycle_hash())
    print(l_list.cycle_2pointer())
    print(l_list.start_cycle())
    print(l_list)
