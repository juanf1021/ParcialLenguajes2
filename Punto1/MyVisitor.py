from RationalParser import RationalParser
from RationalVisitor import RationalVisitor
from fractions import Fraction

class MyVisitor(RationalVisitor):
    def visitMulDiv(self, ctx:RationalParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left is None or right is None:
            return None
        if ctx.op.text == '*':
            result = left * right
        else:
            if right == 0:
                return None
            result = left / right
        return result

    def visitAddSub(self, ctx:RationalParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left is None or right is None:
            return None
        if ctx.op.text == '+':
            result = left + right
        else:
            result = left - right
        return result

    def visitParens(self, ctx:RationalParser.ParensContext):
        result = self.visit(ctx.expr())
        return result

    def visitRationalNum(self, ctx:RationalParser.RationalNumContext):
        return self.visit(ctx.rationalExpr())

    def visitRationalExpr(self, ctx:RationalParser.RationalExprContext):
        numerator = int(ctx.INTEGER(0).getText())
        denominator = int(ctx.INTEGER(1).getText())
        if denominator == 0:
            return None
        result = Fraction(numerator, denominator)
        return result

