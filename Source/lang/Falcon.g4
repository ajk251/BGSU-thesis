
// Useful examples:
//      for unicode:
//      https://github.com/antlr/grammars-v4/blob/master/python/python3/Python3Lexer.g4

// TODO:
//      - validate python names
//

grammar Falcon;

program: block+
       | EOF
       ;

block: namespace+
      | stmt+
      ;

namespace: name LBRAC stmt* RBRAC                                   #ns
         ;

stmt: test
    | compiler
    | CODESMNT
    ;

// Test kinds ---------------------------------------------

assertion: ASSERT name ':' test_stub+
         ;

test: TEST name name ':' test_stub+                                 #test_basic
    ;

test_stub: BAR predicate value    #stub_pv
         ;

// set parameters -----------------------------------------
compiler: DIRECTIVE (ID | NUMBER | STRING)                          #set_directive
//        | DIRECTIVE LIST
//        | DIRECTIVE NAME OP_EQ tuple...
        ;

//fn_arg: FNARG (NAME | NUMBER)
//      ;

// identifiers --------------------------------------------

name: ID                                // must be a safe python name
    | LABEL                             // valid falcon identifer
    ;

predicate: name
         | CODESMNT
         | OP_NOT
         | OP_EQ
         | UMATH
         | OPERATORS
//         | '_'
         ;

value: name
     | NUMBER
     | STRING
     | CODESMNT
     ;

// various operators --------------------------------------

// symbols used -------------
TEST:   'Test';
ASSERT: 'Assert';


LPAREN: '(';
RPAREN: ')';
LBRAC:  '{';
RBRAC:  '}';

ASSIGN: ':=' | '≔';
BAR: '|';

// others?
//OP_REALS: 'ℝ';
//OP_NATS:  'ℕ';

// NOR?
OP_LOGICAL: OP_AND | OP_NAND | OP_OR | OP_XOR;
OP_AND:  '∧' | '&&' | 'and';
OP_NAND: '⊼';
OP_OR:   '∨' | '||' | 'or';
OP_XOR:  '⊻';

OP_NOT:  '￢' | '!';

// kinds of names used ------
DIRECTIVE: ':' (CHAR | [-_])*;
FNARG:     '-' (CHAR | [-_])*;

//FID: (CHAR | '_')(CHAR | DIGIT | [-_+&?])*;
ID: (CHAR | '_')(CHAR | DIGIT | [_.])*;

//CODE: CODESMNT
//    | STRING
//    | NUMBER
//    ;

OPERATORS: [><≤≥] | '<=' | '>=' | '==' | '±';

//PREDICATE: ID
//         | CODESMNT
//         | OP_NOT
//         | OP_EQ
//         | UMATH
//         | [><≤≥] | '<=' | '>=' | '=='
//         | '±'                                  // these aren't in MATH
////         | '_'
//         ;

OP_EQ:  '=';

// CODE/ID is meant to represent the variable names used in most languages
// LABEL is meant to have a more liberal/loose name-ing scheme, Racket-like
//CODE: (CHAR | '_')(CHAR | DIGIT | [_.])*;
LABEL: (CHAR | '_')(CHAR | DIGIT | [-_+&~?])*;

// could do more...
NUMBER: ('+'|'-')? DIGIT+                       // integer
      | ('+'|'-')? DIGIT+ '.' [0-9]*            // float
      | ('+'|'-')? DIGIT* '.' [0-9]+            // float
      ;

STRING: '"' .*? '"'
      | '\'' .*? '\''
      ;

CODESMNT: '`' .*? '`';
UMATH: '\u2200'..'\u22FF';             // this should break this up…

// misc ---------------------
COMMENT: '//' .*? '\n'                      -> skip;
MCOMMENT: '/*' .*? '*/'                     -> skip;
WS: [ \t\r\n]                               -> skip;

fragment DIGIT: ([0-9]);
fragment CHAR: [a-zA-Z];

