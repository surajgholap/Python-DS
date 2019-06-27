class Queue:
    """Queue represents queue data structure
    .items stores all the queue values."""

    def __init__(self):
        self.items = []

    def enqueue(self, val):
        "Enqueues a element in the queue."
        self.items.append(val)

    def dequeue(self):
        "Dequeues the first element in the queue."
        d_val = self.items[0]
        self.items = self.items[1:]
        return d_val

    def size(self):
        "Returns size of the stack"
        return len(self.items)

    def is_empty(self):
        "Check if the queue is empty."
        return not self.items

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(3)
    print(queue.size())
    print(queue)
    queue.dequeue()
    print(queue.size())
    print(queue)
