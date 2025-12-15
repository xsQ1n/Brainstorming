class LinkedList(object):

    class Node(object):
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = self.Node(None)
        self.tail = self.head
        self.size = 0

    def add_first(self, e):
        node = self.Node(e)
        node.next = self.head.next
        self.head.next = node
        if self.size == 0:
            self.tail = node
        self.size += 1

    def add_last(self, e):
        node = self.Node(e)
        self.tail.next = node
        self.tail = node
        self.size += 1

    def add(self, index, e):
        self._check_position_index(index)

        if index == self.size:
            self.add_last(e)

        node = self.Node(e)
        tmp = self.head
        # 找到插入位置的前一个节点
        for i in range(index):
            tmp = tmp.next

        node.next = tmp.next
        tmp.next = node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise IndexError("LinkedList is empty")

        prev = self.head.next
        self.head.next = prev.next
        if self.size == 1:
            self.tail = self.head
        prev.next = None
        self.size -= 1

    def remove_last(self):
        if self.is_empty():
            raise IndexError("LinkedList is empty")

        prev = self.head
        while prev.next != self.tail:
            prev = prev.next
        prev.next = None
        self.tail = prev
        self.size -= 1

    def remove(self, index):
        self._check_element_index(index)

        prev = self.head
        for i in range(index):
            prev = prev.next

        tmp = prev.next
        prev.next = tmp.next
        # 删除的最后一个元素，需要更新tail指针
        if index == self.size - 1:
            self.tail = prev
        self.size -= 1

    def set(self, index, e):
        self._check_element_index(index)
        node = self.get(index)
        node.val = e

    def get_first(self):
        if self.is_empty():
            raise IndexError("LinkedList is empty")
        return self.head.next.val

    def get_last(self):
        if self.is_empty():
            raise IndexError("LinkedList is empty")
        return self.tail.val

    def get(self, index):
        self._check_element_index(index)
        prev = self.head
        for i in range(index):
            prev = prev.next

        return prev.next

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _is_element_index(self, index):
        return 0 < index < self.size

    def _is_position_index(self, index):
        return 0 <= index <= self.size

    def _check_element_index(self, index):
        if not self._is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def _check_position_index(self, index):
        if not self._is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")


if __name__ == "__main__":
    list = LinkedList()
    list.add_first(1)
    list.add_first(2)
    list.add_last(3)
    list.add_last(4)
    list.add(2, 5)

    print(list.remove_first())
    print(list.remove_last())
    print(list.remove(1))

    print(list.get_first())  # 1
    print(list.get_last())  # 3
    print(list.get(1).val)  # 3
