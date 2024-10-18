grammar LaPlace;

// Regla de entrada
start: integral ;  // Cambié 'input' a 'start'
integral: 'int' '0' 'infinity' expression 'dt' ;
expression: term ('*' term)* ;
term: function | ID | INT | '(' expression ')' ;
function: ID '(' expression ')' ;

// Identificadores y números
ID: [a-zA-Z]+ ;
INT: [0-9]+ ;

// Ignorar espacios en blanco
WS: [ \t\n\r]+ -> skip ;
