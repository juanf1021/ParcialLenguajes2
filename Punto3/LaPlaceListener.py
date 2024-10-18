# Generated from LaPlace.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LaPlaceParser import LaPlaceParser
else:
    from LaPlaceParser import LaPlaceParser

# This class defines a complete listener for a parse tree produced by LaPlaceParser.
class LaPlaceListener(ParseTreeListener):

    # Enter a parse tree produced by LaPlaceParser#start.
    def enterStart(self, ctx:LaPlaceParser.StartContext):
        pass

    # Exit a parse tree produced by LaPlaceParser#start.
    def exitStart(self, ctx:LaPlaceParser.StartContext):
        pass


    # Enter a parse tree produced by LaPlaceParser#integral.
    def enterIntegral(self, ctx:LaPlaceParser.IntegralContext):
        pass

    # Exit a parse tree produced by LaPlaceParser#integral.
    def exitIntegral(self, ctx:LaPlaceParser.IntegralContext):
        pass


    # Enter a parse tree produced by LaPlaceParser#expression.
    def enterExpression(self, ctx:LaPlaceParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LaPlaceParser#expression.
    def exitExpression(self, ctx:LaPlaceParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LaPlaceParser#term.
    def enterTerm(self, ctx:LaPlaceParser.TermContext):
        pass

    # Exit a parse tree produced by LaPlaceParser#term.
    def exitTerm(self, ctx:LaPlaceParser.TermContext):
        pass


    # Enter a parse tree produced by LaPlaceParser#function.
    def enterFunction(self, ctx:LaPlaceParser.FunctionContext):
        pass

    # Exit a parse tree produced by LaPlaceParser#function.
    def exitFunction(self, ctx:LaPlaceParser.FunctionContext):
        pass



del LaPlaceParser