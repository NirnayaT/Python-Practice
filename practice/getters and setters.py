class MyClass:
    def __init__(self, value):
        self._value = value

    @property#GETTERS
    def value(self):
        print(self._value)

    @value.setter#SETTERS
    def value(self, new_value):
        self._value = new_value

obj1= MyClass(20)
obj1.value = 10
obj1.value