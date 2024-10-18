# Generated from LaPlace.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,41,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,22,8,2,10,2,12,2,25,9,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,34,8,3,1,4,1,4,1,4,1,4,1,4,1,4,0,0,5,0,
        2,4,6,8,0,0,39,0,10,1,0,0,0,2,12,1,0,0,0,4,18,1,0,0,0,6,33,1,0,0,
        0,8,35,1,0,0,0,10,11,3,2,1,0,11,1,1,0,0,0,12,13,5,1,0,0,13,14,5,
        2,0,0,14,15,5,3,0,0,15,16,3,4,2,0,16,17,5,4,0,0,17,3,1,0,0,0,18,
        23,3,6,3,0,19,20,5,5,0,0,20,22,3,6,3,0,21,19,1,0,0,0,22,25,1,0,0,
        0,23,21,1,0,0,0,23,24,1,0,0,0,24,5,1,0,0,0,25,23,1,0,0,0,26,34,3,
        8,4,0,27,34,5,8,0,0,28,34,5,9,0,0,29,30,5,6,0,0,30,31,3,4,2,0,31,
        32,5,7,0,0,32,34,1,0,0,0,33,26,1,0,0,0,33,27,1,0,0,0,33,28,1,0,0,
        0,33,29,1,0,0,0,34,7,1,0,0,0,35,36,5,8,0,0,36,37,5,6,0,0,37,38,3,
        4,2,0,38,39,5,7,0,0,39,9,1,0,0,0,2,23,33
    ]

class LaPlaceParser ( Parser ):

    grammarFileName = "LaPlace.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'0'", "'infinity'", "'dt'", 
                     "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "WS" ]

    RULE_start = 0
    RULE_integral = 1
    RULE_expression = 2
    RULE_term = 3
    RULE_function = 4

    ruleNames =  [ "start", "integral", "expression", "term", "function" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    ID=8
    INT=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integral(self):
            return self.getTypedRuleContext(LaPlaceParser.IntegralContext,0)


        def getRuleIndex(self):
            return LaPlaceParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = LaPlaceParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.integral()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LaPlaceParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LaPlaceParser.RULE_integral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegral" ):
                listener.enterIntegral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegral" ):
                listener.exitIntegral(self)




    def integral(self):

        localctx = LaPlaceParser.IntegralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_integral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(LaPlaceParser.T__0)
            self.state = 13
            self.match(LaPlaceParser.T__1)
            self.state = 14
            self.match(LaPlaceParser.T__2)
            self.state = 15
            self.expression()
            self.state = 16
            self.match(LaPlaceParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaPlaceParser.TermContext)
            else:
                return self.getTypedRuleContext(LaPlaceParser.TermContext,i)


        def getRuleIndex(self):
            return LaPlaceParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = LaPlaceParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.term()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 19
                self.match(LaPlaceParser.T__4)
                self.state = 20
                self.term()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(LaPlaceParser.FunctionContext,0)


        def ID(self):
            return self.getToken(LaPlaceParser.ID, 0)

        def INT(self):
            return self.getToken(LaPlaceParser.INT, 0)

        def expression(self):
            return self.getTypedRuleContext(LaPlaceParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LaPlaceParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = LaPlaceParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.function()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(LaPlaceParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.match(LaPlaceParser.INT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.match(LaPlaceParser.T__5)
                self.state = 30
                self.expression()
                self.state = 31
                self.match(LaPlaceParser.T__6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LaPlaceParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(LaPlaceParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LaPlaceParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = LaPlaceParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(LaPlaceParser.ID)
            self.state = 36
            self.match(LaPlaceParser.T__5)
            self.state = 37
            self.expression()
            self.state = 38
            self.match(LaPlaceParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





