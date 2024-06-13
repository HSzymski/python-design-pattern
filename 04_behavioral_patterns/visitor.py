"""
The Visitor design pattern is a behavioral design pattern that allows you to add new behaviors to existing class
hierarchies without altering any existing code. It works by creating a separate visitor class that implements all the
appropriate specializations of a particular operation for all classes of an object structure.
"""


class Element:
    def accept(self, visitor):
        visitor.visit(self)


class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)


class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)


class Visitor:
    def visit(self, element):
        pass


class ConcreteVisitor1(Visitor):

    def visit_concrete_element_a(self, element):
        print("ConcreteVisitor1 visited ConcreteElementA")


    def visit_concrete_element_b(self, element):
        print("ConcreteVisitor1 visited ConcreteElementB")


class ConcreteVisitor2(Visitor):

    def visit_concrete_element_a(self, element):
        print("ConcreteVisitor2 visited ConcreteElementA")


    def visit_concrete_element_b(self, element):
        print("ConcreteVisitor2 visited ConcreteElementB")


element_a = ConcreteElementA()
element_b = ConcreteElementB()
visitor1 = ConcreteVisitor1()
visitor2 = ConcreteVisitor2()
element_a.accept(visitor1)

element_b.accept(visitor1)

element_a.accept(visitor2)

element_b.accept(visitor2)
