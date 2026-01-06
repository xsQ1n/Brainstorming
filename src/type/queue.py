from collections import deque


class StackByList(object):
    # LIFO
    def __init__(self):
        self.list = deque()

    def push(self, e):
        self.list.append(e)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)


class StackByArray(object):
    def __init__(self):
        self.arr = []

    def push(self, e):
        self.arr.append(e)

    def pop(self):
        return self.arr.pop()

    def peek(self):
        return self.arr[-1]

    def size(self):
        return len(self.arr)


class QueueByList(object):
    # FIFO
    def __init__(self):
        self.list = deque()

    def push(self, e):
        self.list.append(e)

    def pop(self):
        return self.list.popleft()

    def peek(self):
        return self.list[0]

    def size(self):
        return len(self.list)


class QueueByArray(object):
    def __init__(self):
        self.arr = []

    def push(self, e):
        self.arr.append(e)

    def pop(self):
        val = self.arr[0]
        return self.arr.pop(0)

    def peek(self):
        return self.arr[0]

    def size(self):
        return len(self.arr)


if __name__ == "__main__":
    stack = StackByList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
    print("\n")

    stack = StackByArray()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
    print("\n")

    queue = QueueByList()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.peek())  # 1
    print(queue.pop())  # 1
    print(queue.pop())  # 2
    print(queue.peek())  # 3
    print("\n")

    queue = QueueByArray()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.peek())  # 1
    print(queue.pop())  # 1
    print(queue.pop())  # 2
    print(queue.peek())  # 3
