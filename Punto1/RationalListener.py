# Generated from Rational.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RationalParser import RationalParser
else:
    from RationalParser import RationalParser

# This class defines a complete listener for a parse tree produced by RationalParser.
class RationalListener(ParseTreeListener):

    # Enter a parse tree produced by RationalParser#MulDiv.
    def enterMulDiv(self, ctx:RationalParser.MulDivContext):
        pass

    # Exit a parse tree produced by RationalParser#MulDiv.
    def exitMulDiv(self, ctx:RationalParser.MulDivContext):
        pass


    # Enter a parse tree produced by RationalParser#AddSub.
    def enterAddSub(self, ctx:RationalParser.AddSubContext):
        pass

    # Exit a parse tree produced by RationalParser#AddSub.
    def exitAddSub(self, ctx:RationalParser.AddSubContext):
        pass


    # Enter a parse tree produced by RationalParser#Parens.
    def enterParens(self, ctx:RationalParser.ParensContext):
        pass

    # Exit a parse tree produced by RationalParser#Parens.
    def exitParens(self, ctx:RationalParser.ParensContext):
        pass


    # Enter a parse tree produced by RationalParser#RationalNum.
    def enterRationalNum(self, ctx:RationalParser.RationalNumContext):
        pass

    # Exit a parse tree produced by RationalParser#RationalNum.
    def exitRationalNum(self, ctx:RationalParser.RationalNumContext):
        pass


    # Enter a parse tree produced by RationalParser#rationalExpr.
    def enterRationalExpr(self, ctx:RationalParser.RationalExprContext):
        pass

    # Exit a parse tree produced by RationalParser#rationalExpr.
    def exitRationalExpr(self, ctx:RationalParser.RationalExprContext):
        pass



del RationalParser