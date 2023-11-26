class MyClass:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"String representation: {self.data}"

    def __repr__(self):
        return f"Repr representation: {self.data}"

# Creating an instance of MyClass
obj = MyClass(42)
print(obj)
print(repr(obj))