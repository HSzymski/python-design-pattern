"""
The Interpreter design pattern is a behavioral design pattern that specifies how to evaluate sentences in a language.
This pattern is used to interpret sentences in a language and represents a grammar as a hierarchy of composite objects.

In a nutshel: The Interpreter pattern helps to convert information from one language into another.
"""


class AbstractExpression:
    def interpret(self):
        pass


class TerminalExpression(AbstractExpression):
    def interpret(self):
        print("Terminal expression is being interpreted.")


class NonterminalExpression(AbstractExpression):
    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        print("Nonterminal expression is being interpreted.")
        self._expression.interpret()


terminal_expression = TerminalExpression()
nonterminal_expression = NonterminalExpression(terminal_expression)

nonterminal_expression.interpret()
