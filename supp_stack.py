class Stack:
    """Stack represents stack DS with
    .items stores all stack values and
    gets min of the stack in O(1) using
    additional stack."""
    def __init__(self):
        self.items = []
        self.supp = []

    def push(self, val):
        "Push elements in stack."
        if self.supp == [] or self.items[-1] >= val:
            self.supp.append(val)
        self.items.append(val)

    def pop(self):
        "Pop elements from top of the stack."
        if self.items[-1] == self.supp[-1]:
                self.supp.pop()
        self.items.pop()

    def peek(self):
        "Get the top value of the stack."
        return self.items[len(self.items) - 1]

    def size(self):
        "Returns size of the stack"
        return len(self.items)

    def is_empty(self):
        "Check if the stack is empty."
        return self.items == []

    def get_min(self):
        "Returns the min value in the stack"
        return self.supp[-1]

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(3)
    stack.push(5)
    stack.push(3)
    stack.push(4)
    print(stack.get_min())
    print(stack)
    print(stack.peek())
    stack.pop()
    stack.pop()
    print(stack.get_min())
    print(stack)
