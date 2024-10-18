# Generated from MapFilter.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,66,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,1,1,1,5,1,28,8,1,
        10,1,12,1,31,9,1,1,2,4,2,34,8,2,11,2,12,2,35,1,3,1,3,1,3,1,3,1,3,
        5,3,43,8,3,10,3,12,3,46,9,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,
        1,7,1,8,1,8,1,9,4,9,61,8,9,11,9,12,9,62,1,9,1,9,0,0,10,1,1,3,2,5,
        3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,1,0,5,3,0,65,90,95,95,97,122,
        4,0,48,57,65,90,95,95,97,122,1,0,48,57,1,0,34,34,3,0,9,10,13,13,
        32,32,70,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,
        0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,
        0,0,1,21,1,0,0,0,3,25,1,0,0,0,5,33,1,0,0,0,7,37,1,0,0,0,9,49,1,0,
        0,0,11,51,1,0,0,0,13,53,1,0,0,0,15,55,1,0,0,0,17,57,1,0,0,0,19,60,
        1,0,0,0,21,22,5,77,0,0,22,23,5,65,0,0,23,24,5,80,0,0,24,2,1,0,0,
        0,25,29,7,0,0,0,26,28,7,1,0,0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,
        1,0,0,0,29,30,1,0,0,0,30,4,1,0,0,0,31,29,1,0,0,0,32,34,7,2,0,0,33,
        32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,6,1,0,0,
        0,37,44,5,34,0,0,38,43,8,3,0,0,39,40,5,92,0,0,40,41,9,0,0,0,41,43,
        5,34,0,0,42,38,1,0,0,0,42,39,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,
        44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,47,48,5,34,0,0,48,8,1,
        0,0,0,49,50,5,40,0,0,50,10,1,0,0,0,51,52,5,41,0,0,52,12,1,0,0,0,
        53,54,5,91,0,0,54,14,1,0,0,0,55,56,5,93,0,0,56,16,1,0,0,0,57,58,
        5,44,0,0,58,18,1,0,0,0,59,61,7,4,0,0,60,59,1,0,0,0,61,62,1,0,0,0,
        62,60,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,65,6,9,0,0,65,20,1,
        0,0,0,6,0,29,35,42,44,62,1,6,0,0
    ]

class MapLanguageLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MAP = 1
    ID = 2
    NUMBER = 3
    STRING = 4
    LPAREN = 5
    RPAREN = 6
    LBRACK = 7
    RBRACK = 8
    COMMA = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'MAP'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "MAP", "ID", "NUMBER", "STRING", "LPAREN", "RPAREN", "LBRACK", 
            "RBRACK", "COMMA", "WS" ]

    ruleNames = [ "MAP", "ID", "NUMBER", "STRING", "LPAREN", "RPAREN", "LBRACK", 
                  "RBRACK", "COMMA", "WS" ]

    grammarFileName = "MapFilter.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


