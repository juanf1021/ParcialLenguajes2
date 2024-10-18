grammar MapFilter;

program: operation EOF;

operation
    : MAP '(' function ',' iterable ')'    # mapOperation
    | FILTER '(' condition ',' iterable ')' # filterOperation
    ;

function: ID;
condition: ID comparisonOp expr;
iterable: list;
list: '[' (expr (',' expr)*)? ']';

expr: ID | NUMBER | STRING;

comparisonOp: '>' | '<' | '>=' | '<=' | '==' | '!=';

MAP: 'MAP';
FILTER: 'FILTER';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [-]?[0-9]+('.'[0-9]+)?;
STRING: '\'' .*? '\'';
WS: [ \t\r\n]+ -> skip;
