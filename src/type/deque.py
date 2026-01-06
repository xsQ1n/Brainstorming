from linkedList import LinkedList


class Deque(object):
    def __init__(self):
        self.list = LinkedList()

    def is_empty(self):
        return self.list.is_empty()

    def size(self):
        return self.list.get_size()

    def add_first(self, e):
        self.list.add_first(e)

    def add_last(self, e):
        self.list.add_last(e)

    def remove_first(self):
        return self.list.remove_first()

    def remove_last(self):
        return self.list.remove_last()

    def peek_first(self):
        return self.list.get_first()

    def peek_last(self):
        return self.list.get_last()


if __name__ == "__main__":
    deque = Deque()
    deque.add_first(1)
    deque.add_first(2)
    deque.add_last(3)
    deque.add_last(4)

    print(deque.remove_first())  # 2
    print(deque.remove_last())  # 4
    print(deque.peek_first())  # 1
    print(deque.peek_last())  # 3
