// Generated from d:/source/Universidad/TFG/gramatica.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class gramaticaParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, OpComp=24, 
		OR=25, AND=26, NOT=27, OpIgual=28, OpAsign=29, COMMENT_SIMPLE=30, COMMENT_MULTI=31, 
		BOOLEAN=32, STRING=33, NUMBER=34, INDIVIDUO=35, VARIABLE=36, WS=37;
	public static final int
		RULE_programa = 0, RULE_imports = 1, RULE_elemento = 2, RULE_declaracion = 3, 
		RULE_declCategoria = 4, RULE_listaAtributos = 5, RULE_atributo = 6, RULE_tipoBasico = 7, 
		RULE_declProposicion = 8, RULE_bloquePropiedades = 9, RULE_listaIdentificadores = 10, 
		RULE_listaPropiedades = 11, RULE_accion = 12, RULE_listaParams = 13, RULE_listaCondiciones = 14, 
		RULE_condicion = 15, RULE_condicionFuncion = 16, RULE_asignacionVariable = 17, 
		RULE_predicado = 18, RULE_listaArgsPredicado = 19, RULE_paramPredicado = 20, 
		RULE_comparacion = 21, RULE_operando = 22, RULE_funcion = 23, RULE_listaArgsFuncion = 24, 
		RULE_paramFuncion = 25, RULE_operacionLogica = 26, RULE_listaConsecuencias = 27, 
		RULE_consecuencia = 28, RULE_asignacion = 29, RULE_operandoIzq = 30, RULE_operandoDrc = 31, 
		RULE_borrado = 32, RULE_inicializacion = 33, RULE_bloqueValores = 34, 
		RULE_listaParejasValor = 35, RULE_parejaValor = 36, RULE_valor = 37, RULE_argLit = 38, 
		RULE_ejecucion = 39, RULE_listaArgLit = 40, RULE_comentarioSimple = 41, 
		RULE_comentarioMultilineo = 42, RULE_idName = 43;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "imports", "elemento", "declaracion", "declCategoria", "listaAtributos", 
			"atributo", "tipoBasico", "declProposicion", "bloquePropiedades", "listaIdentificadores", 
			"listaPropiedades", "accion", "listaParams", "listaCondiciones", "condicion", 
			"condicionFuncion", "asignacionVariable", "predicado", "listaArgsPredicado", 
			"paramPredicado", "comparacion", "operando", "funcion", "listaArgsFuncion", 
			"paramFuncion", "operacionLogica", "listaConsecuencias", "consecuencia", 
			"asignacion", "operandoIzq", "operandoDrc", "borrado", "inicializacion", 
			"bloqueValores", "listaParejasValor", "parejaValor", "valor", "argLit", 
			"ejecucion", "listaArgLit", "comentarioSimple", "comentarioMultilineo", 
			"idName"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'from'", "'import'", "';'", "'Categoria'", "'('", "')'", "','", 
			"':'", "'int'", "'str'", "'bool'", "'Prop'", "'{'", "'}'", "'Accion'", 
			"'Condiciones:'", "'Consecuencias:'", "'.'", "'_'", "'*'", "'DEL'", "'add'", 
			"'Run'", null, "'OR'", "'AND'", "'NOT'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"OpComp", "OR", "AND", "NOT", "OpIgual", "OpAsign", "COMMENT_SIMPLE", 
			"COMMENT_MULTI", "BOOLEAN", "STRING", "NUMBER", "INDIVIDUO", "VARIABLE", 
			"WS"
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
	public String getGrammarFileName() { return "gramatica.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public gramaticaParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(gramaticaParser.EOF, 0); }
		public List<ImportsContext> imports() {
			return getRuleContexts(ImportsContext.class);
		}
		public ImportsContext imports(int i) {
			return getRuleContext(ImportsContext.class,i);
		}
		public List<ElementoContext> elemento() {
			return getRuleContexts(ElementoContext.class);
		}
		public ElementoContext elemento(int i) {
			return getRuleContext(ElementoContext.class,i);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterPrograma(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitPrograma(this);
		}
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0) {
				{
				{
				setState(88);
				imports();
				}
				}
				setState(93);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3233845264L) != 0)) {
				{
				{
				setState(94);
				elemento();
				}
				}
				setState(99);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(100);
			match(EOF);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ImportsContext extends ParserRuleContext {
		public List<IdNameContext> idName() {
			return getRuleContexts(IdNameContext.class);
		}
		public IdNameContext idName(int i) {
			return getRuleContext(IdNameContext.class,i);
		}
		public ImportsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_imports; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterImports(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitImports(this);
		}
	}

	public final ImportsContext imports() throws RecognitionException {
		ImportsContext _localctx = new ImportsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_imports);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(T__0);
			setState(103);
			idName();
			setState(104);
			match(T__1);
			setState(105);
			idName();
			setState(106);
			match(T__2);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ElementoContext extends ParserRuleContext {
		public DeclaracionContext declaracion() {
			return getRuleContext(DeclaracionContext.class,0);
		}
		public AccionContext accion() {
			return getRuleContext(AccionContext.class,0);
		}
		public InicializacionContext inicializacion() {
			return getRuleContext(InicializacionContext.class,0);
		}
		public EjecucionContext ejecucion() {
			return getRuleContext(EjecucionContext.class,0);
		}
		public ComentarioSimpleContext comentarioSimple() {
			return getRuleContext(ComentarioSimpleContext.class,0);
		}
		public ComentarioMultilineoContext comentarioMultilineo() {
			return getRuleContext(ComentarioMultilineoContext.class,0);
		}
		public ElementoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elemento; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterElemento(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitElemento(this);
		}
	}

	public final ElementoContext elemento() throws RecognitionException {
		ElementoContext _localctx = new ElementoContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_elemento);
		try {
			setState(114);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
			case T__11:
				enterOuterAlt(_localctx, 1);
				{
				setState(108);
				declaracion();
				}
				break;
			case T__14:
				enterOuterAlt(_localctx, 2);
				{
				setState(109);
				accion();
				}
				break;
			case T__21:
				enterOuterAlt(_localctx, 3);
				{
				setState(110);
				inicializacion();
				}
				break;
			case T__22:
				enterOuterAlt(_localctx, 4);
				{
				setState(111);
				ejecucion();
				}
				break;
			case COMMENT_SIMPLE:
				enterOuterAlt(_localctx, 5);
				{
				setState(112);
				comentarioSimple();
				}
				break;
			case COMMENT_MULTI:
				enterOuterAlt(_localctx, 6);
				{
				setState(113);
				comentarioMultilineo();
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

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionContext extends ParserRuleContext {
		public DeclCategoriaContext declCategoria() {
			return getRuleContext(DeclCategoriaContext.class,0);
		}
		public ComentarioSimpleContext comentarioSimple() {
			return getRuleContext(ComentarioSimpleContext.class,0);
		}
		public DeclProposicionContext declProposicion() {
			return getRuleContext(DeclProposicionContext.class,0);
		}
		public DeclaracionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterDeclaracion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitDeclaracion(this);
		}
	}

	public final DeclaracionContext declaracion() throws RecognitionException {
		DeclaracionContext _localctx = new DeclaracionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_declaracion);
		try {
			setState(126);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(116);
				declCategoria();
				setState(117);
				match(T__2);
				setState(119);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
				case 1:
					{
					setState(118);
					comentarioSimple();
					}
					break;
				}
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 2);
				{
				setState(121);
				declProposicion();
				setState(122);
				match(T__2);
				setState(124);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
				case 1:
					{
					setState(123);
					comentarioSimple();
					}
					break;
				}
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

	@SuppressWarnings("CheckReturnValue")
	public static class DeclCategoriaContext extends ParserRuleContext {
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public ListaAtributosContext listaAtributos() {
			return getRuleContext(ListaAtributosContext.class,0);
		}
		public DeclCategoriaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declCategoria; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterDeclCategoria(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitDeclCategoria(this);
		}
	}

	public final DeclCategoriaContext declCategoria() throws RecognitionException {
		DeclCategoriaContext _localctx = new DeclCategoriaContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_declCategoria);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(T__3);
			setState(129);
			idName();
			setState(130);
			match(T__4);
			setState(132);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INDIVIDUO || _la==VARIABLE) {
				{
				setState(131);
				listaAtributos();
				}
			}

			setState(134);
			match(T__5);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ListaAtributosContext extends ParserRuleContext {
		public List<AtributoContext> atributo() {
			return getRuleContexts(AtributoContext.class);
		}
		public AtributoContext atributo(int i) {
			return getRuleContext(AtributoContext.class,i);
		}
		public ListaAtributosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaAtributos; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterListaAtributos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitListaAtributos(this);
		}
	}

	public final ListaAtributosContext listaAtributos() throws RecognitionException {
		ListaAtributosContext _localctx = new ListaAtributosContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_listaAtributos);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			atributo();
			setState(141);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(137);
				match(T__6);
				setState(138);
				atributo();
				}
				}
				setState(143);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class AtributoContext extends ParserRuleContext {
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public TipoBasicoContext tipoBasico() {
			return getRuleContext(TipoBasicoContext.class,0);
		}
		public AtributoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atributo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterAtributo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitAtributo(this);
		}
	}

	public final AtributoContext atributo() throws RecognitionException {
		AtributoContext _localctx = new AtributoContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_atributo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			idName();
			setState(145);
			match(T__7);
			setState(146);
			tipoBasico();
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

	@SuppressWarnings("CheckReturnValue")
	public static class TipoBasicoContext extends ParserRuleContext {
		public TipoBasicoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipoBasico; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterTipoBasico(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitTipoBasico(this);
		}
	}

	public final TipoBasicoContext tipoBasico() throws RecognitionException {
		TipoBasicoContext _localctx = new TipoBasicoContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_tipoBasico);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3584L) != 0)) ) {
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

	@SuppressWarnings("CheckReturnValue")
	public static class DeclProposicionContext extends ParserRuleContext {
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public ListaIdentificadoresContext listaIdentificadores() {
			return getRuleContext(ListaIdentificadoresContext.class,0);
		}
		public BloquePropiedadesContext bloquePropiedades() {
			return getRuleContext(BloquePropiedadesContext.class,0);
		}
		public DeclProposicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declProposicion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterDeclProposicion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitDeclProposicion(this);
		}
	}

	public final DeclProposicionContext declProposicion() throws RecognitionException {
		DeclProposicionContext _localctx = new DeclProposicionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_declProposicion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(T__11);
			setState(151);
			idName();
			setState(152);
			match(T__4);
			setState(154);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INDIVIDUO || _la==VARIABLE) {
				{
				setState(153);
				listaIdentificadores();
				}
			}

			setState(156);
			match(T__5);
			setState(158);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(157);
				bloquePropiedades();
				}
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

	@SuppressWarnings("CheckReturnValue")
	public static class BloquePropiedadesContext extends ParserRuleContext {
		public ListaPropiedadesContext listaPropiedades() {
			return getRuleContext(ListaPropiedadesContext.class,0);
		}
		public BloquePropiedadesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloquePropiedades; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterBloquePropiedades(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitBloquePropiedades(this);
		}
	}

	public final BloquePropiedadesContext bloquePropiedades() throws RecognitionException {
		BloquePropiedadesContext _localctx = new BloquePropiedadesContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_bloquePropiedades);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			match(T__12);
			setState(162);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INDIVIDUO || _la==VARIABLE) {
				{
				setState(161);
				listaPropiedades();
				}
			}

			setState(164);
			match(T__13);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ListaIdentificadoresContext extends ParserRuleContext {
		public List<IdNameContext> idName() {
			return getRuleContexts(IdNameContext.class);
		}
		public IdNameContext idName(int i) {
			return getRuleContext(IdNameContext.class,i);
		}
		public ListaIdentificadoresContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaIdentificadores; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterListaIdentificadores(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitListaIdentificadores(this);
		}
	}

	public final ListaIdentificadoresContext listaIdentificadores() throws RecognitionException {
		ListaIdentificadoresContext _localctx = new ListaIdentificadoresContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_listaIdentificadores);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			idName();
			setState(171);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(167);
				match(T__6);
				setState(168);
				idName();
				}
				}
				setState(173);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ListaPropiedadesContext extends ParserRuleContext {
		public List<IdNameContext> idName() {
			return getRuleContexts(IdNameContext.class);
		}
		public IdNameContext idName(int i) {
			return getRuleContext(IdNameContext.class,i);
		}
		public ListaPropiedadesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaPropiedades; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterListaPropiedades(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitListaPropiedades(this);
		}
	}

	public final ListaPropiedadesContext listaPropiedades() throws RecognitionException {
		ListaPropiedadesContext _localctx = new ListaPropiedadesContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_listaPropiedades);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			idName();
			setState(179);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(175);
				match(T__6);
				setState(176);
				idName();
				}
				}
				setState(181);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class AccionContext extends ParserRuleContext {
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public ListaCondicionesContext listaCondiciones() {
			return getRuleContext(ListaCondicionesContext.class,0);
		}
		public ListaConsecuenciasContext listaConsecuencias() {
			return getRuleContext(ListaConsecuenciasContext.class,0);
		}
		public ListaParamsContext listaParams() {
			return getRuleContext(ListaParamsContext.class,0);
		}
		public ComentarioMultilineoContext comentarioMultilineo() {
			return getRuleContext(ComentarioMultilineoContext.class,0);
		}
		public AccionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_accion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterAccion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitAccion(this);
		}
	}

	public final AccionContext accion() throws RecognitionException {
		AccionContext _localctx = new AccionContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_accion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(T__14);
			setState(183);
			idName();
			setState(184);
			match(T__4);
			setState(186);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INDIVIDUO || _la==VARIABLE) {
				{
				setState(185);
				listaParams();
				}
			}

			setState(188);
			match(T__5);
			setState(189);
			match(T__7);
			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMENT_MULTI) {
				{
				setState(190);
				comentarioMultilineo();
				}
			}

			setState(193);
			match(T__15);
			setState(194);
			listaCondiciones();
			setState(195);
			match(T__16);
			setState(196);
			listaConsecuencias();
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

	@SuppressWarnings("CheckReturnValue")
	public static class ListaParamsContext extends ParserRuleContext {
		public List<IdNameContext> idName() {
			return getRuleContexts(IdNameContext.class);
		}
		public IdNameContext idName(int i) {
			return getRuleContext(IdNameContext.class,i);
		}
		public ListaParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaParams; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterListaParams(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitListaParams(this);
		}
	}

	public final ListaParamsContext listaParams() throws RecognitionException {
		ListaParamsContext _localctx = new ListaParamsContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_listaParams);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			idName();
			setState(203);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(199);
				match(T__6);
				setState(200);
				idName();
				}
				}
				setState(205);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ListaCondicionesContext extends ParserRuleContext {
		public List<CondicionContext> condicion() {
			return getRuleContexts(CondicionContext.class);
		}
		public CondicionContext condicion(int i) {
			return getRuleContext(CondicionContext.class,i);
		}
		public List<ComentarioSimpleContext> comentarioSimple() {
			return getRuleContexts(ComentarioSimpleContext.class);
		}
		public ComentarioSimpleContext comentarioSimple(int i) {
			return getRuleContext(ComentarioSimpleContext.class,i);
		}
		public ListaCondicionesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaCondiciones; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterListaCondiciones(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitListaCondiciones(this);
		}
	}

	public final ListaCondicionesContext listaCondiciones() throws RecognitionException {
		ListaCondicionesContext _localctx = new ListaCondicionesContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_listaCondiciones);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 133378867200L) != 0)) {
				{
				{
				setState(206);
				condicion();
				setState(207);
				match(T__2);
				setState(209);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMENT_SIMPLE) {
					{
					setState(208);
					comentarioSimple();
					}
				}

				}
				}
				setState(215);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionContext extends ParserRuleContext {
		public PredicadoContext predicado() {
			return getRuleContext(PredicadoContext.class,0);
		}
		public ComparacionContext comparacion() {
			return getRuleContext(ComparacionContext.class,0);
		}
		public OperacionLogicaContext operacionLogica() {
			return getRuleContext(OperacionLogicaContext.class,0);
		}
		public AsignacionVariableContext asignacionVariable() {
			return getRuleContext(AsignacionVariableContext.class,0);
		}
		public CondicionFuncionContext condicionFuncion() {
			return getRuleContext(CondicionFuncionContext.class,0);
		}
		public CondicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterCondicion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitCondicion(this);
		}
	}

	public final CondicionContext condicion() throws RecognitionException {
		CondicionContext _localctx = new CondicionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_condicion);
		try {
			setState(221);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(216);
				predicado();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(217);
				comparacion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(218);
				operacionLogica();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(219);
				asignacionVariable();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(220);
				condicionFuncion();
				}
				break;
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

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionFuncionContext extends ParserRuleContext {
		public FuncionContext funcion() {
			return getRuleContext(FuncionContext.class,0);
		}
		public CondicionFuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicionFuncion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterCondicionFuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitCondicionFuncion(this);
		}
	}

	public final CondicionFuncionContext condicionFuncion() throws RecognitionException {
		CondicionFuncionContext _localctx = new CondicionFuncionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_condicionFuncion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			funcion();
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

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionVariableContext extends ParserRuleContext {
		public TerminalNode VARIABLE() { return getToken(gramaticaParser.VARIABLE, 0); }
		public TerminalNode OpIgual() { return getToken(gramaticaParser.OpIgual, 0); }
		public PredicadoContext predicado() {
			return getRuleContext(PredicadoContext.class,0);
		}
		public FuncionContext funcion() {
			return getRuleContext(FuncionContext.class,0);
		}
		public AsignacionVariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacionVariable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterAsignacionVariable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitAsignacionVariable(this);
		}
	}

	public final AsignacionVariableContext asignacionVariable() throws RecognitionException {
		AsignacionVariableContext _localctx = new AsignacionVariableContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_asignacionVariable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			match(VARIABLE);
			setState(226);
			match(OpIgual);
			setState(229);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				{
				setState(227);
				predicado();
				}
				break;
			case 2:
				{
				setState(228);
				funcion();
				}
				break;
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

	@SuppressWarnings("CheckReturnValue")
	public static class PredicadoContext extends ParserRuleContext {
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public ListaArgsPredicadoContext listaArgsPredicado() {
			return getRuleContext(ListaArgsPredicadoContext.class,0);
		}
		public PredicadoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predicado; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterPredicado(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitPredicado(this);
		}
	}

	public final PredicadoContext predicado() throws RecognitionException {
		PredicadoContext _localctx = new PredicadoContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_predicado);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
			idName();
			setState(232);
			match(T__4);
			setState(233);
			listaArgsPredicado();
			setState(234);
			match(T__5);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ListaArgsPredicadoContext extends ParserRuleContext {
		public List<ParamPredicadoContext> paramPredicado() {
			return getRuleContexts(ParamPredicadoContext.class);
		}
		public ParamPredicadoContext paramPredicado(int i) {
			return getRuleContext(ParamPredicadoContext.class,i);
		}
		public ListaArgsPredicadoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaArgsPredicado; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterListaArgsPredicado(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitListaArgsPredicado(this);
		}
	}

	public final ListaArgsPredicadoContext listaArgsPredicado() throws RecognitionException {
		ListaArgsPredicadoContext _localctx = new ListaArgsPredicadoContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_listaArgsPredicado);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(236);
			paramPredicado();
			setState(241);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(237);
				match(T__6);
				setState(238);
				paramPredicado();
				}
				}
				setState(243);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ParamPredicadoContext extends ParserRuleContext {
		public TerminalNode INDIVIDUO() { return getToken(gramaticaParser.INDIVIDUO, 0); }
		public FuncionContext funcion() {
			return getRuleContext(FuncionContext.class,0);
		}
		public TerminalNode VARIABLE() { return getToken(gramaticaParser.VARIABLE, 0); }
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public TerminalNode STRING() { return getToken(gramaticaParser.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(gramaticaParser.NUMBER, 0); }
		public TerminalNode BOOLEAN() { return getToken(gramaticaParser.BOOLEAN, 0); }
		public ParamPredicadoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramPredicado; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterParamPredicado(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitParamPredicado(this);
		}
	}

	public final ParamPredicadoContext paramPredicado() throws RecognitionException {
		ParamPredicadoContext _localctx = new ParamPredicadoContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_paramPredicado);
		try {
			setState(254);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(244);
				match(INDIVIDUO);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(245);
				funcion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(246);
				match(VARIABLE);
				setState(247);
				match(T__17);
				setState(248);
				idName();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(249);
				match(VARIABLE);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(250);
				match(STRING);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(251);
				match(NUMBER);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(252);
				match(BOOLEAN);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(253);
				match(T__18);
				}
				break;
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

	@SuppressWarnings("CheckReturnValue")
	public static class ComparacionContext extends ParserRuleContext {
		public List<OperandoContext> operando() {
			return getRuleContexts(OperandoContext.class);
		}
		public OperandoContext operando(int i) {
			return getRuleContext(OperandoContext.class,i);
		}
		public TerminalNode OpComp() { return getToken(gramaticaParser.OpComp, 0); }
		public ComparacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterComparacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitComparacion(this);
		}
	}

	public final ComparacionContext comparacion() throws RecognitionException {
		ComparacionContext _localctx = new ComparacionContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_comparacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(256);
			operando();
			setState(257);
			match(OpComp);
			setState(258);
			operando();
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

	@SuppressWarnings("CheckReturnValue")
	public static class OperandoContext extends ParserRuleContext {
		public FuncionContext funcion() {
			return getRuleContext(FuncionContext.class,0);
		}
		public TerminalNode VARIABLE() { return getToken(gramaticaParser.VARIABLE, 0); }
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public TerminalNode INDIVIDUO() { return getToken(gramaticaParser.INDIVIDUO, 0); }
		public TerminalNode NUMBER() { return getToken(gramaticaParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(gramaticaParser.STRING, 0); }
		public TerminalNode BOOLEAN() { return getToken(gramaticaParser.BOOLEAN, 0); }
		public OperandoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operando; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterOperando(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitOperando(this);
		}
	}

	public final OperandoContext operando() throws RecognitionException {
		OperandoContext _localctx = new OperandoContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_operando);
		try {
			setState(272);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(260);
				funcion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(261);
				match(VARIABLE);
				setState(262);
				match(T__17);
				setState(263);
				idName();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(264);
				match(INDIVIDUO);
				setState(265);
				match(T__17);
				setState(266);
				idName();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(267);
				match(INDIVIDUO);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(268);
				match(VARIABLE);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(269);
				match(NUMBER);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(270);
				match(STRING);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(271);
				match(BOOLEAN);
				}
				break;
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

	@SuppressWarnings("CheckReturnValue")
	public static class FuncionContext extends ParserRuleContext {
		public List<IdNameContext> idName() {
			return getRuleContexts(IdNameContext.class);
		}
		public IdNameContext idName(int i) {
			return getRuleContext(IdNameContext.class,i);
		}
		public ListaArgsFuncionContext listaArgsFuncion() {
			return getRuleContext(ListaArgsFuncionContext.class,0);
		}
		public FuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterFuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitFuncion(this);
		}
	}

	public final FuncionContext funcion() throws RecognitionException {
		FuncionContext _localctx = new FuncionContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_funcion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(274);
			idName();
			setState(275);
			match(T__17);
			setState(276);
			idName();
			setState(277);
			match(T__4);
			setState(279);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 133145034752L) != 0)) {
				{
				setState(278);
				listaArgsFuncion();
				}
			}

			setState(281);
			match(T__5);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ListaArgsFuncionContext extends ParserRuleContext {
		public List<ParamFuncionContext> paramFuncion() {
			return getRuleContexts(ParamFuncionContext.class);
		}
		public ParamFuncionContext paramFuncion(int i) {
			return getRuleContext(ParamFuncionContext.class,i);
		}
		public ListaArgsFuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaArgsFuncion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterListaArgsFuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitListaArgsFuncion(this);
		}
	}

	public final ListaArgsFuncionContext listaArgsFuncion() throws RecognitionException {
		ListaArgsFuncionContext _localctx = new ListaArgsFuncionContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_listaArgsFuncion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			paramFuncion();
			setState(288);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(284);
				match(T__6);
				setState(285);
				paramFuncion();
				}
				}
				setState(290);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ParamFuncionContext extends ParserRuleContext {
		public TerminalNode INDIVIDUO() { return getToken(gramaticaParser.INDIVIDUO, 0); }
		public TerminalNode VARIABLE() { return getToken(gramaticaParser.VARIABLE, 0); }
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public TerminalNode STRING() { return getToken(gramaticaParser.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(gramaticaParser.NUMBER, 0); }
		public TerminalNode BOOLEAN() { return getToken(gramaticaParser.BOOLEAN, 0); }
		public ParamFuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramFuncion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterParamFuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitParamFuncion(this);
		}
	}

	public final ParamFuncionContext paramFuncion() throws RecognitionException {
		ParamFuncionContext _localctx = new ParamFuncionContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_paramFuncion);
		int _la;
		try {
			setState(302);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(291);
				match(INDIVIDUO);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(292);
				match(VARIABLE);
				setState(293);
				match(T__17);
				setState(294);
				idName();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(296);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__19) {
					{
					setState(295);
					match(T__19);
					}
				}

				setState(298);
				match(VARIABLE);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(299);
				match(STRING);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(300);
				match(NUMBER);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(301);
				match(BOOLEAN);
				}
				break;
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

	@SuppressWarnings("CheckReturnValue")
	public static class OperacionLogicaContext extends ParserRuleContext {
		public OperacionLogicaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operacionLogica; }
	 
		public OperacionLogicaContext() { }
		public void copyFrom(OperacionLogicaContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OpOrContext extends OperacionLogicaContext {
		public TerminalNode OR() { return getToken(gramaticaParser.OR, 0); }
		public ListaCondicionesContext listaCondiciones() {
			return getRuleContext(ListaCondicionesContext.class,0);
		}
		public OpOrContext(OperacionLogicaContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterOpOr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitOpOr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OpNotContext extends OperacionLogicaContext {
		public TerminalNode NOT() { return getToken(gramaticaParser.NOT, 0); }
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public OpNotContext(OperacionLogicaContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterOpNot(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitOpNot(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OpAndContext extends OperacionLogicaContext {
		public TerminalNode AND() { return getToken(gramaticaParser.AND, 0); }
		public ListaCondicionesContext listaCondiciones() {
			return getRuleContext(ListaCondicionesContext.class,0);
		}
		public OpAndContext(OperacionLogicaContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterOpAnd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitOpAnd(this);
		}
	}

	public final OperacionLogicaContext operacionLogica() throws RecognitionException {
		OperacionLogicaContext _localctx = new OperacionLogicaContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_operacionLogica);
		try {
			setState(319);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OR:
				_localctx = new OpOrContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(304);
				match(OR);
				setState(305);
				match(T__4);
				setState(306);
				listaCondiciones();
				setState(307);
				match(T__5);
				}
				break;
			case AND:
				_localctx = new OpAndContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(309);
				match(AND);
				setState(310);
				match(T__4);
				setState(311);
				listaCondiciones();
				setState(312);
				match(T__5);
				}
				break;
			case NOT:
				_localctx = new OpNotContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(314);
				match(NOT);
				setState(315);
				match(T__4);
				setState(316);
				condicion();
				setState(317);
				match(T__5);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ListaConsecuenciasContext extends ParserRuleContext {
		public List<ConsecuenciaContext> consecuencia() {
			return getRuleContexts(ConsecuenciaContext.class);
		}
		public ConsecuenciaContext consecuencia(int i) {
			return getRuleContext(ConsecuenciaContext.class,i);
		}
		public List<ComentarioSimpleContext> comentarioSimple() {
			return getRuleContexts(ComentarioSimpleContext.class);
		}
		public ComentarioSimpleContext comentarioSimple(int i) {
			return getRuleContext(ComentarioSimpleContext.class,i);
		}
		public ListaConsecuenciasContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaConsecuencias; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterListaConsecuencias(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitListaConsecuencias(this);
		}
	}

	public final ListaConsecuenciasContext listaConsecuencias() throws RecognitionException {
		ListaConsecuenciasContext _localctx = new ListaConsecuenciasContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_listaConsecuencias);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(328);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 103081312256L) != 0)) {
				{
				{
				setState(321);
				consecuencia();
				setState(322);
				match(T__2);
				setState(324);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
				case 1:
					{
					setState(323);
					comentarioSimple();
					}
					break;
				}
				}
				}
				setState(330);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ConsecuenciaContext extends ParserRuleContext {
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public FuncionContext funcion() {
			return getRuleContext(FuncionContext.class,0);
		}
		public BorradoContext borrado() {
			return getRuleContext(BorradoContext.class,0);
		}
		public PredicadoContext predicado() {
			return getRuleContext(PredicadoContext.class,0);
		}
		public BloqueValoresContext bloqueValores() {
			return getRuleContext(BloqueValoresContext.class,0);
		}
		public ConsecuenciaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_consecuencia; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterConsecuencia(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitConsecuencia(this);
		}
	}

	public final ConsecuenciaContext consecuencia() throws RecognitionException {
		ConsecuenciaContext _localctx = new ConsecuenciaContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_consecuencia);
		int _la;
		try {
			setState(338);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(331);
				asignacion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(332);
				funcion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(333);
				borrado();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(334);
				predicado();
				setState(336);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__12) {
					{
					setState(335);
					bloqueValores();
					}
				}

				}
				break;
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

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends ParserRuleContext {
		public OperandoIzqContext operandoIzq() {
			return getRuleContext(OperandoIzqContext.class,0);
		}
		public OperandoDrcContext operandoDrc() {
			return getRuleContext(OperandoDrcContext.class,0);
		}
		public TerminalNode OpAsign() { return getToken(gramaticaParser.OpAsign, 0); }
		public TerminalNode OpIgual() { return getToken(gramaticaParser.OpIgual, 0); }
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterAsignacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitAsignacion(this);
		}
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_asignacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(340);
			operandoIzq();
			setState(341);
			_la = _input.LA(1);
			if ( !(_la==OpIgual || _la==OpAsign) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(342);
			operandoDrc();
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

	@SuppressWarnings("CheckReturnValue")
	public static class OperandoIzqContext extends ParserRuleContext {
		public TerminalNode VARIABLE() { return getToken(gramaticaParser.VARIABLE, 0); }
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public OperandoIzqContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operandoIzq; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterOperandoIzq(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitOperandoIzq(this);
		}
	}

	public final OperandoIzqContext operandoIzq() throws RecognitionException {
		OperandoIzqContext _localctx = new OperandoIzqContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_operandoIzq);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(344);
			match(VARIABLE);
			setState(345);
			match(T__17);
			setState(346);
			idName();
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

	@SuppressWarnings("CheckReturnValue")
	public static class OperandoDrcContext extends ParserRuleContext {
		public FuncionContext funcion() {
			return getRuleContext(FuncionContext.class,0);
		}
		public OperandoIzqContext operandoIzq() {
			return getRuleContext(OperandoIzqContext.class,0);
		}
		public TerminalNode NUMBER() { return getToken(gramaticaParser.NUMBER, 0); }
		public TerminalNode VARIABLE() { return getToken(gramaticaParser.VARIABLE, 0); }
		public OperandoDrcContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operandoDrc; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterOperandoDrc(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitOperandoDrc(this);
		}
	}

	public final OperandoDrcContext operandoDrc() throws RecognitionException {
		OperandoDrcContext _localctx = new OperandoDrcContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_operandoDrc);
		try {
			setState(352);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(348);
				funcion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(349);
				operandoIzq();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(350);
				match(NUMBER);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(351);
				match(VARIABLE);
				}
				break;
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

	@SuppressWarnings("CheckReturnValue")
	public static class BorradoContext extends ParserRuleContext {
		public PredicadoContext predicado() {
			return getRuleContext(PredicadoContext.class,0);
		}
		public BorradoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_borrado; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterBorrado(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitBorrado(this);
		}
	}

	public final BorradoContext borrado() throws RecognitionException {
		BorradoContext _localctx = new BorradoContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_borrado);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(354);
			match(T__20);
			setState(355);
			predicado();
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

	@SuppressWarnings("CheckReturnValue")
	public static class InicializacionContext extends ParserRuleContext {
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public List<ArgLitContext> argLit() {
			return getRuleContexts(ArgLitContext.class);
		}
		public ArgLitContext argLit(int i) {
			return getRuleContext(ArgLitContext.class,i);
		}
		public BloqueValoresContext bloqueValores() {
			return getRuleContext(BloqueValoresContext.class,0);
		}
		public InicializacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inicializacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterInicializacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitInicializacion(this);
		}
	}

	public final InicializacionContext inicializacion() throws RecognitionException {
		InicializacionContext _localctx = new InicializacionContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_inicializacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(357);
			match(T__21);
			}
			setState(358);
			idName();
			setState(359);
			match(T__4);
			setState(360);
			argLit();
			setState(365);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(361);
				match(T__6);
				setState(362);
				argLit();
				}
				}
				setState(367);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(368);
			match(T__5);
			setState(370);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(369);
				bloqueValores();
				}
			}

			setState(372);
			match(T__2);
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

	@SuppressWarnings("CheckReturnValue")
	public static class BloqueValoresContext extends ParserRuleContext {
		public ListaParejasValorContext listaParejasValor() {
			return getRuleContext(ListaParejasValorContext.class,0);
		}
		public BloqueValoresContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloqueValores; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterBloqueValores(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitBloqueValores(this);
		}
	}

	public final BloqueValoresContext bloqueValores() throws RecognitionException {
		BloqueValoresContext _localctx = new BloqueValoresContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_bloqueValores);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(374);
			match(T__12);
			setState(376);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INDIVIDUO || _la==VARIABLE) {
				{
				setState(375);
				listaParejasValor();
				}
			}

			setState(378);
			match(T__13);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ListaParejasValorContext extends ParserRuleContext {
		public List<ParejaValorContext> parejaValor() {
			return getRuleContexts(ParejaValorContext.class);
		}
		public ParejaValorContext parejaValor(int i) {
			return getRuleContext(ParejaValorContext.class,i);
		}
		public ListaParejasValorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaParejasValor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterListaParejasValor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitListaParejasValor(this);
		}
	}

	public final ListaParejasValorContext listaParejasValor() throws RecognitionException {
		ListaParejasValorContext _localctx = new ListaParejasValorContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_listaParejasValor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(380);
			parejaValor();
			setState(385);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(381);
				match(T__6);
				setState(382);
				parejaValor();
				}
				}
				setState(387);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ParejaValorContext extends ParserRuleContext {
		public List<IdNameContext> idName() {
			return getRuleContexts(IdNameContext.class);
		}
		public IdNameContext idName(int i) {
			return getRuleContext(IdNameContext.class,i);
		}
		public TerminalNode OpIgual() { return getToken(gramaticaParser.OpIgual, 0); }
		public ValorContext valor() {
			return getRuleContext(ValorContext.class,0);
		}
		public TerminalNode VARIABLE() { return getToken(gramaticaParser.VARIABLE, 0); }
		public ParejaValorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parejaValor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterParejaValor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitParejaValor(this);
		}
	}

	public final ParejaValorContext parejaValor() throws RecognitionException {
		ParejaValorContext _localctx = new ParejaValorContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_parejaValor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(388);
			idName();
			setState(389);
			match(OpIgual);
			setState(395);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				{
				setState(390);
				valor();
				}
				break;
			case 2:
				{
				setState(391);
				match(VARIABLE);
				setState(392);
				match(T__17);
				setState(393);
				idName();
				}
				break;
			case 3:
				{
				setState(394);
				match(VARIABLE);
				}
				break;
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

	@SuppressWarnings("CheckReturnValue")
	public static class ValorContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(gramaticaParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(gramaticaParser.STRING, 0); }
		public TerminalNode BOOLEAN() { return getToken(gramaticaParser.BOOLEAN, 0); }
		public ValorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterValor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitValor(this);
		}
	}

	public final ValorContext valor() throws RecognitionException {
		ValorContext _localctx = new ValorContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_valor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(397);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 30064771072L) != 0)) ) {
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

	@SuppressWarnings("CheckReturnValue")
	public static class ArgLitContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(gramaticaParser.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(gramaticaParser.NUMBER, 0); }
		public ArgLitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argLit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterArgLit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitArgLit(this);
		}
	}

	public final ArgLitContext argLit() throws RecognitionException {
		ArgLitContext _localctx = new ArgLitContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_argLit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(399);
			_la = _input.LA(1);
			if ( !(_la==STRING || _la==NUMBER) ) {
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

	@SuppressWarnings("CheckReturnValue")
	public static class EjecucionContext extends ParserRuleContext {
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public ListaArgLitContext listaArgLit() {
			return getRuleContext(ListaArgLitContext.class,0);
		}
		public EjecucionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ejecucion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterEjecucion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitEjecucion(this);
		}
	}

	public final EjecucionContext ejecucion() throws RecognitionException {
		EjecucionContext _localctx = new EjecucionContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_ejecucion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(401);
			match(T__22);
			setState(402);
			idName();
			setState(403);
			match(T__4);
			setState(405);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STRING || _la==NUMBER) {
				{
				setState(404);
				listaArgLit();
				}
			}

			setState(407);
			match(T__5);
			setState(408);
			match(T__2);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ListaArgLitContext extends ParserRuleContext {
		public List<ArgLitContext> argLit() {
			return getRuleContexts(ArgLitContext.class);
		}
		public ArgLitContext argLit(int i) {
			return getRuleContext(ArgLitContext.class,i);
		}
		public ListaArgLitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaArgLit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterListaArgLit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitListaArgLit(this);
		}
	}

	public final ListaArgLitContext listaArgLit() throws RecognitionException {
		ListaArgLitContext _localctx = new ListaArgLitContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_listaArgLit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(410);
			argLit();
			setState(415);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(411);
				match(T__6);
				setState(412);
				argLit();
				}
				}
				setState(417);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ComentarioSimpleContext extends ParserRuleContext {
		public TerminalNode COMMENT_SIMPLE() { return getToken(gramaticaParser.COMMENT_SIMPLE, 0); }
		public ComentarioSimpleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comentarioSimple; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterComentarioSimple(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitComentarioSimple(this);
		}
	}

	public final ComentarioSimpleContext comentarioSimple() throws RecognitionException {
		ComentarioSimpleContext _localctx = new ComentarioSimpleContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_comentarioSimple);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(418);
			match(COMMENT_SIMPLE);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ComentarioMultilineoContext extends ParserRuleContext {
		public TerminalNode COMMENT_MULTI() { return getToken(gramaticaParser.COMMENT_MULTI, 0); }
		public ComentarioMultilineoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comentarioMultilineo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterComentarioMultilineo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitComentarioMultilineo(this);
		}
	}

	public final ComentarioMultilineoContext comentarioMultilineo() throws RecognitionException {
		ComentarioMultilineoContext _localctx = new ComentarioMultilineoContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_comentarioMultilineo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(420);
			match(COMMENT_MULTI);
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

	@SuppressWarnings("CheckReturnValue")
	public static class IdNameContext extends ParserRuleContext {
		public TerminalNode INDIVIDUO() { return getToken(gramaticaParser.INDIVIDUO, 0); }
		public TerminalNode VARIABLE() { return getToken(gramaticaParser.VARIABLE, 0); }
		public IdNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterIdName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitIdName(this);
		}
	}

	public final IdNameContext idName() throws RecognitionException {
		IdNameContext _localctx = new IdNameContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_idName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(422);
			_la = _input.LA(1);
			if ( !(_la==INDIVIDUO || _la==VARIABLE) ) {
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
		"\u0004\u0001%\u01a9\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0001\u0000\u0005\u0000"+
		"Z\b\u0000\n\u0000\f\u0000]\t\u0000\u0001\u0000\u0005\u0000`\b\u0000\n"+
		"\u0000\f\u0000c\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002s\b\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003x\b\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0003\u0003}\b\u0003\u0003\u0003\u007f\b\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u0085\b\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005"+
		"\u008c\b\u0005\n\u0005\f\u0005\u008f\t\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0003\b\u009b\b\b\u0001\b\u0001\b\u0003\b\u009f\b\b\u0001\t\u0001\t"+
		"\u0003\t\u00a3\b\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0005\n\u00aa"+
		"\b\n\n\n\f\n\u00ad\t\n\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b"+
		"\u00b2\b\u000b\n\u000b\f\u000b\u00b5\t\u000b\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0003\f\u00bb\b\f\u0001\f\u0001\f\u0001\f\u0003\f\u00c0\b\f\u0001\f"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0005\r\u00ca"+
		"\b\r\n\r\f\r\u00cd\t\r\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e"+
		"\u00d2\b\u000e\u0005\u000e\u00d4\b\u000e\n\u000e\f\u000e\u00d7\t\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f"+
		"\u00de\b\u000f\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0003\u0011\u00e6\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0005\u0013"+
		"\u00f0\b\u0013\n\u0013\f\u0013\u00f3\t\u0013\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0003\u0014\u00ff\b\u0014\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0003\u0016\u0111\b\u0016\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u0118\b\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0005\u0018\u011f\b\u0018\n"+
		"\u0018\f\u0018\u0122\t\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0003\u0019\u0129\b\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0003\u0019\u012f\b\u0019\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0003\u001a\u0140\b\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0003"+
		"\u001b\u0145\b\u001b\u0005\u001b\u0147\b\u001b\n\u001b\f\u001b\u014a\t"+
		"\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0003"+
		"\u001c\u0151\b\u001c\u0003\u001c\u0153\b\u001c\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0003\u001f\u0161\b\u001f"+
		"\u0001 \u0001 \u0001 \u0001!\u0001!\u0001!\u0001!\u0001!\u0001!\u0005"+
		"!\u016c\b!\n!\f!\u016f\t!\u0001!\u0001!\u0003!\u0173\b!\u0001!\u0001!"+
		"\u0001\"\u0001\"\u0003\"\u0179\b\"\u0001\"\u0001\"\u0001#\u0001#\u0001"+
		"#\u0005#\u0180\b#\n#\f#\u0183\t#\u0001$\u0001$\u0001$\u0001$\u0001$\u0001"+
		"$\u0001$\u0003$\u018c\b$\u0001%\u0001%\u0001&\u0001&\u0001\'\u0001\'\u0001"+
		"\'\u0001\'\u0003\'\u0196\b\'\u0001\'\u0001\'\u0001\'\u0001(\u0001(\u0001"+
		"(\u0005(\u019e\b(\n(\f(\u01a1\t(\u0001)\u0001)\u0001*\u0001*\u0001+\u0001"+
		"+\u0001+\u0000\u0000,\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012"+
		"\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJLNPRTV\u0000"+
		"\u0005\u0001\u0000\t\u000b\u0001\u0000\u001c\u001d\u0001\u0000 \"\u0001"+
		"\u0000!\"\u0001\u0000#$\u01c1\u0000[\u0001\u0000\u0000\u0000\u0002f\u0001"+
		"\u0000\u0000\u0000\u0004r\u0001\u0000\u0000\u0000\u0006~\u0001\u0000\u0000"+
		"\u0000\b\u0080\u0001\u0000\u0000\u0000\n\u0088\u0001\u0000\u0000\u0000"+
		"\f\u0090\u0001\u0000\u0000\u0000\u000e\u0094\u0001\u0000\u0000\u0000\u0010"+
		"\u0096\u0001\u0000\u0000\u0000\u0012\u00a0\u0001\u0000\u0000\u0000\u0014"+
		"\u00a6\u0001\u0000\u0000\u0000\u0016\u00ae\u0001\u0000\u0000\u0000\u0018"+
		"\u00b6\u0001\u0000\u0000\u0000\u001a\u00c6\u0001\u0000\u0000\u0000\u001c"+
		"\u00d5\u0001\u0000\u0000\u0000\u001e\u00dd\u0001\u0000\u0000\u0000 \u00df"+
		"\u0001\u0000\u0000\u0000\"\u00e1\u0001\u0000\u0000\u0000$\u00e7\u0001"+
		"\u0000\u0000\u0000&\u00ec\u0001\u0000\u0000\u0000(\u00fe\u0001\u0000\u0000"+
		"\u0000*\u0100\u0001\u0000\u0000\u0000,\u0110\u0001\u0000\u0000\u0000."+
		"\u0112\u0001\u0000\u0000\u00000\u011b\u0001\u0000\u0000\u00002\u012e\u0001"+
		"\u0000\u0000\u00004\u013f\u0001\u0000\u0000\u00006\u0148\u0001\u0000\u0000"+
		"\u00008\u0152\u0001\u0000\u0000\u0000:\u0154\u0001\u0000\u0000\u0000<"+
		"\u0158\u0001\u0000\u0000\u0000>\u0160\u0001\u0000\u0000\u0000@\u0162\u0001"+
		"\u0000\u0000\u0000B\u0165\u0001\u0000\u0000\u0000D\u0176\u0001\u0000\u0000"+
		"\u0000F\u017c\u0001\u0000\u0000\u0000H\u0184\u0001\u0000\u0000\u0000J"+
		"\u018d\u0001\u0000\u0000\u0000L\u018f\u0001\u0000\u0000\u0000N\u0191\u0001"+
		"\u0000\u0000\u0000P\u019a\u0001\u0000\u0000\u0000R\u01a2\u0001\u0000\u0000"+
		"\u0000T\u01a4\u0001\u0000\u0000\u0000V\u01a6\u0001\u0000\u0000\u0000X"+
		"Z\u0003\u0002\u0001\u0000YX\u0001\u0000\u0000\u0000Z]\u0001\u0000\u0000"+
		"\u0000[Y\u0001\u0000\u0000\u0000[\\\u0001\u0000\u0000\u0000\\a\u0001\u0000"+
		"\u0000\u0000][\u0001\u0000\u0000\u0000^`\u0003\u0004\u0002\u0000_^\u0001"+
		"\u0000\u0000\u0000`c\u0001\u0000\u0000\u0000a_\u0001\u0000\u0000\u0000"+
		"ab\u0001\u0000\u0000\u0000bd\u0001\u0000\u0000\u0000ca\u0001\u0000\u0000"+
		"\u0000de\u0005\u0000\u0000\u0001e\u0001\u0001\u0000\u0000\u0000fg\u0005"+
		"\u0001\u0000\u0000gh\u0003V+\u0000hi\u0005\u0002\u0000\u0000ij\u0003V"+
		"+\u0000jk\u0005\u0003\u0000\u0000k\u0003\u0001\u0000\u0000\u0000ls\u0003"+
		"\u0006\u0003\u0000ms\u0003\u0018\f\u0000ns\u0003B!\u0000os\u0003N\'\u0000"+
		"ps\u0003R)\u0000qs\u0003T*\u0000rl\u0001\u0000\u0000\u0000rm\u0001\u0000"+
		"\u0000\u0000rn\u0001\u0000\u0000\u0000ro\u0001\u0000\u0000\u0000rp\u0001"+
		"\u0000\u0000\u0000rq\u0001\u0000\u0000\u0000s\u0005\u0001\u0000\u0000"+
		"\u0000tu\u0003\b\u0004\u0000uw\u0005\u0003\u0000\u0000vx\u0003R)\u0000"+
		"wv\u0001\u0000\u0000\u0000wx\u0001\u0000\u0000\u0000x\u007f\u0001\u0000"+
		"\u0000\u0000yz\u0003\u0010\b\u0000z|\u0005\u0003\u0000\u0000{}\u0003R"+
		")\u0000|{\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000}\u007f\u0001"+
		"\u0000\u0000\u0000~t\u0001\u0000\u0000\u0000~y\u0001\u0000\u0000\u0000"+
		"\u007f\u0007\u0001\u0000\u0000\u0000\u0080\u0081\u0005\u0004\u0000\u0000"+
		"\u0081\u0082\u0003V+\u0000\u0082\u0084\u0005\u0005\u0000\u0000\u0083\u0085"+
		"\u0003\n\u0005\u0000\u0084\u0083\u0001\u0000\u0000\u0000\u0084\u0085\u0001"+
		"\u0000\u0000\u0000\u0085\u0086\u0001\u0000\u0000\u0000\u0086\u0087\u0005"+
		"\u0006\u0000\u0000\u0087\t\u0001\u0000\u0000\u0000\u0088\u008d\u0003\f"+
		"\u0006\u0000\u0089\u008a\u0005\u0007\u0000\u0000\u008a\u008c\u0003\f\u0006"+
		"\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008c\u008f\u0001\u0000\u0000"+
		"\u0000\u008d\u008b\u0001\u0000\u0000\u0000\u008d\u008e\u0001\u0000\u0000"+
		"\u0000\u008e\u000b\u0001\u0000\u0000\u0000\u008f\u008d\u0001\u0000\u0000"+
		"\u0000\u0090\u0091\u0003V+\u0000\u0091\u0092\u0005\b\u0000\u0000\u0092"+
		"\u0093\u0003\u000e\u0007\u0000\u0093\r\u0001\u0000\u0000\u0000\u0094\u0095"+
		"\u0007\u0000\u0000\u0000\u0095\u000f\u0001\u0000\u0000\u0000\u0096\u0097"+
		"\u0005\f\u0000\u0000\u0097\u0098\u0003V+\u0000\u0098\u009a\u0005\u0005"+
		"\u0000\u0000\u0099\u009b\u0003\u0014\n\u0000\u009a\u0099\u0001\u0000\u0000"+
		"\u0000\u009a\u009b\u0001\u0000\u0000\u0000\u009b\u009c\u0001\u0000\u0000"+
		"\u0000\u009c\u009e\u0005\u0006\u0000\u0000\u009d\u009f\u0003\u0012\t\u0000"+
		"\u009e\u009d\u0001\u0000\u0000\u0000\u009e\u009f\u0001\u0000\u0000\u0000"+
		"\u009f\u0011\u0001\u0000\u0000\u0000\u00a0\u00a2\u0005\r\u0000\u0000\u00a1"+
		"\u00a3\u0003\u0016\u000b\u0000\u00a2\u00a1\u0001\u0000\u0000\u0000\u00a2"+
		"\u00a3\u0001\u0000\u0000\u0000\u00a3\u00a4\u0001\u0000\u0000\u0000\u00a4"+
		"\u00a5\u0005\u000e\u0000\u0000\u00a5\u0013\u0001\u0000\u0000\u0000\u00a6"+
		"\u00ab\u0003V+\u0000\u00a7\u00a8\u0005\u0007\u0000\u0000\u00a8\u00aa\u0003"+
		"V+\u0000\u00a9\u00a7\u0001\u0000\u0000\u0000\u00aa\u00ad\u0001\u0000\u0000"+
		"\u0000\u00ab\u00a9\u0001\u0000\u0000\u0000\u00ab\u00ac\u0001\u0000\u0000"+
		"\u0000\u00ac\u0015\u0001\u0000\u0000\u0000\u00ad\u00ab\u0001\u0000\u0000"+
		"\u0000\u00ae\u00b3\u0003V+\u0000\u00af\u00b0\u0005\u0007\u0000\u0000\u00b0"+
		"\u00b2\u0003V+\u0000\u00b1\u00af\u0001\u0000\u0000\u0000\u00b2\u00b5\u0001"+
		"\u0000\u0000\u0000\u00b3\u00b1\u0001\u0000\u0000\u0000\u00b3\u00b4\u0001"+
		"\u0000\u0000\u0000\u00b4\u0017\u0001\u0000\u0000\u0000\u00b5\u00b3\u0001"+
		"\u0000\u0000\u0000\u00b6\u00b7\u0005\u000f\u0000\u0000\u00b7\u00b8\u0003"+
		"V+\u0000\u00b8\u00ba\u0005\u0005\u0000\u0000\u00b9\u00bb\u0003\u001a\r"+
		"\u0000\u00ba\u00b9\u0001\u0000\u0000\u0000\u00ba\u00bb\u0001\u0000\u0000"+
		"\u0000\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc\u00bd\u0005\u0006\u0000"+
		"\u0000\u00bd\u00bf\u0005\b\u0000\u0000\u00be\u00c0\u0003T*\u0000\u00bf"+
		"\u00be\u0001\u0000\u0000\u0000\u00bf\u00c0\u0001\u0000\u0000\u0000\u00c0"+
		"\u00c1\u0001\u0000\u0000\u0000\u00c1\u00c2\u0005\u0010\u0000\u0000\u00c2"+
		"\u00c3\u0003\u001c\u000e\u0000\u00c3\u00c4\u0005\u0011\u0000\u0000\u00c4"+
		"\u00c5\u00036\u001b\u0000\u00c5\u0019\u0001\u0000\u0000\u0000\u00c6\u00cb"+
		"\u0003V+\u0000\u00c7\u00c8\u0005\u0007\u0000\u0000\u00c8\u00ca\u0003V"+
		"+\u0000\u00c9\u00c7\u0001\u0000\u0000\u0000\u00ca\u00cd\u0001\u0000\u0000"+
		"\u0000\u00cb\u00c9\u0001\u0000\u0000\u0000\u00cb\u00cc\u0001\u0000\u0000"+
		"\u0000\u00cc\u001b\u0001\u0000\u0000\u0000\u00cd\u00cb\u0001\u0000\u0000"+
		"\u0000\u00ce\u00cf\u0003\u001e\u000f\u0000\u00cf\u00d1\u0005\u0003\u0000"+
		"\u0000\u00d0\u00d2\u0003R)\u0000\u00d1\u00d0\u0001\u0000\u0000\u0000\u00d1"+
		"\u00d2\u0001\u0000\u0000\u0000\u00d2\u00d4\u0001\u0000\u0000\u0000\u00d3"+
		"\u00ce\u0001\u0000\u0000\u0000\u00d4\u00d7\u0001\u0000\u0000\u0000\u00d5"+
		"\u00d3\u0001\u0000\u0000\u0000\u00d5\u00d6\u0001\u0000\u0000\u0000\u00d6"+
		"\u001d\u0001\u0000\u0000\u0000\u00d7\u00d5\u0001\u0000\u0000\u0000\u00d8"+
		"\u00de\u0003$\u0012\u0000\u00d9\u00de\u0003*\u0015\u0000\u00da\u00de\u0003"+
		"4\u001a\u0000\u00db\u00de\u0003\"\u0011\u0000\u00dc\u00de\u0003 \u0010"+
		"\u0000\u00dd\u00d8\u0001\u0000\u0000\u0000\u00dd\u00d9\u0001\u0000\u0000"+
		"\u0000\u00dd\u00da\u0001\u0000\u0000\u0000\u00dd\u00db\u0001\u0000\u0000"+
		"\u0000\u00dd\u00dc\u0001\u0000\u0000\u0000\u00de\u001f\u0001\u0000\u0000"+
		"\u0000\u00df\u00e0\u0003.\u0017\u0000\u00e0!\u0001\u0000\u0000\u0000\u00e1"+
		"\u00e2\u0005$\u0000\u0000\u00e2\u00e5\u0005\u001c\u0000\u0000\u00e3\u00e6"+
		"\u0003$\u0012\u0000\u00e4\u00e6\u0003.\u0017\u0000\u00e5\u00e3\u0001\u0000"+
		"\u0000\u0000\u00e5\u00e4\u0001\u0000\u0000\u0000\u00e6#\u0001\u0000\u0000"+
		"\u0000\u00e7\u00e8\u0003V+\u0000\u00e8\u00e9\u0005\u0005\u0000\u0000\u00e9"+
		"\u00ea\u0003&\u0013\u0000\u00ea\u00eb\u0005\u0006\u0000\u0000\u00eb%\u0001"+
		"\u0000\u0000\u0000\u00ec\u00f1\u0003(\u0014\u0000\u00ed\u00ee\u0005\u0007"+
		"\u0000\u0000\u00ee\u00f0\u0003(\u0014\u0000\u00ef\u00ed\u0001\u0000\u0000"+
		"\u0000\u00f0\u00f3\u0001\u0000\u0000\u0000\u00f1\u00ef\u0001\u0000\u0000"+
		"\u0000\u00f1\u00f2\u0001\u0000\u0000\u0000\u00f2\'\u0001\u0000\u0000\u0000"+
		"\u00f3\u00f1\u0001\u0000\u0000\u0000\u00f4\u00ff\u0005#\u0000\u0000\u00f5"+
		"\u00ff\u0003.\u0017\u0000\u00f6\u00f7\u0005$\u0000\u0000\u00f7\u00f8\u0005"+
		"\u0012\u0000\u0000\u00f8\u00ff\u0003V+\u0000\u00f9\u00ff\u0005$\u0000"+
		"\u0000\u00fa\u00ff\u0005!\u0000\u0000\u00fb\u00ff\u0005\"\u0000\u0000"+
		"\u00fc\u00ff\u0005 \u0000\u0000\u00fd\u00ff\u0005\u0013\u0000\u0000\u00fe"+
		"\u00f4\u0001\u0000\u0000\u0000\u00fe\u00f5\u0001\u0000\u0000\u0000\u00fe"+
		"\u00f6\u0001\u0000\u0000\u0000\u00fe\u00f9\u0001\u0000\u0000\u0000\u00fe"+
		"\u00fa\u0001\u0000\u0000\u0000\u00fe\u00fb\u0001\u0000\u0000\u0000\u00fe"+
		"\u00fc\u0001\u0000\u0000\u0000\u00fe\u00fd\u0001\u0000\u0000\u0000\u00ff"+
		")\u0001\u0000\u0000\u0000\u0100\u0101\u0003,\u0016\u0000\u0101\u0102\u0005"+
		"\u0018\u0000\u0000\u0102\u0103\u0003,\u0016\u0000\u0103+\u0001\u0000\u0000"+
		"\u0000\u0104\u0111\u0003.\u0017\u0000\u0105\u0106\u0005$\u0000\u0000\u0106"+
		"\u0107\u0005\u0012\u0000\u0000\u0107\u0111\u0003V+\u0000\u0108\u0109\u0005"+
		"#\u0000\u0000\u0109\u010a\u0005\u0012\u0000\u0000\u010a\u0111\u0003V+"+
		"\u0000\u010b\u0111\u0005#\u0000\u0000\u010c\u0111\u0005$\u0000\u0000\u010d"+
		"\u0111\u0005\"\u0000\u0000\u010e\u0111\u0005!\u0000\u0000\u010f\u0111"+
		"\u0005 \u0000\u0000\u0110\u0104\u0001\u0000\u0000\u0000\u0110\u0105\u0001"+
		"\u0000\u0000\u0000\u0110\u0108\u0001\u0000\u0000\u0000\u0110\u010b\u0001"+
		"\u0000\u0000\u0000\u0110\u010c\u0001\u0000\u0000\u0000\u0110\u010d\u0001"+
		"\u0000\u0000\u0000\u0110\u010e\u0001\u0000\u0000\u0000\u0110\u010f\u0001"+
		"\u0000\u0000\u0000\u0111-\u0001\u0000\u0000\u0000\u0112\u0113\u0003V+"+
		"\u0000\u0113\u0114\u0005\u0012\u0000\u0000\u0114\u0115\u0003V+\u0000\u0115"+
		"\u0117\u0005\u0005\u0000\u0000\u0116\u0118\u00030\u0018\u0000\u0117\u0116"+
		"\u0001\u0000\u0000\u0000\u0117\u0118\u0001\u0000\u0000\u0000\u0118\u0119"+
		"\u0001\u0000\u0000\u0000\u0119\u011a\u0005\u0006\u0000\u0000\u011a/\u0001"+
		"\u0000\u0000\u0000\u011b\u0120\u00032\u0019\u0000\u011c\u011d\u0005\u0007"+
		"\u0000\u0000\u011d\u011f\u00032\u0019\u0000\u011e\u011c\u0001\u0000\u0000"+
		"\u0000\u011f\u0122\u0001\u0000\u0000\u0000\u0120\u011e\u0001\u0000\u0000"+
		"\u0000\u0120\u0121\u0001\u0000\u0000\u0000\u01211\u0001\u0000\u0000\u0000"+
		"\u0122\u0120\u0001\u0000\u0000\u0000\u0123\u012f\u0005#\u0000\u0000\u0124"+
		"\u0125\u0005$\u0000\u0000\u0125\u0126\u0005\u0012\u0000\u0000\u0126\u012f"+
		"\u0003V+\u0000\u0127\u0129\u0005\u0014\u0000\u0000\u0128\u0127\u0001\u0000"+
		"\u0000\u0000\u0128\u0129\u0001\u0000\u0000\u0000\u0129\u012a\u0001\u0000"+
		"\u0000\u0000\u012a\u012f\u0005$\u0000\u0000\u012b\u012f\u0005!\u0000\u0000"+
		"\u012c\u012f\u0005\"\u0000\u0000\u012d\u012f\u0005 \u0000\u0000\u012e"+
		"\u0123\u0001\u0000\u0000\u0000\u012e\u0124\u0001\u0000\u0000\u0000\u012e"+
		"\u0128\u0001\u0000\u0000\u0000\u012e\u012b\u0001\u0000\u0000\u0000\u012e"+
		"\u012c\u0001\u0000\u0000\u0000\u012e\u012d\u0001\u0000\u0000\u0000\u012f"+
		"3\u0001\u0000\u0000\u0000\u0130\u0131\u0005\u0019\u0000\u0000\u0131\u0132"+
		"\u0005\u0005\u0000\u0000\u0132\u0133\u0003\u001c\u000e\u0000\u0133\u0134"+
		"\u0005\u0006\u0000\u0000\u0134\u0140\u0001\u0000\u0000\u0000\u0135\u0136"+
		"\u0005\u001a\u0000\u0000\u0136\u0137\u0005\u0005\u0000\u0000\u0137\u0138"+
		"\u0003\u001c\u000e\u0000\u0138\u0139\u0005\u0006\u0000\u0000\u0139\u0140"+
		"\u0001\u0000\u0000\u0000\u013a\u013b\u0005\u001b\u0000\u0000\u013b\u013c"+
		"\u0005\u0005\u0000\u0000\u013c\u013d\u0003\u001e\u000f\u0000\u013d\u013e"+
		"\u0005\u0006\u0000\u0000\u013e\u0140\u0001\u0000\u0000\u0000\u013f\u0130"+
		"\u0001\u0000\u0000\u0000\u013f\u0135\u0001\u0000\u0000\u0000\u013f\u013a"+
		"\u0001\u0000\u0000\u0000\u01405\u0001\u0000\u0000\u0000\u0141\u0142\u0003"+
		"8\u001c\u0000\u0142\u0144\u0005\u0003\u0000\u0000\u0143\u0145\u0003R)"+
		"\u0000\u0144\u0143\u0001\u0000\u0000\u0000\u0144\u0145\u0001\u0000\u0000"+
		"\u0000\u0145\u0147\u0001\u0000\u0000\u0000\u0146\u0141\u0001\u0000\u0000"+
		"\u0000\u0147\u014a\u0001\u0000\u0000\u0000\u0148\u0146\u0001\u0000\u0000"+
		"\u0000\u0148\u0149\u0001\u0000\u0000\u0000\u01497\u0001\u0000\u0000\u0000"+
		"\u014a\u0148\u0001\u0000\u0000\u0000\u014b\u0153\u0003:\u001d\u0000\u014c"+
		"\u0153\u0003.\u0017\u0000\u014d\u0153\u0003@ \u0000\u014e\u0150\u0003"+
		"$\u0012\u0000\u014f\u0151\u0003D\"\u0000\u0150\u014f\u0001\u0000\u0000"+
		"\u0000\u0150\u0151\u0001\u0000\u0000\u0000\u0151\u0153\u0001\u0000\u0000"+
		"\u0000\u0152\u014b\u0001\u0000\u0000\u0000\u0152\u014c\u0001\u0000\u0000"+
		"\u0000\u0152\u014d\u0001\u0000\u0000\u0000\u0152\u014e\u0001\u0000\u0000"+
		"\u0000\u01539\u0001\u0000\u0000\u0000\u0154\u0155\u0003<\u001e\u0000\u0155"+
		"\u0156\u0007\u0001\u0000\u0000\u0156\u0157\u0003>\u001f\u0000\u0157;\u0001"+
		"\u0000\u0000\u0000\u0158\u0159\u0005$\u0000\u0000\u0159\u015a\u0005\u0012"+
		"\u0000\u0000\u015a\u015b\u0003V+\u0000\u015b=\u0001\u0000\u0000\u0000"+
		"\u015c\u0161\u0003.\u0017\u0000\u015d\u0161\u0003<\u001e\u0000\u015e\u0161"+
		"\u0005\"\u0000\u0000\u015f\u0161\u0005$\u0000\u0000\u0160\u015c\u0001"+
		"\u0000\u0000\u0000\u0160\u015d\u0001\u0000\u0000\u0000\u0160\u015e\u0001"+
		"\u0000\u0000\u0000\u0160\u015f\u0001\u0000\u0000\u0000\u0161?\u0001\u0000"+
		"\u0000\u0000\u0162\u0163\u0005\u0015\u0000\u0000\u0163\u0164\u0003$\u0012"+
		"\u0000\u0164A\u0001\u0000\u0000\u0000\u0165\u0166\u0005\u0016\u0000\u0000"+
		"\u0166\u0167\u0003V+\u0000\u0167\u0168\u0005\u0005\u0000\u0000\u0168\u016d"+
		"\u0003L&\u0000\u0169\u016a\u0005\u0007\u0000\u0000\u016a\u016c\u0003L"+
		"&\u0000\u016b\u0169\u0001\u0000\u0000\u0000\u016c\u016f\u0001\u0000\u0000"+
		"\u0000\u016d\u016b\u0001\u0000\u0000\u0000\u016d\u016e\u0001\u0000\u0000"+
		"\u0000\u016e\u0170\u0001\u0000\u0000\u0000\u016f\u016d\u0001\u0000\u0000"+
		"\u0000\u0170\u0172\u0005\u0006\u0000\u0000\u0171\u0173\u0003D\"\u0000"+
		"\u0172\u0171\u0001\u0000\u0000\u0000\u0172\u0173\u0001\u0000\u0000\u0000"+
		"\u0173\u0174\u0001\u0000\u0000\u0000\u0174\u0175\u0005\u0003\u0000\u0000"+
		"\u0175C\u0001\u0000\u0000\u0000\u0176\u0178\u0005\r\u0000\u0000\u0177"+
		"\u0179\u0003F#\u0000\u0178\u0177\u0001\u0000\u0000\u0000\u0178\u0179\u0001"+
		"\u0000\u0000\u0000\u0179\u017a\u0001\u0000\u0000\u0000\u017a\u017b\u0005"+
		"\u000e\u0000\u0000\u017bE\u0001\u0000\u0000\u0000\u017c\u0181\u0003H$"+
		"\u0000\u017d\u017e\u0005\u0007\u0000\u0000\u017e\u0180\u0003H$\u0000\u017f"+
		"\u017d\u0001\u0000\u0000\u0000\u0180\u0183\u0001\u0000\u0000\u0000\u0181"+
		"\u017f\u0001\u0000\u0000\u0000\u0181\u0182\u0001\u0000\u0000\u0000\u0182"+
		"G\u0001\u0000\u0000\u0000\u0183\u0181\u0001\u0000\u0000\u0000\u0184\u0185"+
		"\u0003V+\u0000\u0185\u018b\u0005\u001c\u0000\u0000\u0186\u018c\u0003J"+
		"%\u0000\u0187\u0188\u0005$\u0000\u0000\u0188\u0189\u0005\u0012\u0000\u0000"+
		"\u0189\u018c\u0003V+\u0000\u018a\u018c\u0005$\u0000\u0000\u018b\u0186"+
		"\u0001\u0000\u0000\u0000\u018b\u0187\u0001\u0000\u0000\u0000\u018b\u018a"+
		"\u0001\u0000\u0000\u0000\u018cI\u0001\u0000\u0000\u0000\u018d\u018e\u0007"+
		"\u0002\u0000\u0000\u018eK\u0001\u0000\u0000\u0000\u018f\u0190\u0007\u0003"+
		"\u0000\u0000\u0190M\u0001\u0000\u0000\u0000\u0191\u0192\u0005\u0017\u0000"+
		"\u0000\u0192\u0193\u0003V+\u0000\u0193\u0195\u0005\u0005\u0000\u0000\u0194"+
		"\u0196\u0003P(\u0000\u0195\u0194\u0001\u0000\u0000\u0000\u0195\u0196\u0001"+
		"\u0000\u0000\u0000\u0196\u0197\u0001\u0000\u0000\u0000\u0197\u0198\u0005"+
		"\u0006\u0000\u0000\u0198\u0199\u0005\u0003\u0000\u0000\u0199O\u0001\u0000"+
		"\u0000\u0000\u019a\u019f\u0003L&\u0000\u019b\u019c\u0005\u0007\u0000\u0000"+
		"\u019c\u019e\u0003L&\u0000\u019d\u019b\u0001\u0000\u0000\u0000\u019e\u01a1"+
		"\u0001\u0000\u0000\u0000\u019f\u019d\u0001\u0000\u0000\u0000\u019f\u01a0"+
		"\u0001\u0000\u0000\u0000\u01a0Q\u0001\u0000\u0000\u0000\u01a1\u019f\u0001"+
		"\u0000\u0000\u0000\u01a2\u01a3\u0005\u001e\u0000\u0000\u01a3S\u0001\u0000"+
		"\u0000\u0000\u01a4\u01a5\u0005\u001f\u0000\u0000\u01a5U\u0001\u0000\u0000"+
		"\u0000\u01a6\u01a7\u0007\u0004\u0000\u0000\u01a7W\u0001\u0000\u0000\u0000"+
		"([arw|~\u0084\u008d\u009a\u009e\u00a2\u00ab\u00b3\u00ba\u00bf\u00cb\u00d1"+
		"\u00d5\u00dd\u00e5\u00f1\u00fe\u0110\u0117\u0120\u0128\u012e\u013f\u0144"+
		"\u0148\u0150\u0152\u0160\u016d\u0172\u0178\u0181\u018b\u0195\u019f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}