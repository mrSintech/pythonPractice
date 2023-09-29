class CallableClass:
    def __init__(self):
        self.value = 0

    def __call__(self, x):
        self.value += x
        return self.value


# Create an instance of CallableClass
callable_obj = CallableClass()

# Use the instance as a callable
result1 = callable_obj(5)
result2 = callable_obj(10)

print(result1)  # Output: 5
print(result2)  # Output: 15
