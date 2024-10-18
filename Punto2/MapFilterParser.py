# Generated from MapFilter.g4 by ANTLR 4.13.1
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
        4,1,17,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,
        1,5,1,5,5,5,48,8,5,10,5,12,5,51,9,5,3,5,53,8,5,1,5,1,5,1,6,1,6,1,
        7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,2,1,0,14,16,1,0,6,11,55,0,16,
        1,0,0,0,2,33,1,0,0,0,4,35,1,0,0,0,6,37,1,0,0,0,8,41,1,0,0,0,10,43,
        1,0,0,0,12,56,1,0,0,0,14,58,1,0,0,0,16,17,3,2,1,0,17,18,5,0,0,1,
        18,1,1,0,0,0,19,20,5,12,0,0,20,21,5,1,0,0,21,22,3,4,2,0,22,23,5,
        2,0,0,23,24,3,8,4,0,24,25,5,3,0,0,25,34,1,0,0,0,26,27,5,13,0,0,27,
        28,5,1,0,0,28,29,3,6,3,0,29,30,5,2,0,0,30,31,3,8,4,0,31,32,5,3,0,
        0,32,34,1,0,0,0,33,19,1,0,0,0,33,26,1,0,0,0,34,3,1,0,0,0,35,36,5,
        14,0,0,36,5,1,0,0,0,37,38,5,14,0,0,38,39,3,14,7,0,39,40,3,12,6,0,
        40,7,1,0,0,0,41,42,3,10,5,0,42,9,1,0,0,0,43,52,5,4,0,0,44,49,3,12,
        6,0,45,46,5,2,0,0,46,48,3,12,6,0,47,45,1,0,0,0,48,51,1,0,0,0,49,
        47,1,0,0,0,49,50,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,52,44,1,0,0,
        0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,5,5,0,0,55,11,1,0,0,0,56,57,
        7,0,0,0,57,13,1,0,0,0,58,59,7,1,0,0,59,15,1,0,0,0,3,33,49,52
    ]

class MapFilterParser ( Parser ):

    grammarFileName = "MapFilter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'['", "']'", "'>'", 
                     "'<'", "'>='", "'<='", "'=='", "'!='", "'MAP'", "'FILTER'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MAP", "FILTER", "ID", "NUMBER", "STRING", "WS" ]

    RULE_program = 0
    RULE_operation = 1
    RULE_function = 2
    RULE_condition = 3
    RULE_iterable = 4
    RULE_list = 5
    RULE_expr = 6
    RULE_comparisonOp = 7

    ruleNames =  [ "program", "operation", "function", "condition", "iterable", 
                   "list", "expr", "comparisonOp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    MAP=12
    FILTER=13
    ID=14
    NUMBER=15
    STRING=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self):
            return self.getTypedRuleContext(MapFilterParser.OperationContext,0)


        def EOF(self):
            return self.getToken(MapFilterParser.EOF, 0)

        def getRuleIndex(self):
            return MapFilterParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MapFilterParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.operation()
            self.state = 17
            self.match(MapFilterParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MapFilterParser.RULE_operation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MapOperationContext(OperationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MapFilterParser.OperationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MAP(self):
            return self.getToken(MapFilterParser.MAP, 0)
        def function(self):
            return self.getTypedRuleContext(MapFilterParser.FunctionContext,0)

        def iterable(self):
            return self.getTypedRuleContext(MapFilterParser.IterableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapOperation" ):
                listener.enterMapOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapOperation" ):
                listener.exitMapOperation(self)


    class FilterOperationContext(OperationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MapFilterParser.OperationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FILTER(self):
            return self.getToken(MapFilterParser.FILTER, 0)
        def condition(self):
            return self.getTypedRuleContext(MapFilterParser.ConditionContext,0)

        def iterable(self):
            return self.getTypedRuleContext(MapFilterParser.IterableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterOperation" ):
                listener.enterFilterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterOperation" ):
                listener.exitFilterOperation(self)



    def operation(self):

        localctx = MapFilterParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_operation)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = MapFilterParser.MapOperationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(MapFilterParser.MAP)
                self.state = 20
                self.match(MapFilterParser.T__0)
                self.state = 21
                self.function()
                self.state = 22
                self.match(MapFilterParser.T__1)
                self.state = 23
                self.iterable()
                self.state = 24
                self.match(MapFilterParser.T__2)
                pass
            elif token in [13]:
                localctx = MapFilterParser.FilterOperationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(MapFilterParser.FILTER)
                self.state = 27
                self.match(MapFilterParser.T__0)
                self.state = 28
                self.condition()
                self.state = 29
                self.match(MapFilterParser.T__1)
                self.state = 30
                self.iterable()
                self.state = 31
                self.match(MapFilterParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

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
            return self.getToken(MapFilterParser.ID, 0)

        def getRuleIndex(self):
            return MapFilterParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = MapFilterParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(MapFilterParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MapFilterParser.ID, 0)

        def comparisonOp(self):
            return self.getTypedRuleContext(MapFilterParser.ComparisonOpContext,0)


        def expr(self):
            return self.getTypedRuleContext(MapFilterParser.ExprContext,0)


        def getRuleIndex(self):
            return MapFilterParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = MapFilterParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(MapFilterParser.ID)
            self.state = 38
            self.comparisonOp()
            self.state = 39
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(MapFilterParser.ListContext,0)


        def getRuleIndex(self):
            return MapFilterParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)




    def iterable(self):

        localctx = MapFilterParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_iterable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.list_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapFilterParser.ExprContext)
            else:
                return self.getTypedRuleContext(MapFilterParser.ExprContext,i)


        def getRuleIndex(self):
            return MapFilterParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)




    def list_(self):

        localctx = MapFilterParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(MapFilterParser.T__3)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0):
                self.state = 44
                self.expr()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 45
                    self.match(MapFilterParser.T__1)
                    self.state = 46
                    self.expr()
                    self.state = 51
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 54
            self.match(MapFilterParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MapFilterParser.ID, 0)

        def NUMBER(self):
            return self.getToken(MapFilterParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(MapFilterParser.STRING, 0)

        def getRuleIndex(self):
            return MapFilterParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = MapFilterParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MapFilterParser.RULE_comparisonOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOp" ):
                listener.enterComparisonOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOp" ):
                listener.exitComparisonOp(self)




    def comparisonOp(self):

        localctx = MapFilterParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comparisonOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





