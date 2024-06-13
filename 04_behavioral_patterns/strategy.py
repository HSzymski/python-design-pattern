"""
The Strategy design pattern is a behavioral design pattern that allows you to define a family of algorithms,
encapsulate each one, and make them interchangeable. The Strategy pattern lets the algorithm vary independently
from the clients that use it.


Comment from stack (https://stackoverflow.com/questions/1658192/what-is-the-difference-between-strategy-design-pattern-and-state-design-pattern)
Honestly, the two patterns are pretty similar in practice, and the defining difference between them tends to vary
depending on who you ask. Some popular choices are:
- States store a reference to the context object that contains them. Strategies do not.
- States are allowed to replace themselves (IE: to change the state of the context object to something else), while
Strategies are not.
- Strategies are passed to the context object as parameters, while States are created by the context object itself.
- Strategies only handle a single, specific task, while States provide the underlying implementation for everything
(or most everything) the context object does.
"""
