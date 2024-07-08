import random

class Person:
    def __init__(self, name):
        self.name = name




    def __str__(self):
        return f"{self.__class__.__qualname__}(name = {self.name})"

class RandomStuff:
    def __init__(self, iterable):
        self._items = list(iterable)
        random.shuffle(self._items)

    def __call__(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("There are no more items!")
    def __str__(self):
        return f"{','.join([ str(_) for _ in self._items])}"

#testdrive

numbers = RandomStuff(range(20))
print(numbers)
print(numbers())

people = RandomStuff([Person(name = 'Daniel'), Person(name = 'Gabriel'), Person(name = 'Naomi')])

print(people)
print(people())
