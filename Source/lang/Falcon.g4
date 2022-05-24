
// Useful examples:
//      for unicode:
//      https://github.com/antlr/grammars-v4/blob/master/python/python3/Python3Lexer.g4

grammar Falcon;

block: namespace+
      | stmt+
      ;

namespace: name LBRAC stmt* RBRAC                                   #ns
         ;

stmt: test
    | assertion
    | groupby_test
    | winnow_test
    | satisfy_test
    | macro
    | domain
    | compiler
    | code
    | assign
    ;

// Test kinds ---------------------------------------------

assertion: ASSERT name ':' test_stub+ ';'                           #assert_test
         ;

test: TEST name domain_names ':' test_stub+ ';'                     #test_basic
//    | name name domain_names ':' test_stub+ ';'                     #macro_basic
    ;

macro: name name domain_names ':' (test_stub | winnow_stub)+  ';'   #macro_basic
     ;

domain_names: name                                                  #get_domain_name
            | name (COMMA? name)+                                   #get_domain_names
            ;

test_stub: BAR predicate ('~~' STRING)?                             #stub_p
         | BAR predicate value ('~~' STRING)?                       #stub_pv
         | BAR predicate (value)+ ('~~' STRING)?                    #stub_many_pv
         | BAR arg_list predicate value ('~~' STRING)?              #stub_assert
         | BAR arg_list predicate ('~~' STRING)?                    #stub_assert_p
//         | BAR arg_list test_logical ('~~' STRING)?                 #stub_assert_logical
         | BAR compiler*                                            #stub_directives
         | BAR test_logical ('~~' STRING)?                          #stub_logical
         | ABAR code                                                #stub_code
         | ABAR value predicate (value)+ ('~~' STRING)?             #stub_side_effect_many
         | ABAR value predicate ('~~' STRING)?                      #stub_side_effect
         | EBAR value? predicate ('~~' STRING)?                     #stub_fail_side_effect
         | EBAR value? predicate (value)+ ('~~' STRING)?            #stub_fail_side_effect_many
         ;

test_logical: OP_NOT? predicate value* (OP_LOGICAL OP_NOT? predicate value*)* #stub_logic
            | OP_NOT? '(' test_logical+ ')'                         #stub_paren
            | test_logical OP_LOGICAL test_logical                  #stub_logic_multi
            ;

// more complex tests ------------

winnow_test: WINNOW name domain_names ARROW name ':' winnow_stub+ ';'    #test_winnow
           ;

groupby_test: GROUPBY name domain_names (ARROW name)? ':' bin_stub+ ';'  #test_groupby
           ;

satisfy_test: SATISFY name domain_names (ARROW name)? ':' test_stub+ ';'  #test_satisfy
            ;

bin_stub: BAR value predicate                                       #groupby_stub
        | BAR value predicate value+                                #groupby_stub_many
        | BAR value predicate value* ':' predicate value*           #groupby_stub_many_many
        | BAR CODESMNT                                              #groupby_code
        | BAR compiler*                                             #groupby_directives
        //        | BAR test_logical                                          #winnow_logical
        ;

winnow_stub: BAR value predicate value* ':' predicate value*        #winnow_stub_many_many
           | BAR compiler*                                          #winnow_stub_directives
           ;

// Domain stuff -------------------------------------------

domain: 'Domain' name name                                         #make_domain
      | 'Domain' name name (value (value*))? (fn_arg (fn_arg*))?   #make_domain_args
      ;

// set parameters -----------------------------------------
compiler: DIRECTIVE dictate (fn_arg+)?                             #set_directive
        | DIRECTIVE                                                #set_single_directive
//        | DIRECTIVE dictate (fn_arg*)?                              #set_directive_args
//        | DIRECTIVE LIST
//        | DIRECTIVE NAME OP_EQ tuple...
        ;

fn_arg: FNARG dictate                                               #make_fn_directive
      | FNARG                                                       #make_fn_flag_directive
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

name: ID                                                            // must be a safe python name
    | LABEL                                                         // valid falcon identifer
    | code
    ;

predicate: name
         | CODESMNT
         | OP_NOT
         | OP_EQ
         | OP_NE
         | UMATH
         | OPERATORS
         ;

//expression: OP_CARDINALITY name                                     #get_card
//          | OP_NOT name                                             #get_not
//          ;

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
     | value_list
     ;

// various operators --------------------------------------

// symbols used -------------
TEST:   'Test';
ASSERT: 'Assert';
WINNOW: 'Winnow'; // | 'Groupby';
GROUPBY: 'Groupby';
SATISFY: 'Satisfy';

LPAREN: '(';
RPAREN: ')';
LBRAC:  '{';
RBRAC:  '}';
COMMA: ',';
SEMICOLON: ';';

ASSIGN: ':=' | '≔';
BAR: '|';
ABAR: '|>';
EBAR: '|!';
COLON: ':';

// others?
//OP_REALS: 'ℝ';
//OP_NATS:  'ℕ';

// NOR?
OP_LOGICAL: OP_AND | OP_OR;
OP_AND:  '∧' | '&&' | 'and';
OP_OR:   '∨' | '||' | 'or';
//OP_NAND: '⊼';
//OP_NOR: '⊽';
//OP_XOR:  '⊻';

OP_NOT:  '￢' | '!';
//OP_CARDINALITY: '#';

// kinds of names used ------
DIRECTIVE: COLON (CHAR | [-_])*;
FNARG:     '-' (CHAR | [-_])*;

//ID: (CHAR | '_')(CHAR | DIGIT | _.])*;
ID: (CHAR | [_#] | [ℝℂℤ])(CHAR | DIGIT | [_.*⨯+\-&≠=￫?] | OPERATORS)*;

OPERATORS: [><≤≥] | '<=' | '>=' | '==' | '±';
OP_EQ:  '=';
OP_NE: '!=' | '/=' | '≠';
ARROW: '->' | '→';

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
