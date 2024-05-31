"""
In Python, context managers are implemented using the with statement. The with statement provides a way to wrap a block
of code with methods defined by a context manager. When the block of code is entered, the __enter__() method of the
context manager is called, and when the block of code is exited, the __exit__() method is called.
"""

class ContextManager:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return None


with ContextManager() as cm:
    print('Do something with: cm')