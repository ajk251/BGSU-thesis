
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
    | domain
    | compiler
    | code
    | assign
    ;

// Test kinds ---------------------------------------------

assertion: ASSERT name ':' test_stub+ ';'                           #assert_test
         ;

test: TEST name domain_names ':' test_stub+ ';'                     #test_basic
//    | TEST name name ':' test_stub+ ';'                             #test_basic
//    | TEST name name ((',')? name+) ':' test_stub+ ';'              #test_basic_domains
    ;

domain_names: name                                                  #get_domain_name
            | name ((',')? name+)                                   #get_domain_names
            ;

// changed!!!
test_stub: BAR predicate                                            #stub_p
         | BAR predicate value                                      #stub_pv
         | BAR predicate value+                                     #stub_many_pv
         | BAR arg_list predicate value                             #stub_assert
         | BAR arg_list predicate                                   #stub_assert_p
         | BAR CODESMNT                                             #stub_code
         | BAR compiler*                                            #stub_directives
         | BAR test_logical                                         #stub_logical
         ;

test_logical: predicate value* (OP_LOGICAL predicate value*)*
            | test_logical OP_LOGICAL test_logical
            | '(' test_logical+ ')'
            ;

// Domain stuff -------------------------------------------

domain: 'Domain' name name                                          #make_domain
      | 'Domain' name name (value (value*))? (fn_arg (fn_arg*))?    #make_domain_args
      ;

// set parameters -----------------------------------------
compiler: DIRECTIVE dictate                                         #set_directive
//        | DIRECTIVE LIST
//        | DIRECTIVE NAME OP_EQ tuple...
        ;

fn_arg: FNARG dictate                                               #make_fn_directive
      ;

code: CODESMNT                                                      #make_codestmt
    ;

// setters ------------------------------------------------

assign: name ASSIGN value                                           #assign_value
      | name ASSIGN (name | CODESMNT) ':' value                     #assign_type_value
      ;

arg_list: '(' named_value (',' named_value)* ')'                    #args
        ;

value_list: '[' value (',' value)* ']'                              #make_list_c
          | '[' value (value)* ']'                                  #make_list
          ;

// identifiers --------------------------------------------

name: ID                                #get_name// must be a safe python name
    | LABEL                             #get_name// valid falcon identifer
    | OP_CARDINALITY name               #get_card
    | OP_LOGICAL name                   #get_not
    ;

predicate: name
         | CODESMNT
         | OP_NOT
         | OP_EQ
         | UMATH
         | OPERATORS
         ;

// add list?
value: name
     | NUMBER
     | STRING
     | CODESMNT
     ;

named_value: value                                                  #make_value
           | name '=' value                                         #make_name_value
           | value ':' value                                        #make_value_type
           | name '=' (name | CODESMNT) ':' value                   #make_name_type_value
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
OP_CARDINALITY: '#';

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

