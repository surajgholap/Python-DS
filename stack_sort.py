from stack import Stack


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
