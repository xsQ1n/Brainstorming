class ArrayList(object):
    # 默认初始容量
    INIT_CAP = 1

    def __init__(self, init_capacity=None):
        self.data = [None] * (
            init_capacity if init_capacity is not None else self.__class__.INIT_CAP
        )
        self.size = 0

    # 增
    def add_last(self, e):
        cap = len(self.data)
        # check capacity
        if self.size == cap:
            self._resize(2 * cap)

        self.data[self.size] = e
        self.size += 1

    def add(self, index, e):
        self._check_element_index(index)

        cap = len(self.data)
        if self.size == cap:
            self._resize(2 * cap)

        for i in range(self.size - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]

        self.data[index] = e
        self.size += 1

    # 删
    def remove_last(self):
        if self.size == 0:
            raise IndexError("ArrayList is empty")

        cap = len(self.data)
        # check cap
        if self.size == cap // 4:
            self._resize(cap // 2)

        del_val = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1

    def remove(self, index):
        self._check_element_index(index)

        cap = len(self.data)

        del_val = self.data[index]

        for i in range(index + 1, self.size):
            self.data[i - 1] = self.data[i]
        # 移位之后，最后一个元素置空
        self.data[self.size - 1] = None
        self.size -= 1

        if self.size == cap // 4:
            self._resize(cap // 2)

    # 改
    def set(self, index, e):
        # check index
        self._check_element_index(index)
        self.data[index] = e

    # 查
    def get(self, index):
        # check index
        self._check_element_index(index)

        return self.data[index]

    # 工具方法
    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    # expand capacity
    def _resize(self, new_capacity):
        tmp = [None] * new_capacity
        for i in range(self.size):
            tmp[i] = self.data[i]
        self.data = tmp

    def _is_element_index(self, index):
        return 0 <= index < self.size

    def _is_position_index(self, index):
        return 0 <= index <= self.size

    def _check_element_index(self, index):
        if not self._is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def _check_position_index(self, index):
        if not self._is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def display(self):
        print(f"ArrayList size: {self.size}, capacity: {len(self.data)}")
        print(self.data)


if __name__ == "__main__":
    arr = ArrayList(3)

    for i in range(1, 6):
        arr.add_last(i)
    arr.display()

    arr.remove_last()
    arr.display()

    arr.remove(2)
    arr.display()

    arr.add(1, 3)
    arr.display()
