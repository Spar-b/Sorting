class CustomList:
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            if step is None:
                step = 1
            return [self.data[i] for i in range(start, stop, step)]
        else:
            return self.data[index]

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            if step is None:
                step = 1
            for i in range(start, stop, step):
                self.data[i] = value[i - start]
        else:
            self.data[index] = value

    def append(self, value):
        self.data.append(value)

    def insert(self, index, value):
        self.data.insert(index, value)

    def pop(self, index=-1):
        return self.data.pop(index)

    def delete(self, index):
        del self.data[index]

    def to_builtin_list(self):
        return self.data

    def __len__(self):
        return len(self.data)
