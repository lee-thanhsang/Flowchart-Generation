from abc import ABC, abstractmethod, ABCMeta


class Visitor(ABC):

    def visit(self, ast):
        return ast.accept(self)

    @abstractmethod
    def visitFuncDecl(self):
        pass

    @abstractmethod
    def visitVarDecl(self):
        pass

    @abstractmethod
    def visitAssign(self):
        pass

    @abstractmethod
    def visitIf(self):
        pass

    @abstractmethod
    def visitFor(self):
        pass

    @abstractmethod
    def visitWhile(self):
        pass

    @abstractmethod
    def visitBreak(self):
        pass

    @abstractmethod
    def visitContinue(self):
        pass

    @abstractmethod
    def visitReturn(self):
        pass

    @abstractmethod
    def visitExpr(self):
        pass