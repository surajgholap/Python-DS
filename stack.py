class Stack:
    """Stack represents stack DS which
    follows FILO sequence with
    .items storing all stack values."""

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
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        "Returns size of the stack"
        return len(self.items)

    def is_empty(self):
        "Check if the stack is empty."
        return not self.items

    def __str__(self):
        return "The len of the stack is {} and contents are {}".\
            format(len(self.items), self.items)


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(3)
    stack.push(5)
    stack.push(3)
    stack.push(4)
    print(stack)
    print(stack.peek())
    stack.pop()
    print(stack)
