// Generated from /media/aaron/Shared2/School/BGSU-thesis/Source/lang/Falcon.g4 by ANTLR 4.9.1
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
	static { RuntimeMetaData.checkVersion("4.9.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		OP_ASSIGN=1, OP_BAR=2, DIRECTIVE=3, FNARG=4, NAME=5, NUMBER=6, OP_LPAREN=7, 
		OP_RPAREN=8, OP_LBRAC=9, OP_RBRAC=10, OP_REALS=11, OP_NATS=12, OP_LOGICAL=13, 
		OP_AND=14, OP_NAND=15, OP_OR=16, OP_XOR=17, OP_NOT=18, COMMENT=19, MCOMMENT=20, 
		WS=21;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"OP_ASSIGN", "OP_BAR", "DIRECTIVE", "FNARG", "NAME", "NUMBER", "OP_LPAREN", 
			"OP_RPAREN", "OP_LBRAC", "OP_RBRAC", "OP_REALS", "OP_NATS", "OP_LOGICAL", 
			"OP_AND", "OP_NAND", "OP_OR", "OP_XOR", "OP_NOT", "COMMENT", "MCOMMENT", 
			"WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'|'", null, null, null, null, "'('", "')'", "'{'", "'}'", 
			"'\u211D'", "'\u2115'", null, null, "'\u22BC'", null, "'\u22BB'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "OP_ASSIGN", "OP_BAR", "DIRECTIVE", "FNARG", "NAME", "NUMBER", 
			"OP_LPAREN", "OP_RPAREN", "OP_LBRAC", "OP_RBRAC", "OP_REALS", "OP_NATS", 
			"OP_LOGICAL", "OP_AND", "OP_NAND", "OP_OR", "OP_XOR", "OP_NOT", "COMMENT", 
			"MCOMMENT", "WS"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27\u00a3\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\2\5\2\61\n\2\3"+
		"\3\3\3\3\4\3\4\6\4\67\n\4\r\4\16\48\3\5\3\5\6\5=\n\5\r\5\16\5>\3\6\6\6"+
		"B\n\6\r\6\16\6C\3\7\5\7G\n\7\3\7\6\7J\n\7\r\7\16\7K\3\7\5\7O\n\7\3\7\6"+
		"\7R\n\7\r\7\16\7S\3\7\3\7\6\7X\n\7\r\7\16\7Y\5\7\\\n\7\3\b\3\b\3\t\3\t"+
		"\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\5\16n\n\16\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\5\17v\n\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21"+
		"\5\21\177\n\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\7\24\u0089\n\24"+
		"\f\24\16\24\u008c\13\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\7\25\u0096"+
		"\n\25\f\25\16\25\u0099\13\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3"+
		"\26\5S\u008a\u0097\2\27\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f"+
		"\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27\3\2\7\6\2//C\\"+
		"aac|\4\2--//\3\2\62;\4\2##\uffe4\uffe4\4\2\13\f\"\"\2\u00b5\2\3\3\2\2"+
		"\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3"+
		"\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2"+
		"\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2"+
		"\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\3\60\3\2\2\2\5\62\3\2\2\2\7\64"+
		"\3\2\2\2\t:\3\2\2\2\13A\3\2\2\2\r[\3\2\2\2\17]\3\2\2\2\21_\3\2\2\2\23"+
		"a\3\2\2\2\25c\3\2\2\2\27e\3\2\2\2\31g\3\2\2\2\33m\3\2\2\2\35u\3\2\2\2"+
		"\37w\3\2\2\2!~\3\2\2\2#\u0080\3\2\2\2%\u0082\3\2\2\2\'\u0084\3\2\2\2)"+
		"\u0091\3\2\2\2+\u009f\3\2\2\2-.\7<\2\2.\61\7?\2\2/\61\7\u2256\2\2\60-"+
		"\3\2\2\2\60/\3\2\2\2\61\4\3\2\2\2\62\63\7~\2\2\63\6\3\2\2\2\64\66\7<\2"+
		"\2\65\67\t\2\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29\b\3"+
		"\2\2\2:<\7/\2\2;=\t\2\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?\n\3"+
		"\2\2\2@B\t\2\2\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\f\3\2\2\2EG"+
		"\t\3\2\2FE\3\2\2\2FG\3\2\2\2GI\3\2\2\2HJ\t\4\2\2IH\3\2\2\2JK\3\2\2\2K"+
		"I\3\2\2\2KL\3\2\2\2L\\\3\2\2\2MO\t\3\2\2NM\3\2\2\2NO\3\2\2\2OQ\3\2\2\2"+
		"PR\t\4\2\2QP\3\2\2\2RS\3\2\2\2ST\3\2\2\2SQ\3\2\2\2TU\3\2\2\2UW\7\60\2"+
		"\2VX\t\4\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[F\3\2"+
		"\2\2[N\3\2\2\2\\\16\3\2\2\2]^\7*\2\2^\20\3\2\2\2_`\7+\2\2`\22\3\2\2\2"+
		"ab\7}\2\2b\24\3\2\2\2cd\7\177\2\2d\26\3\2\2\2ef\7\u211f\2\2f\30\3\2\2"+
		"\2gh\7\u2117\2\2h\32\3\2\2\2in\5\35\17\2jn\5\37\20\2kn\5!\21\2ln\5#\22"+
		"\2mi\3\2\2\2mj\3\2\2\2mk\3\2\2\2ml\3\2\2\2n\34\3\2\2\2ov\7\u2229\2\2p"+
		"q\7(\2\2qv\7(\2\2rs\7c\2\2st\7p\2\2tv\7f\2\2uo\3\2\2\2up\3\2\2\2ur\3\2"+
		"\2\2v\36\3\2\2\2wx\7\u22be\2\2x \3\2\2\2y\177\7\u222a\2\2z{\7~\2\2{\177"+
		"\7~\2\2|}\7q\2\2}\177\7t\2\2~y\3\2\2\2~z\3\2\2\2~|\3\2\2\2\177\"\3\2\2"+
		"\2\u0080\u0081\7\u22bd\2\2\u0081$\3\2\2\2\u0082\u0083\t\5\2\2\u0083&\3"+
		"\2\2\2\u0084\u0085\7\61\2\2\u0085\u0086\7\61\2\2\u0086\u008a\3\2\2\2\u0087"+
		"\u0089\13\2\2\2\u0088\u0087\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u008b\3"+
		"\2\2\2\u008a\u0088\3\2\2\2\u008b\u008d\3\2\2\2\u008c\u008a\3\2\2\2\u008d"+
		"\u008e\7\f\2\2\u008e\u008f\3\2\2\2\u008f\u0090\b\24\2\2\u0090(\3\2\2\2"+
		"\u0091\u0092\7\61\2\2\u0092\u0093\7,\2\2\u0093\u0097\3\2\2\2\u0094\u0096"+
		"\13\2\2\2\u0095\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0098\3\2\2\2"+
		"\u0097\u0095\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009b"+
		"\7,\2\2\u009b\u009c\7\61\2\2\u009c\u009d\3\2\2\2\u009d\u009e\b\25\2\2"+
		"\u009e*\3\2\2\2\u009f\u00a0\t\6\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\b"+
		"\26\2\2\u00a2,\3\2\2\2\25\2\60\668<>ACFKNSY[mu~\u008a\u0097\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}