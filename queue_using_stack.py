from stack import Stack


class Queue:
    "Queue represents queue DS using stacks"

    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()

    def enqueue(self, val):
        "Enqueues val in the stack"
        self.st1.push(val)

    def dequeue(self):
        "Dequeues the queue"
        while self.st1.items != []:
            self.st2.push(self.st1.pop())
        popped = self.st2.pop()
        while self.st2.items != []:
            self.st1.push(self.st2.pop())

    def __str__(self):
        return str(self.st1)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue)
    queue.dequeue()
    print(queue)
