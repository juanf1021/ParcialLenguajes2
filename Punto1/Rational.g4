grammar Rational;

expr: expr op=('*'|'/') expr   # MulDiv
    | expr op=('+'|'-') expr   # AddSub
    | '(' expr ')'             # Parens
    | rationalExpr             # RationalNum
    ;

rationalExpr: INTEGER '/' INTEGER;

INTEGER: [0-9]+;
WS: [ \t\r\n]+ -> skip;
