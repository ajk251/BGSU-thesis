
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

namespace: name LBRAC stmt* RBRAC                                   #ns
         ;

stmt: test
    | assertion
    | compiler
    | code
    | assign
    ;

// Test kinds ---------------------------------------------

assertion: ASSERT name ':' test_stub+ ';'                           #assert_test
         ;

test: TEST name name ':' test_stub+ ';'                             #test_basic
    ;

test_stub: BAR predicate value                                      #stub_pv
         | BAR predicate value+                                     #stub_many_pv
         | BAR arg_list predicate value                             #stub_assert
         | BAR CODESMNT                                             #stub_code
         | BAR compiler*                                            #stub_directives
         ;

// set parameters -----------------------------------------
compiler: DIRECTIVE dictate                                         #set_directive
//        | DIRECTIVE LIST
//        | DIRECTIVE NAME OP_EQ tuple...
        ;

//fn_arg: FNARG (NAME | NUMBER)
//      ;

code: CODESMNT                                                      #make_codestmt
    ;

// setters ------------------------------------------------

assign: name ASSIGN value                                           #assign_value
      | name ASSIGN (name | CODESMNT) ':' value                     #assign_type_value
      ;

arg_list: '(' named_value (',' named_value)* ')'                 #args
        ;

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

named_value: value                                      #make_value
           | name '=' value                             #make_name_value
           | value ':' value                            #make_value_type
           | name '=' (name | CODESMNT) ':' value       #make_name_type_value
           ;

dictate: name
     | NUMBER
     | STRING
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
COLON: ':';

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
DIRECTIVE: COLON (CHAR | [-_])*;
FNARG:     '-' (CHAR | [-_])*;

ID: (CHAR | '_')(CHAR | DIGIT | [_.])*;

OPERATORS: [><≤≥] | '<=' | '>=' | '==' | '±';

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
//WS: [ \t\r]                               -> skip;
NL: '\n';


fragment DIGIT: ([0-9]);
fragment CHAR: [a-zA-Z];

