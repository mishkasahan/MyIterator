class MyIterator:
    def __init__(self, strinng):
        self.value = 0
        self.strinng = strinng

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= len(self.strinng):
            raise StopIteration
        result = self.strinng[self.value]
        self.value += 1
        return result


rjadok = input("Введіть свій рядок:")
myrange = MyIterator(rjadok)
for i in myrange:
    print(i)
