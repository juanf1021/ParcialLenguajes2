# Generated from MapFilter.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MapFilterParser import MapFilterParser
else:
    from MapFilterParser import MapFilterParser

# This class defines a complete listener for a parse tree produced by MapFilterParser.
class MapFilterListener(ParseTreeListener):

    # Enter a parse tree produced by MapFilterParser#program.
    def enterProgram(self, ctx:MapFilterParser.ProgramContext):
        pass

    # Exit a parse tree produced by MapFilterParser#program.
    def exitProgram(self, ctx:MapFilterParser.ProgramContext):
        pass


    # Enter a parse tree produced by MapFilterParser#mapOperation.
    def enterMapOperation(self, ctx:MapFilterParser.MapOperationContext):
        pass

    # Exit a parse tree produced by MapFilterParser#mapOperation.
    def exitMapOperation(self, ctx:MapFilterParser.MapOperationContext):
        pass


    # Enter a parse tree produced by MapFilterParser#filterOperation.
    def enterFilterOperation(self, ctx:MapFilterParser.FilterOperationContext):
        pass

    # Exit a parse tree produced by MapFilterParser#filterOperation.
    def exitFilterOperation(self, ctx:MapFilterParser.FilterOperationContext):
        pass


    # Enter a parse tree produced by MapFilterParser#function.
    def enterFunction(self, ctx:MapFilterParser.FunctionContext):
        pass

    # Exit a parse tree produced by MapFilterParser#function.
    def exitFunction(self, ctx:MapFilterParser.FunctionContext):
        pass


    # Enter a parse tree produced by MapFilterParser#condition.
    def enterCondition(self, ctx:MapFilterParser.ConditionContext):
        pass

    # Exit a parse tree produced by MapFilterParser#condition.
    def exitCondition(self, ctx:MapFilterParser.ConditionContext):
        pass


    # Enter a parse tree produced by MapFilterParser#iterable.
    def enterIterable(self, ctx:MapFilterParser.IterableContext):
        pass

    # Exit a parse tree produced by MapFilterParser#iterable.
    def exitIterable(self, ctx:MapFilterParser.IterableContext):
        pass


    # Enter a parse tree produced by MapFilterParser#list.
    def enterList(self, ctx:MapFilterParser.ListContext):
        pass

    # Exit a parse tree produced by MapFilterParser#list.
    def exitList(self, ctx:MapFilterParser.ListContext):
        pass


    # Enter a parse tree produced by MapFilterParser#expr.
    def enterExpr(self, ctx:MapFilterParser.ExprContext):
        pass

    # Exit a parse tree produced by MapFilterParser#expr.
    def exitExpr(self, ctx:MapFilterParser.ExprContext):
        pass


    # Enter a parse tree produced by MapFilterParser#comparisonOp.
    def enterComparisonOp(self, ctx:MapFilterParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by MapFilterParser#comparisonOp.
    def exitComparisonOp(self, ctx:MapFilterParser.ComparisonOpContext):
        pass



del MapFilterParser