grammar Sample;

query     : 'outfit' '(' fields? ')' EOF ;
fields    : field (',' field)* ;
field     : ID '=' ID ;

ID        : [a-zA-Z_][a-zA-Z0-9_]* ;
WS        : [ \t\r\n]+ -> skip ;
