class Person(object):
    """The Person class represents people in a registry"""

    def __init__(self, name, weight):
        self.weight=weight
        self.name=name


class Child(Person):
    """The class \"Child`" is derived from the Person class"""

    def __init__(self, name, weight, age):
        Person.__init__(self, name, weight)

        self.weight=weight





