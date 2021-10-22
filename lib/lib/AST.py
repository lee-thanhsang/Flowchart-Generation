from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List
from Visitor import Visitor

class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self,param)


class Inst(AST):
    __metaclass__ = ABCMeta
    pass


class Stmt(AST):
    __metaclass__ = ABCMeta
    pass


@dataclass
class Expr(Inst):
    value: str
    
    def __str__(self):
        return self.value

    def accept(self, v):
        return v.visitExpr(self)


@dataclass
class VarDecl(Inst):
    decl: str

    def accept(self, v):
        return v.visitVarDecl(self)


@dataclass
class FuncDecl(Inst):
    input: List[VarDecl]
    body: List[Inst]

    def accept(self, v):
        return v.visitFuncDecl(self)


@dataclass
class Assign(Stmt):
    assign: str

    def accept(self, v):
        return v.visitAssign(self)


@dataclass
class If(Stmt):
    condition: Expr
    ifthenStmt: List[Inst]
    elseStmt: List[Inst]

    def accept(self, v):
        return v.visitIf(self)


@dataclass
class For(Stmt):
    init: VarDecl
    condition: Expr
    update: Assign

    def accept(self, v):
        return v.visitFor(self)


@dataclass
class While(Stmt):
    condition: Expr
    body: List[Stmt]

    def accept(self, v):
        return v.visitWhile(self)


@dataclass
class DoWhile(Stmt):
    condition: Expr
    body: List[Stmt]

    def accept(self, v):
        return v.visitDoWhile(self)


@dataclass
class Break(Stmt):
    def accept(self, v):
        return v.visitBreak(self)


@dataclass
class Continue(Stmt):
    def accept(self, v):
        return v.visitContinue(self)


@dataclass
class Return(Stmt):
    expr: Expr

    def accept(self, v):
        return v.visitReturn(self)