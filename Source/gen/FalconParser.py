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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\6\2\32\n\2")
        buf.write("\r\2\16\2\33\3\2\5\2\37\n\2\3\3\6\3\"\n\3\r\3\16\3#\3")
        buf.write("\3\6\3\'\n\3\r\3\16\3(\5\3+\n\3\3\4\3\4\3\4\7\4\60\n\4")
        buf.write("\f\4\16\4\63\13\4\3\4\3\4\3\5\3\5\3\5\5\5:\n\5\3\6\3\6")
        buf.write("\3\6\3\6\6\6@\n\6\r\6\16\6A\3\7\3\7\3\7\3\7\3\7\6\7I\n")
        buf.write("\7\r\7\16\7J\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\5\13\\\n\13\3\f\3\f\3\f\3\f")
        buf.write("\5\fb\n\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2\4\4\2")
        buf.write("\24\24\30\31\4\2\24\24\27\27\2j\2\36\3\2\2\2\4*\3\2\2")
        buf.write("\2\6,\3\2\2\2\b9\3\2\2\2\n;\3\2\2\2\fC\3\2\2\2\16L\3\2")
        buf.write("\2\2\20P\3\2\2\2\22S\3\2\2\2\24[\3\2\2\2\26a\3\2\2\2\30")
        buf.write("\32\5\4\3\2\31\30\3\2\2\2\32\33\3\2\2\2\33\31\3\2\2\2")
        buf.write("\33\34\3\2\2\2\34\37\3\2\2\2\35\37\7\2\2\3\36\31\3\2\2")
        buf.write("\2\36\35\3\2\2\2\37\3\3\2\2\2 \"\5\6\4\2! \3\2\2\2\"#")
        buf.write("\3\2\2\2#!\3\2\2\2#$\3\2\2\2$+\3\2\2\2%\'\5\b\5\2&%\3")
        buf.write("\2\2\2\'(\3\2\2\2(&\3\2\2\2()\3\2\2\2)+\3\2\2\2*!\3\2")
        buf.write("\2\2*&\3\2\2\2+\5\3\2\2\2,-\5\22\n\2-\61\7\b\2\2.\60\5")
        buf.write("\b\5\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2")
        buf.write("\2\62\64\3\2\2\2\63\61\3\2\2\2\64\65\7\t\2\2\65\7\3\2")
        buf.write("\2\2\66:\5\f\7\2\67:\5\20\t\28:\7\32\2\29\66\3\2\2\29")
        buf.write("\67\3\2\2\298\3\2\2\2:\t\3\2\2\2;<\7\5\2\2<=\5\22\n\2")
        buf.write("=?\7\3\2\2>@\5\16\b\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB")
        buf.write("\3\2\2\2B\13\3\2\2\2CD\7\4\2\2DE\5\22\n\2EF\5\22\n\2F")
        buf.write("H\7\3\2\2GI\5\16\b\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3")
        buf.write("\2\2\2K\r\3\2\2\2LM\7\13\2\2MN\5\24\13\2NO\5\26\f\2O\17")
        buf.write("\3\2\2\2PQ\7\22\2\2QR\t\2\2\2R\21\3\2\2\2ST\t\3\2\2T\23")
        buf.write("\3\2\2\2U\\\5\22\n\2V\\\7\32\2\2W\\\7\21\2\2X\\\7\26\2")
        buf.write("\2Y\\\7\33\2\2Z\\\7\25\2\2[U\3\2\2\2[V\3\2\2\2[W\3\2\2")
        buf.write("\2[X\3\2\2\2[Y\3\2\2\2[Z\3\2\2\2\\\25\3\2\2\2]b\5\22\n")
        buf.write("\2^b\7\30\2\2_b\7\31\2\2`b\7\32\2\2a]\3\2\2\2a^\3\2\2")
        buf.write("\2a_\3\2\2\2a`\3\2\2\2b\27\3\2\2\2\r\33\36#(*\619AJ[a")
        return buf.getvalue()


class FalconParser ( Parser ):

    grammarFileName = "Falcon.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'Test'", "'Assert'", "'('", "')'", 
                     "'{'", "'}'", "<INVALID>", "'|'", "<INVALID>", "<INVALID>", 
                     "'\u22BC'", "<INVALID>", "'\u22BB'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "TEST", "ASSERT", "LPAREN", 
                      "RPAREN", "LBRAC", "RBRAC", "ASSIGN", "BAR", "OP_LOGICAL", 
                      "OP_AND", "OP_NAND", "OP_OR", "OP_XOR", "OP_NOT", 
                      "DIRECTIVE", "FNARG", "ID", "OPERATORS", "OP_EQ", 
                      "LABEL", "NUMBER", "STRING", "CODESMNT", "UMATH", 
                      "COMMENT", "MCOMMENT", "WS" ]

    RULE_program = 0
    RULE_block = 1
    RULE_namespace = 2
    RULE_stmt = 3
    RULE_assertion = 4
    RULE_test = 5
    RULE_test_stub = 6
    RULE_compiler = 7
    RULE_name = 8
    RULE_predicate = 9
    RULE_value = 10

    ruleNames =  [ "program", "block", "namespace", "stmt", "assertion", 
                   "test", "test_stub", "compiler", "name", "predicate", 
                   "value" ]

    EOF = Token.EOF
    T__0=1
    TEST=2
    ASSERT=3
    LPAREN=4
    RPAREN=5
    LBRAC=6
    RBRAC=7
    ASSIGN=8
    BAR=9
    OP_LOGICAL=10
    OP_AND=11
    OP_NAND=12
    OP_OR=13
    OP_XOR=14
    OP_NOT=15
    DIRECTIVE=16
    FNARG=17
    ID=18
    OPERATORS=19
    OP_EQ=20
    LABEL=21
    NUMBER=22
    STRING=23
    CODESMNT=24
    UMATH=25
    COMMENT=26
    MCOMMENT=27
    WS=28

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
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FalconParser.TEST, FalconParser.DIRECTIVE, FalconParser.ID, FalconParser.LABEL, FalconParser.CODESMNT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 22
                    self.block()
                    self.state = 25 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FalconParser.TEST) | (1 << FalconParser.DIRECTIVE) | (1 << FalconParser.ID) | (1 << FalconParser.LABEL) | (1 << FalconParser.CODESMNT))) != 0)):
                        break

                pass
            elif token in [FalconParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
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
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FalconParser.ID, FalconParser.LABEL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 30
                        self.namespace()

                    else:
                        raise NoViableAltException(self)
                    self.state = 33 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass
            elif token in [FalconParser.TEST, FalconParser.DIRECTIVE, FalconParser.CODESMNT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 35
                        self.stmt()

                    else:
                        raise NoViableAltException(self)
                    self.state = 38 
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

        def name(self):
            return self.getTypedRuleContext(FalconParser.NameContext,0)

        def LBRAC(self):
            return self.getToken(FalconParser.LBRAC, 0)
        def RBRAC(self):
            return self.getToken(FalconParser.RBRAC, 0)
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
            self.state = 42
            self.name()
            self.state = 43
            self.match(FalconParser.LBRAC)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FalconParser.TEST) | (1 << FalconParser.DIRECTIVE) | (1 << FalconParser.CODESMNT))) != 0):
                self.state = 44
                self.stmt()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(FalconParser.RBRAC)
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
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FalconParser.TEST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.test()
                pass
            elif token in [FalconParser.DIRECTIVE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.compiler()
                pass
            elif token in [FalconParser.CODESMNT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
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


    class AssertionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSERT(self):
            return self.getToken(FalconParser.ASSERT, 0)

        def name(self):
            return self.getTypedRuleContext(FalconParser.NameContext,0)


        def test_stub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FalconParser.Test_stubContext)
            else:
                return self.getTypedRuleContext(FalconParser.Test_stubContext,i)


        def getRuleIndex(self):
            return FalconParser.RULE_assertion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssertion" ):
                listener.enterAssertion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssertion" ):
                listener.exitAssertion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssertion" ):
                return visitor.visitAssertion(self)
            else:
                return visitor.visitChildren(self)




    def assertion(self):

        localctx = FalconParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assertion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(FalconParser.ASSERT)
            self.state = 58
            self.name()
            self.state = 59
            self.match(FalconParser.T__0)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.test_stub()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==FalconParser.BAR):
                    break

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

        def TEST(self):
            return self.getToken(FalconParser.TEST, 0)
        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FalconParser.NameContext)
            else:
                return self.getTypedRuleContext(FalconParser.NameContext,i)

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
        self.enterRule(localctx, 10, self.RULE_test)
        self._la = 0 # Token type
        try:
            localctx = FalconParser.Test_basicContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(FalconParser.TEST)
            self.state = 66
            self.name()
            self.state = 67
            self.name()
            self.state = 68
            self.match(FalconParser.T__0)
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.test_stub()
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==FalconParser.BAR):
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

        def BAR(self):
            return self.getToken(FalconParser.BAR, 0)
        def predicate(self):
            return self.getTypedRuleContext(FalconParser.PredicateContext,0)

        def value(self):
            return self.getTypedRuleContext(FalconParser.ValueContext,0)


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
        self.enterRule(localctx, 12, self.RULE_test_stub)
        try:
            localctx = FalconParser.Stub_pvContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(FalconParser.BAR)
            self.state = 75
            self.predicate()
            self.state = 76
            self.value()
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
        def ID(self):
            return self.getToken(FalconParser.ID, 0)
        def NUMBER(self):
            return self.getToken(FalconParser.NUMBER, 0)
        def STRING(self):
            return self.getToken(FalconParser.STRING, 0)

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
        self.enterRule(localctx, 14, self.RULE_compiler)
        self._la = 0 # Token type
        try:
            localctx = FalconParser.Set_directiveContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(FalconParser.DIRECTIVE)
            self.state = 79
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FalconParser.ID) | (1 << FalconParser.NUMBER) | (1 << FalconParser.STRING))) != 0)):
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


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(FalconParser.ID, 0)

        def LABEL(self):
            return self.getToken(FalconParser.LABEL, 0)

        def getRuleIndex(self):
            return FalconParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = FalconParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==FalconParser.ID or _la==FalconParser.LABEL):
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


    class PredicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(FalconParser.NameContext,0)


        def CODESMNT(self):
            return self.getToken(FalconParser.CODESMNT, 0)

        def OP_NOT(self):
            return self.getToken(FalconParser.OP_NOT, 0)

        def OP_EQ(self):
            return self.getToken(FalconParser.OP_EQ, 0)

        def UMATH(self):
            return self.getToken(FalconParser.UMATH, 0)

        def OPERATORS(self):
            return self.getToken(FalconParser.OPERATORS, 0)

        def getRuleIndex(self):
            return FalconParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate" ):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)




    def predicate(self):

        localctx = FalconParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_predicate)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FalconParser.ID, FalconParser.LABEL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.name()
                pass
            elif token in [FalconParser.CODESMNT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(FalconParser.CODESMNT)
                pass
            elif token in [FalconParser.OP_NOT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.match(FalconParser.OP_NOT)
                pass
            elif token in [FalconParser.OP_EQ]:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.match(FalconParser.OP_EQ)
                pass
            elif token in [FalconParser.UMATH]:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.match(FalconParser.UMATH)
                pass
            elif token in [FalconParser.OPERATORS]:
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.match(FalconParser.OPERATORS)
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(FalconParser.NameContext,0)


        def NUMBER(self):
            return self.getToken(FalconParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(FalconParser.STRING, 0)

        def CODESMNT(self):
            return self.getToken(FalconParser.CODESMNT, 0)

        def getRuleIndex(self):
            return FalconParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = FalconParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_value)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FalconParser.ID, FalconParser.LABEL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.name()
                pass
            elif token in [FalconParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.match(FalconParser.NUMBER)
                pass
            elif token in [FalconParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.match(FalconParser.STRING)
                pass
            elif token in [FalconParser.CODESMNT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
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





