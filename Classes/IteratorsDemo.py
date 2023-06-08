class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse("spam")
it = iter(rev)
print(next(it))  # m
print(next(it))  # a
print(next(it))  # p
print(next(it))  # s
for char in rev:
    print(char)
# m
# a
# p
# s
