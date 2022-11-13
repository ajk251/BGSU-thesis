// Generated from /media/aaron/Shared2/School/BGSU-thesis/Source/lang/Falcon.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class FalconLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "TEST", "ASSERT", "LPAREN", "RPAREN", "LBRAC", "RBRAC", "ASSIGN", 
			"BAR", "OP_LOGICAL", "OP_AND", "OP_NAND", "OP_OR", "OP_XOR", "OP_NOT", 
			"DIRECTIVE", "FNARG", "ID", "CODE", "OPERATORS", "OP_EQ", "LABEL", "NUMBER", 
			"STRING", "CODESMNT", "UMATH", "COMMENT", "MCOMMENT", "WS", "DIGIT", 
			"CHAR"
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


	public FalconLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Falcon.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\37\u011a\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6"+
		"\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\5\t[\n\t\3\n\3\n\3\13\3\13\3\13\3\13"+
		"\5\13c\n\13\3\f\3\f\3\f\3\f\3\f\3\f\5\fk\n\f\3\r\3\r\3\16\3\16\3\16\3"+
		"\16\3\16\5\16t\n\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\7\21}\n\21\f\21"+
		"\16\21\u0080\13\21\3\22\3\22\3\22\7\22\u0085\n\22\f\22\16\22\u0088\13"+
		"\22\3\23\3\23\5\23\u008c\n\23\3\23\3\23\3\23\7\23\u0091\n\23\f\23\16\23"+
		"\u0094\13\23\3\24\3\24\3\24\5\24\u0099\n\24\3\25\3\25\3\25\3\25\3\25\3"+
		"\25\3\25\3\25\5\25\u00a3\n\25\3\26\3\26\3\27\3\27\5\27\u00a9\n\27\3\27"+
		"\3\27\3\27\7\27\u00ae\n\27\f\27\16\27\u00b1\13\27\3\30\5\30\u00b4\n\30"+
		"\3\30\6\30\u00b7\n\30\r\30\16\30\u00b8\3\30\5\30\u00bc\n\30\3\30\6\30"+
		"\u00bf\n\30\r\30\16\30\u00c0\3\30\3\30\7\30\u00c5\n\30\f\30\16\30\u00c8"+
		"\13\30\3\30\5\30\u00cb\n\30\3\30\7\30\u00ce\n\30\f\30\16\30\u00d1\13\30"+
		"\3\30\3\30\6\30\u00d5\n\30\r\30\16\30\u00d6\5\30\u00d9\n\30\3\31\3\31"+
		"\7\31\u00dd\n\31\f\31\16\31\u00e0\13\31\3\31\3\31\3\31\7\31\u00e5\n\31"+
		"\f\31\16\31\u00e8\13\31\3\31\5\31\u00eb\n\31\3\32\3\32\7\32\u00ef\n\32"+
		"\f\32\16\32\u00f2\13\32\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\7\34\u00fc"+
		"\n\34\f\34\16\34\u00ff\13\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\7"+
		"\35\u0109\n\35\f\35\16\35\u010c\13\35\3\35\3\35\3\35\3\35\3\35\3\36\3"+
		"\36\3\36\3\36\3\37\3\37\3 \3 \7\u00de\u00e6\u00f0\u00fd\u010a\2!\3\3\5"+
		"\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21"+
		"!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37=\2?"+
		"\2\3\2\13\4\2##\uffe4\uffe4\4\2//aa\4\2\60\60aa\5\2>>@@\u2266\u2267\b"+
		"\2((--//AAaa\u0080\u0080\4\2--//\3\2\62;\5\2\13\f\17\17\"\"\4\2C\\c|\2"+
		"\u0141\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2"+
		"\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3"+
		"\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2"+
		"\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2"+
		"/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2"+
		"\2\2;\3\2\2\2\3A\3\2\2\2\5C\3\2\2\2\7H\3\2\2\2\tO\3\2\2\2\13Q\3\2\2\2"+
		"\rS\3\2\2\2\17U\3\2\2\2\21Z\3\2\2\2\23\\\3\2\2\2\25b\3\2\2\2\27j\3\2\2"+
		"\2\31l\3\2\2\2\33s\3\2\2\2\35u\3\2\2\2\37w\3\2\2\2!y\3\2\2\2#\u0081\3"+
		"\2\2\2%\u008b\3\2\2\2\'\u0098\3\2\2\2)\u00a2\3\2\2\2+\u00a4\3\2\2\2-\u00a8"+
		"\3\2\2\2/\u00d8\3\2\2\2\61\u00ea\3\2\2\2\63\u00ec\3\2\2\2\65\u00f5\3\2"+
		"\2\2\67\u00f7\3\2\2\29\u0104\3\2\2\2;\u0112\3\2\2\2=\u0116\3\2\2\2?\u0118"+
		"\3\2\2\2AB\7<\2\2B\4\3\2\2\2CD\7V\2\2DE\7g\2\2EF\7u\2\2FG\7v\2\2G\6\3"+
		"\2\2\2HI\7C\2\2IJ\7u\2\2JK\7u\2\2KL\7g\2\2LM\7t\2\2MN\7v\2\2N\b\3\2\2"+
		"\2OP\7*\2\2P\n\3\2\2\2QR\7+\2\2R\f\3\2\2\2ST\7}\2\2T\16\3\2\2\2UV\7\177"+
		"\2\2V\20\3\2\2\2WX\7<\2\2X[\7?\2\2Y[\7\u2256\2\2ZW\3\2\2\2ZY\3\2\2\2["+
		"\22\3\2\2\2\\]\7~\2\2]\24\3\2\2\2^c\5\27\f\2_c\5\31\r\2`c\5\33\16\2ac"+
		"\5\35\17\2b^\3\2\2\2b_\3\2\2\2b`\3\2\2\2ba\3\2\2\2c\26\3\2\2\2dk\7\u2229"+
		"\2\2ef\7(\2\2fk\7(\2\2gh\7c\2\2hi\7p\2\2ik\7f\2\2jd\3\2\2\2je\3\2\2\2"+
		"jg\3\2\2\2k\30\3\2\2\2lm\7\u22be\2\2m\32\3\2\2\2nt\7\u222a\2\2op\7~\2"+
		"\2pt\7~\2\2qr\7q\2\2rt\7t\2\2sn\3\2\2\2so\3\2\2\2sq\3\2\2\2t\34\3\2\2"+
		"\2uv\7\u22bd\2\2v\36\3\2\2\2wx\t\2\2\2x \3\2\2\2y~\7<\2\2z}\5? \2{}\t"+
		"\3\2\2|z\3\2\2\2|{\3\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\""+
		"\3\2\2\2\u0080~\3\2\2\2\u0081\u0086\7/\2\2\u0082\u0085\5? \2\u0083\u0085"+
		"\t\3\2\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085\u0088\3\2\2\2\u0086"+
		"\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087$\3\2\2\2\u0088\u0086\3\2\2\2"+
		"\u0089\u008c\5? \2\u008a\u008c\7a\2\2\u008b\u0089\3\2\2\2\u008b\u008a"+
		"\3\2\2\2\u008c\u0092\3\2\2\2\u008d\u0091\5? \2\u008e\u0091\5=\37\2\u008f"+
		"\u0091\t\4\2\2\u0090\u008d\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u008f\3\2"+
		"\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093"+
		"&\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u0099\5\63\32\2\u0096\u0099\5\61\31"+
		"\2\u0097\u0099\5/\30\2\u0098\u0095\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0097"+
		"\3\2\2\2\u0099(\3\2\2\2\u009a\u00a3\t\5\2\2\u009b\u009c\7>\2\2\u009c\u00a3"+
		"\7?\2\2\u009d\u009e\7@\2\2\u009e\u00a3\7?\2\2\u009f\u00a0\7?\2\2\u00a0"+
		"\u00a3\7?\2\2\u00a1\u00a3\7\u00b3\2\2\u00a2\u009a\3\2\2\2\u00a2\u009b"+
		"\3\2\2\2\u00a2\u009d\3\2\2\2\u00a2\u009f\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3"+
		"*\3\2\2\2\u00a4\u00a5\7?\2\2\u00a5,\3\2\2\2\u00a6\u00a9\5? \2\u00a7\u00a9"+
		"\7a\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00af\3\2\2\2\u00aa"+
		"\u00ae\5? \2\u00ab\u00ae\5=\37\2\u00ac\u00ae\t\6\2\2\u00ad\u00aa\3\2\2"+
		"\2\u00ad\u00ab\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad"+
		"\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0.\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2"+
		"\u00b4\t\7\2\2\u00b3\u00b2\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b6\3\2"+
		"\2\2\u00b5\u00b7\5=\37\2\u00b6\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8"+
		"\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00d9\3\2\2\2\u00ba\u00bc\t\7"+
		"\2\2\u00bb\u00ba\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00be\3\2\2\2\u00bd"+
		"\u00bf\5=\37\2\u00be\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00be\3\2"+
		"\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c6\7\60\2\2\u00c3"+
		"\u00c5\t\b\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2"+
		"\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00d9\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9"+
		"\u00cb\t\7\2\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cf\3\2"+
		"\2\2\u00cc\u00ce\5=\37\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf"+
		"\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00cf\3\2"+
		"\2\2\u00d2\u00d4\7\60\2\2\u00d3\u00d5\t\b\2\2\u00d4\u00d3\3\2\2\2\u00d5"+
		"\u00d6\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d9\3\2"+
		"\2\2\u00d8\u00b3\3\2\2\2\u00d8\u00bb\3\2\2\2\u00d8\u00ca\3\2\2\2\u00d9"+
		"\60\3\2\2\2\u00da\u00de\3\2\2\2\u00db\u00dd\13\2\2\2\u00dc\u00db\3\2\2"+
		"\2\u00dd\u00e0\3\2\2\2\u00de\u00df\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e1"+
		"\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00eb\3\2\2\2\u00e2\u00e6\7)\2\2\u00e3"+
		"\u00e5\13\2\2\2\u00e4\u00e3\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6\u00e7\3"+
		"\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e9\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9"+
		"\u00eb\7)\2\2\u00ea\u00da\3\2\2\2\u00ea\u00e2\3\2\2\2\u00eb\62\3\2\2\2"+
		"\u00ec\u00f0\7b\2\2\u00ed\u00ef\13\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\u00f2"+
		"\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f3\3\2\2\2\u00f2"+
		"\u00f0\3\2\2\2\u00f3\u00f4\7b\2\2\u00f4\64\3\2\2\2\u00f5\u00f6\4\u2202"+
		"\u2301\2\u00f6\66\3\2\2\2\u00f7\u00f8\7\61\2\2\u00f8\u00f9\7\61\2\2\u00f9"+
		"\u00fd\3\2\2\2\u00fa\u00fc\13\2\2\2\u00fb\u00fa\3\2\2\2\u00fc\u00ff\3"+
		"\2\2\2\u00fd\u00fe\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u0100\3\2\2\2\u00ff"+
		"\u00fd\3\2\2\2\u0100\u0101\7\f\2\2\u0101\u0102\3\2\2\2\u0102\u0103\b\34"+
		"\2\2\u01038\3\2\2\2\u0104\u0105\7\61\2\2\u0105\u0106\7,\2\2\u0106\u010a"+
		"\3\2\2\2\u0107\u0109\13\2\2\2\u0108\u0107\3\2\2\2\u0109\u010c\3\2\2\2"+
		"\u010a\u010b\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010d\3\2\2\2\u010c\u010a"+
		"\3\2\2\2\u010d\u010e\7,\2\2\u010e\u010f\7\61\2\2\u010f\u0110\3\2\2\2\u0110"+
		"\u0111\b\35\2\2\u0111:\3\2\2\2\u0112\u0113\t\t\2\2\u0113\u0114\3\2\2\2"+
		"\u0114\u0115\b\36\2\2\u0115<\3\2\2\2\u0116\u0117\t\b\2\2\u0117>\3\2\2"+
		"\2\u0118\u0119\t\n\2\2\u0119@\3\2\2\2\"\2Zbjs|~\u0084\u0086\u008b\u0090"+
		"\u0092\u0098\u00a2\u00a8\u00ad\u00af\u00b3\u00b8\u00bb\u00c0\u00c6\u00ca"+
		"\u00cf\u00d6\u00d8\u00de\u00e6\u00ea\u00f0\u00fd\u010a\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}