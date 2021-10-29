
// Useful examples:
//      for unicode:
//      https://github.com/antlr/grammars-v4/blob/master/python/python3/Python3Lexer.g4

grammar Falcon;

program: block+
       | EOF
       ;

block: namespace+
      | stmt+
      ;

namespace: name OP_LBRAC stmt* OP_RBRAC                      #ns
         ;

stmt: test
    | compiler
    | CODESMNT
    ;

// Test kinds ---------------------------------------------

test: OP_TEST ID ID ':' test_stub+                                  #test_basic
    ;

test_stub: OP_BAR (name | PREDICATE) (name | CODE)                           #stub_pv
         ;

// set parameters -----------------------------------------
compiler: DIRECTIVE ID                                             #set_directive
//        | DIRECTIVE LIST
//        | DIRECTIVE NAME OP_EQ tuple...
        ;

//fn_arg: FNARG (NAME | NUMBER)
//      ;

name: ID                                // must be a safe python name
    | LABEL                             // valid falcon identifer
    ;

// various operators --------------------------------------

// symbols used -------------
OP_TEST:   'Test';
OP_LPAREN: '(';
OP_RPAREN: ')';
OP_LBRAC:  '{';
OP_RBRAC:  '}';

OP_ASSIGN: ':=' | '≔';
OP_BAR: '|';

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

CODE: CODESMNT
    | STRING
    | NUMBER
    ;

PREDICATE: ID
         | CODESMNT
         | OP_NOT
         | OP_EQ
         | UMATH
         | [><≤≥] | '<=' | '>=' | '=='
         | '±'
//         | '_'
         ;

OP_EQ:  '=';

// CODE is meant to represent the variable names used in most languages
// NAME is meant to have a more liberal/loose name-ing scheme, Racket-like
//CODE: (CHAR | '_')(CHAR | DIGIT | [_.])*;
LABEL: (CHAR | '_')(CHAR | DIGIT | [-_+&?])*;

// could do more...
NUMBER: ('+'|'-')? DIGIT+                        // integer
      | ('+'|'-')? DIGIT+ '.' [0-9]*            // float
      | ('+'|'-')? DIGIT* '.' [0-9]+            // float
      ;

STRING: '"' .*? '"'
      | '\'' .*? '\''
      ;

CODESMNT: '`' .*? '`';

// misc ---------------------
COMMENT: '//' .*? '\n'                      -> skip;
MCOMMENT: '/*' .*? '*/'                     -> skip;
WS: [ \t\r\n]                               -> skip;

fragment DIGIT: ([0-9]);
fragment CHAR: [a-zA-Z];
fragment UMATH: '\u2200'..'\u22FF';             // this should be more limited
