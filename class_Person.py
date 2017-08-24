class Person(object):
    """The Person class represents people in a registry"""

    def __init__(self, name, weight):
        self.weight=weight
        self.name=name

    def health(self):
        if self.weight <= 80:
            print('Everything OK')
        else:
            print('Health not good')

class Child(Person):
    """The class \"Child`" is derived from the Person class"""

    def __init__(self, name, weight, age):
        Person.__init__(self, name, weight)

        self.weight=weight





