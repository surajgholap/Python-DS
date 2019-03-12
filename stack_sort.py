class Stack:
    """Stack represents stack DS with
    .items stores all stack values."""
    def __init__(self):
        self.items = []

    def push(self, val):
        "Push elements in stack."
        self.items.append(val)

    def pop(self):
        "Pop elements from top of the stack."
        return self.items.pop()

    def peek(self):
        "Get the top value of the stack."
        return self.items[len(self.items) - 1]

    def size(self):
        "Returns size of the stack"
        return len(self.items)

    def is_empty(self):
        "Check if the stack is empty."
        return self.items == []

    def __str__(self):
        return str(self.items)


def sort_stack(orig):
    "Returns sorted stack."
    helper = Stack()
    while not orig.is_empty():
        temp = orig.pop()
        if helper.is_empty():
            helper.push(temp)
        elif temp > helper.peek():
            orig.push(helper.pop())
            orig.push(temp)
        elif temp <= helper.peek():
            helper.push(temp)
    while not helper.is_empty():
        orig.push(helper.pop())
    return orig
if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(3)
    stack.push(2)
    stack.push(1)
    # stack.push(4)
    # stack.push(0)
    print(stack)
    print(stack.peek())
    # stack.pop()
    sort_stack(stack)
    print(stack)
