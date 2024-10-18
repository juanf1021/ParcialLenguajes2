# Generated from Rational.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RationalParser import RationalParser
else:
    from RationalParser import RationalParser

# This class defines a complete generic visitor for a parse tree produced by RationalParser.

class RationalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RationalParser#MulDiv.
    def visitMulDiv(self, ctx:RationalParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RationalParser#AddSub.
    def visitAddSub(self, ctx:RationalParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RationalParser#Parens.
    def visitParens(self, ctx:RationalParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RationalParser#RationalNum.
    def visitRationalNum(self, ctx:RationalParser.RationalNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RationalParser#rationalExpr.
    def visitRationalExpr(self, ctx:RationalParser.RationalExprContext):
        return self.visitChildren(ctx)



del RationalParser