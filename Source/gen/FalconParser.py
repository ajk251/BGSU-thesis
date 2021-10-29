# Generated from /media/aaron/Shared2/School/BGSU-thesis/Source/lang/Falcon.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2\16\2\25\3\2\5\2\31\n\2")
        buf.write("\3\3\6\3\34\n\3\r\3\16\3\35\3\3\6\3!\n\3\r\3\16\3\"\5")
        buf.write("\3%\n\3\3\4\3\4\3\4\7\4*\n\4\f\4\16\4-\13\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\5\5\64\n\5\3\6\3\6\3\6\3\6\3\6\6\6;\n\6\r\6")
        buf.write("\16\6<\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\2\2")
        buf.write("\n\2\4\6\b\n\f\16\20\2\4\3\2\24\25\3\2\30\31\2I\2\30\3")
        buf.write("\2\2\2\4$\3\2\2\2\6&\3\2\2\2\b\63\3\2\2\2\n\65\3\2\2\2")
        buf.write("\f>\3\2\2\2\16B\3\2\2\2\20E\3\2\2\2\22\24\5\4\3\2\23\22")
        buf.write("\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26")
        buf.write("\31\3\2\2\2\27\31\7\2\2\3\30\23\3\2\2\2\30\27\3\2\2\2")
        buf.write("\31\3\3\2\2\2\32\34\5\6\4\2\33\32\3\2\2\2\34\35\3\2\2")
        buf.write("\2\35\33\3\2\2\2\35\36\3\2\2\2\36%\3\2\2\2\37!\5\b\5\2")
        buf.write(" \37\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3\2\2")
        buf.write("\2$\33\3\2\2\2$ \3\2\2\2%\5\3\2\2\2&\'\7\24\2\2\'+\7\7")
        buf.write("\2\2(*\5\b\5\2)(\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2")
        buf.write(",.\3\2\2\2-+\3\2\2\2./\7\b\2\2/\7\3\2\2\2\60\64\5\n\6")
        buf.write("\2\61\64\5\16\b\2\62\64\7\23\2\2\63\60\3\2\2\2\63\61\3")
        buf.write("\2\2\2\63\62\3\2\2\2\64\t\3\2\2\2\65\66\7\4\2\2\66\67")
        buf.write("\7\27\2\2\678\7\24\2\28:\7\3\2\29;\5\f\7\2:9\3\2\2\2;")
        buf.write("<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\13\3\2\2\2>?\7\n\2\2?@")
        buf.write("\7\26\2\2@A\7\25\2\2A\r\3\2\2\2BC\7\21\2\2CD\t\2\2\2D")
        buf.write("\17\3\2\2\2EF\7\22\2\2FG\t\3\2\2G\21\3\2\2\2\n\25\30\35")
        buf.write("\"$+\63<")
        return buf.getvalue()


class FalconParser ( Parser ):

    grammarFileName = "Falcon.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'Test'", "'('", "')'", "'{'", 
                     "'}'", "'='", "'|'", "<INVALID>", "<INVALID>", "'\u22BC'", 
                     "<INVALID>", "'\u22BB'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "OP_TEST", "OP_LPAREN", 
                      "OP_RPAREN", "OP_LBRAC", "OP_RBRAC", "OP_EQ", "OP_BAR", 
                      "OP_LOGICAL", "OP_AND", "OP_NAND", "OP_OR", "OP_XOR", 
                      "OP_NOT", "DIRECTIVE", "FNARG", "CODESMNT", "LABEL", 
                      "VALUE", "PREDICATE", "CODE", "NAME", "NUMBER", "STRING", 
                      "COMMENT", "MCOMMENT", "WS" ]

    RULE_program = 0
    RULE_block = 1
    RULE_namespace = 2
    RULE_stmt = 3
    RULE_test = 4
    RULE_test_stub = 5
    RULE_compiler = 6
    RULE_fn_arg = 7

    ruleNames =  [ "program", "block", "namespace", "stmt", "test", "test_stub", 
                   "compiler", "fn_arg" ]

    EOF = Token.EOF
    T__0=1
    OP_TEST=2
    OP_LPAREN=3
    OP_RPAREN=4
    OP_LBRAC=5
    OP_RBRAC=6
    OP_EQ=7
    OP_BAR=8
    OP_LOGICAL=9
    OP_AND=10
    OP_NAND=11
    OP_OR=12
    OP_XOR=13
    OP_NOT=14
    DIRECTIVE=15
    FNARG=16
    CODESMNT=17
    LABEL=18
    VALUE=19
    PREDICATE=20
    CODE=21
    NAME=22
    NUMBER=23
    STRING=24
    COMMENT=25
    MCOMMENT=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FalconParser.BlockContext)
            else:
                return self.getTypedRuleContext(FalconParser.BlockContext,i)


        def EOF(self):
            return self.getToken(FalconParser.EOF, 0)

        def getRuleIndex(self):
            return FalconParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = FalconParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FalconParser.OP_TEST, FalconParser.DIRECTIVE, FalconParser.CODESMNT, FalconParser.LABEL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 16
                    self.block()
                    self.state = 19 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FalconParser.OP_TEST) | (1 << FalconParser.DIRECTIVE) | (1 << FalconParser.CODESMNT) | (1 << FalconParser.LABEL))) != 0)):
                        break

                pass
            elif token in [FalconParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(FalconParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespace(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FalconParser.NamespaceContext)
            else:
                return self.getTypedRuleContext(FalconParser.NamespaceContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FalconParser.StmtContext)
            else:
                return self.getTypedRuleContext(FalconParser.StmtContext,i)


        def getRuleIndex(self):
            return FalconParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = FalconParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FalconParser.LABEL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 24
                        self.namespace()

                    else:
                        raise NoViableAltException(self)
                    self.state = 27 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass
            elif token in [FalconParser.OP_TEST, FalconParser.DIRECTIVE, FalconParser.CODESMNT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 29
                        self.stmt()

                    else:
                        raise NoViableAltException(self)
                    self.state = 32 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamespaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FalconParser.RULE_namespace

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NsContext(NamespaceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FalconParser.NamespaceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LABEL(self):
            return self.getToken(FalconParser.LABEL, 0)
        def OP_LBRAC(self):
            return self.getToken(FalconParser.OP_LBRAC, 0)
        def OP_RBRAC(self):
            return self.getToken(FalconParser.OP_RBRAC, 0)
        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FalconParser.StmtContext)
            else:
                return self.getTypedRuleContext(FalconParser.StmtContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNs" ):
                listener.enterNs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNs" ):
                listener.exitNs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNs" ):
                return visitor.visitNs(self)
            else:
                return visitor.visitChildren(self)



    def namespace(self):

        localctx = FalconParser.NamespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_namespace)
        self._la = 0 # Token type
        try:
            localctx = FalconParser.NsContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(FalconParser.LABEL)
            self.state = 37
            self.match(FalconParser.OP_LBRAC)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FalconParser.OP_TEST) | (1 << FalconParser.DIRECTIVE) | (1 << FalconParser.CODESMNT))) != 0):
                self.state = 38
                self.stmt()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(FalconParser.OP_RBRAC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self):
            return self.getTypedRuleContext(FalconParser.TestContext,0)


        def compiler(self):
            return self.getTypedRuleContext(FalconParser.CompilerContext,0)


        def CODESMNT(self):
            return self.getToken(FalconParser.CODESMNT, 0)

        def getRuleIndex(self):
            return FalconParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = FalconParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FalconParser.OP_TEST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.test()
                pass
            elif token in [FalconParser.DIRECTIVE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.compiler()
                pass
            elif token in [FalconParser.CODESMNT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.match(FalconParser.CODESMNT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FalconParser.RULE_test

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Test_basicContext(TestContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FalconParser.TestContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OP_TEST(self):
            return self.getToken(FalconParser.OP_TEST, 0)
        def CODE(self):
            return self.getToken(FalconParser.CODE, 0)
        def LABEL(self):
            return self.getToken(FalconParser.LABEL, 0)
        def test_stub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FalconParser.Test_stubContext)
            else:
                return self.getTypedRuleContext(FalconParser.Test_stubContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTest_basic" ):
                listener.enterTest_basic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTest_basic" ):
                listener.exitTest_basic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTest_basic" ):
                return visitor.visitTest_basic(self)
            else:
                return visitor.visitChildren(self)



    def test(self):

        localctx = FalconParser.TestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_test)
        self._la = 0 # Token type
        try:
            localctx = FalconParser.Test_basicContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(FalconParser.OP_TEST)
            self.state = 52
            self.match(FalconParser.CODE)
            self.state = 53
            self.match(FalconParser.LABEL)
            self.state = 54
            self.match(FalconParser.T__0)
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.test_stub()
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==FalconParser.OP_BAR):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Test_stubContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FalconParser.RULE_test_stub

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Stub_pvContext(Test_stubContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FalconParser.Test_stubContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OP_BAR(self):
            return self.getToken(FalconParser.OP_BAR, 0)
        def PREDICATE(self):
            return self.getToken(FalconParser.PREDICATE, 0)
        def VALUE(self):
            return self.getToken(FalconParser.VALUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStub_pv" ):
                listener.enterStub_pv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStub_pv" ):
                listener.exitStub_pv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStub_pv" ):
                return visitor.visitStub_pv(self)
            else:
                return visitor.visitChildren(self)



    def test_stub(self):

        localctx = FalconParser.Test_stubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_test_stub)
        try:
            localctx = FalconParser.Stub_pvContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(FalconParser.OP_BAR)
            self.state = 61
            self.match(FalconParser.PREDICATE)
            self.state = 62
            self.match(FalconParser.VALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompilerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FalconParser.RULE_compiler

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Set_directiveContext(CompilerContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FalconParser.CompilerContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DIRECTIVE(self):
            return self.getToken(FalconParser.DIRECTIVE, 0)
        def LABEL(self):
            return self.getToken(FalconParser.LABEL, 0)
        def VALUE(self):
            return self.getToken(FalconParser.VALUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_directive" ):
                listener.enterSet_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_directive" ):
                listener.exitSet_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSet_directive" ):
                return visitor.visitSet_directive(self)
            else:
                return visitor.visitChildren(self)



    def compiler(self):

        localctx = FalconParser.CompilerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_compiler)
        self._la = 0 # Token type
        try:
            localctx = FalconParser.Set_directiveContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(FalconParser.DIRECTIVE)
            self.state = 65
            _la = self._input.LA(1)
            if not(_la==FalconParser.LABEL or _la==FalconParser.VALUE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fn_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FNARG(self):
            return self.getToken(FalconParser.FNARG, 0)

        def NAME(self):
            return self.getToken(FalconParser.NAME, 0)

        def NUMBER(self):
            return self.getToken(FalconParser.NUMBER, 0)

        def getRuleIndex(self):
            return FalconParser.RULE_fn_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFn_arg" ):
                listener.enterFn_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFn_arg" ):
                listener.exitFn_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFn_arg" ):
                return visitor.visitFn_arg(self)
            else:
                return visitor.visitChildren(self)




    def fn_arg(self):

        localctx = FalconParser.Fn_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fn_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(FalconParser.FNARG)
            self.state = 68
            _la = self._input.LA(1)
            if not(_la==FalconParser.NAME or _la==FalconParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





