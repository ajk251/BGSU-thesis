// Generated from /media/aaron/Shared2/School/BGSU-thesis/Source/lang/Falcon.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class FalconParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, TEST=2, ASSERT=3, LPAREN=4, RPAREN=5, LBRAC=6, RBRAC=7, ASSIGN=8, 
		BAR=9, OP_LOGICAL=10, OP_AND=11, OP_NAND=12, OP_OR=13, OP_XOR=14, OP_NOT=15, 
		DIRECTIVE=16, FNARG=17, ID=18, CODE=19, OPERATORS=20, OP_EQ=21, LABEL=22, 
		NUMBER=23, STRING=24, CODESMNT=25, UMATH=26, COMMENT=27, MCOMMENT=28, 
		WS=29;
	public static final int
		RULE_program = 0, RULE_block = 1, RULE_namespace = 2, RULE_stmt = 3, RULE_assertion = 4, 
		RULE_test = 5, RULE_test_stub = 6, RULE_compiler = 7, RULE_name = 8, RULE_predicate = 9;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "block", "namespace", "stmt", "assertion", "test", "test_stub", 
			"compiler", "name", "predicate"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "':'", "'Test'", "'Assert'", "'('", "')'", "'{'", "'}'", null, 
			"'|'", null, null, "'\u22BC'", null, "'\u22BB'", null, null, null, null, 
			null, null, "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "TEST", "ASSERT", "LPAREN", "RPAREN", "LBRAC", "RBRAC", "ASSIGN", 
			"BAR", "OP_LOGICAL", "OP_AND", "OP_NAND", "OP_OR", "OP_XOR", "OP_NOT", 
			"DIRECTIVE", "FNARG", "ID", "CODE", "OPERATORS", "OP_EQ", "LABEL", "NUMBER", 
			"STRING", "CODESMNT", "UMATH", "COMMENT", "MCOMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Falcon.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public FalconParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode EOF() { return getToken(FalconParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			setState(26);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TEST:
			case DIRECTIVE:
			case ID:
			case LABEL:
			case CODESMNT:
				enterOuterAlt(_localctx, 1);
				{
				setState(21); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(20);
					block();
					}
					}
					setState(23); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TEST) | (1L << DIRECTIVE) | (1L << ID) | (1L << LABEL) | (1L << CODESMNT))) != 0) );
				}
				break;
			case EOF:
				enterOuterAlt(_localctx, 2);
				{
				setState(25);
				match(EOF);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public List<NamespaceContext> namespace() {
			return getRuleContexts(NamespaceContext.class);
		}
		public NamespaceContext namespace(int i) {
			return getRuleContext(NamespaceContext.class,i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_block);
		try {
			int _alt;
			setState(38);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
			case LABEL:
				enterOuterAlt(_localctx, 1);
				{
				setState(29); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(28);
						namespace();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(31); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			case TEST:
			case DIRECTIVE:
			case CODESMNT:
				enterOuterAlt(_localctx, 2);
				{
				setState(34); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(33);
						stmt();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(36); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NamespaceContext extends ParserRuleContext {
		public NamespaceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_namespace; }
	 
		public NamespaceContext() { }
		public void copyFrom(NamespaceContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class NsContext extends NamespaceContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode LBRAC() { return getToken(FalconParser.LBRAC, 0); }
		public TerminalNode RBRAC() { return getToken(FalconParser.RBRAC, 0); }
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public NsContext(NamespaceContext ctx) { copyFrom(ctx); }
	}

	public final NamespaceContext namespace() throws RecognitionException {
		NamespaceContext _localctx = new NamespaceContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_namespace);
		int _la;
		try {
			_localctx = new NsContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			name();
			setState(41);
			match(LBRAC);
			setState(45);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TEST) | (1L << DIRECTIVE) | (1L << CODESMNT))) != 0)) {
				{
				{
				setState(42);
				stmt();
				}
				}
				setState(47);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(48);
			match(RBRAC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtContext extends ParserRuleContext {
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public CompilerContext compiler() {
			return getRuleContext(CompilerContext.class,0);
		}
		public TerminalNode CODESMNT() { return getToken(FalconParser.CODESMNT, 0); }
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_stmt);
		try {
			setState(53);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TEST:
				enterOuterAlt(_localctx, 1);
				{
				setState(50);
				test();
				}
				break;
			case DIRECTIVE:
				enterOuterAlt(_localctx, 2);
				{
				setState(51);
				compiler();
				}
				break;
			case CODESMNT:
				enterOuterAlt(_localctx, 3);
				{
				setState(52);
				match(CODESMNT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssertionContext extends ParserRuleContext {
		public TerminalNode ASSERT() { return getToken(FalconParser.ASSERT, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public List<Test_stubContext> test_stub() {
			return getRuleContexts(Test_stubContext.class);
		}
		public Test_stubContext test_stub(int i) {
			return getRuleContext(Test_stubContext.class,i);
		}
		public AssertionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assertion; }
	}

	public final AssertionContext assertion() throws RecognitionException {
		AssertionContext _localctx = new AssertionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_assertion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(ASSERT);
			setState(56);
			name();
			setState(57);
			match(T__0);
			setState(59); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(58);
				test_stub();
				}
				}
				setState(61); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==BAR );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TestContext extends ParserRuleContext {
		public TestContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_test; }
	 
		public TestContext() { }
		public void copyFrom(TestContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class Test_basicContext extends TestContext {
		public TerminalNode TEST() { return getToken(FalconParser.TEST, 0); }
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public List<Test_stubContext> test_stub() {
			return getRuleContexts(Test_stubContext.class);
		}
		public Test_stubContext test_stub(int i) {
			return getRuleContext(Test_stubContext.class,i);
		}
		public Test_basicContext(TestContext ctx) { copyFrom(ctx); }
	}

	public final TestContext test() throws RecognitionException {
		TestContext _localctx = new TestContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_test);
		int _la;
		try {
			_localctx = new Test_basicContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(TEST);
			setState(64);
			name();
			setState(65);
			name();
			setState(66);
			match(T__0);
			setState(68); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(67);
				test_stub();
				}
				}
				setState(70); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==BAR );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Test_stubContext extends ParserRuleContext {
		public Test_stubContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_test_stub; }
	 
		public Test_stubContext() { }
		public void copyFrom(Test_stubContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class Stub_pvContext extends Test_stubContext {
		public TerminalNode BAR() { return getToken(FalconParser.BAR, 0); }
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public PredicateContext predicate() {
			return getRuleContext(PredicateContext.class,0);
		}
		public TerminalNode CODE() { return getToken(FalconParser.CODE, 0); }
		public Stub_pvContext(Test_stubContext ctx) { copyFrom(ctx); }
	}

	public final Test_stubContext test_stub() throws RecognitionException {
		Test_stubContext _localctx = new Test_stubContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_test_stub);
		try {
			_localctx = new Stub_pvContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			match(BAR);
			setState(75);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(73);
				name();
				}
				break;
			case 2:
				{
				setState(74);
				predicate();
				}
				break;
			}
			setState(79);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
			case LABEL:
				{
				setState(77);
				name();
				}
				break;
			case CODE:
				{
				setState(78);
				match(CODE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CompilerContext extends ParserRuleContext {
		public CompilerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compiler; }
	 
		public CompilerContext() { }
		public void copyFrom(CompilerContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class Set_directiveContext extends CompilerContext {
		public TerminalNode DIRECTIVE() { return getToken(FalconParser.DIRECTIVE, 0); }
		public TerminalNode NUMBER() { return getToken(FalconParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(FalconParser.STRING, 0); }
		public Set_directiveContext(CompilerContext ctx) { copyFrom(ctx); }
	}

	public final CompilerContext compiler() throws RecognitionException {
		CompilerContext _localctx = new CompilerContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_compiler);
		int _la;
		try {
			_localctx = new Set_directiveContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(DIRECTIVE);
			setState(82);
			_la = _input.LA(1);
			if ( !(_la==NUMBER || _la==STRING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(FalconParser.ID, 0); }
		public TerminalNode LABEL() { return getToken(FalconParser.LABEL, 0); }
		public NameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_name; }
	}

	public final NameContext name() throws RecognitionException {
		NameContext _localctx = new NameContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==LABEL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PredicateContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(FalconParser.ID, 0); }
		public TerminalNode CODESMNT() { return getToken(FalconParser.CODESMNT, 0); }
		public TerminalNode OP_NOT() { return getToken(FalconParser.OP_NOT, 0); }
		public TerminalNode OP_EQ() { return getToken(FalconParser.OP_EQ, 0); }
		public TerminalNode UMATH() { return getToken(FalconParser.UMATH, 0); }
		public TerminalNode OPERATORS() { return getToken(FalconParser.OPERATORS, 0); }
		public PredicateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predicate; }
	}

	public final PredicateContext predicate() throws RecognitionException {
		PredicateContext _localctx = new PredicateContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_predicate);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << OP_NOT) | (1L << ID) | (1L << OPERATORS) | (1L << OP_EQ) | (1L << CODESMNT) | (1L << UMATH))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37[\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3"+
		"\2\6\2\30\n\2\r\2\16\2\31\3\2\5\2\35\n\2\3\3\6\3 \n\3\r\3\16\3!\3\3\6"+
		"\3%\n\3\r\3\16\3&\5\3)\n\3\3\4\3\4\3\4\7\4.\n\4\f\4\16\4\61\13\4\3\4\3"+
		"\4\3\5\3\5\3\5\5\58\n\5\3\6\3\6\3\6\3\6\6\6>\n\6\r\6\16\6?\3\7\3\7\3\7"+
		"\3\7\3\7\6\7G\n\7\r\7\16\7H\3\b\3\b\3\b\5\bN\n\b\3\b\3\b\5\bR\n\b\3\t"+
		"\3\t\3\t\3\n\3\n\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\5\3\2"+
		"\31\32\4\2\24\24\30\30\6\2\21\21\24\24\26\27\33\34\2\\\2\34\3\2\2\2\4"+
		"(\3\2\2\2\6*\3\2\2\2\b\67\3\2\2\2\n9\3\2\2\2\fA\3\2\2\2\16J\3\2\2\2\20"+
		"S\3\2\2\2\22V\3\2\2\2\24X\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\30\31\3"+
		"\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\35\3\2\2\2\33\35\7\2\2\3\34\27\3"+
		"\2\2\2\34\33\3\2\2\2\35\3\3\2\2\2\36 \5\6\4\2\37\36\3\2\2\2 !\3\2\2\2"+
		"!\37\3\2\2\2!\"\3\2\2\2\")\3\2\2\2#%\5\b\5\2$#\3\2\2\2%&\3\2\2\2&$\3\2"+
		"\2\2&\'\3\2\2\2\')\3\2\2\2(\37\3\2\2\2($\3\2\2\2)\5\3\2\2\2*+\5\22\n\2"+
		"+/\7\b\2\2,.\5\b\5\2-,\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\62"+
		"\3\2\2\2\61/\3\2\2\2\62\63\7\t\2\2\63\7\3\2\2\2\648\5\f\7\2\658\5\20\t"+
		"\2\668\7\33\2\2\67\64\3\2\2\2\67\65\3\2\2\2\67\66\3\2\2\28\t\3\2\2\29"+
		":\7\5\2\2:;\5\22\n\2;=\7\3\2\2<>\5\16\b\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2"+
		"\2?@\3\2\2\2@\13\3\2\2\2AB\7\4\2\2BC\5\22\n\2CD\5\22\n\2DF\7\3\2\2EG\5"+
		"\16\b\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\r\3\2\2\2JM\7\13\2\2"+
		"KN\5\22\n\2LN\5\24\13\2MK\3\2\2\2ML\3\2\2\2NQ\3\2\2\2OR\5\22\n\2PR\7\25"+
		"\2\2QO\3\2\2\2QP\3\2\2\2R\17\3\2\2\2ST\7\22\2\2TU\t\2\2\2U\21\3\2\2\2"+
		"VW\t\3\2\2W\23\3\2\2\2XY\t\4\2\2Y\25\3\2\2\2\r\31\34!&(/\67?HMQ";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}