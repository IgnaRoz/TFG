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
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, OpComp=29, OR=30, AND=31, NOT=32, 
		OpIgual=33, OpAsign=34, COMMENT_SIMPLE=35, COMMENT_MULTI=36, BOOLEAN=37, 
		STRING=38, NUMBER=39, INDIVIDUO=40, VARIABLE=41, WS=42;
	public static final int
		RULE_programa = 0, RULE_imports = 1, RULE_elemento = 2, RULE_declaracion = 3, 
		RULE_declCategoria = 4, RULE_listaAtributos = 5, RULE_atributo = 6, RULE_tipoBasico = 7, 
		RULE_declProposicion = 8, RULE_bloquePropiedades = 9, RULE_listaIdentificadores = 10, 
		RULE_listaPropiedades = 11, RULE_propiedad = 12, RULE_accion = 13, RULE_contingencia = 14, 
		RULE_listaParams = 15, RULE_listaCondiciones = 16, RULE_condicion = 17, 
		RULE_condicionRule = 18, RULE_condicionFuncion = 19, RULE_asignacionVariable = 20, 
		RULE_predicado = 21, RULE_listaArgsPredicado = 22, RULE_paramPredicado = 23, 
		RULE_comparacion = 24, RULE_operando = 25, RULE_funcion = 26, RULE_listaArgsFuncion = 27, 
		RULE_paramFuncion = 28, RULE_operacionLogica = 29, RULE_listaConsecuencias = 30, 
		RULE_consecuencia = 31, RULE_consecuenciaRule = 32, RULE_asignacion = 33, 
		RULE_operandoIzq = 34, RULE_operandoDrc = 35, RULE_borrado = 36, RULE_inicializacion = 37, 
		RULE_bloqueValores = 38, RULE_listaParejasValor = 39, RULE_parejaValor = 40, 
		RULE_valor = 41, RULE_argLit = 42, RULE_ejecucion = 43, RULE_listaArgLit = 44, 
		RULE_comentarioSimple = 45, RULE_comentarioMultilineo = 46, RULE_idName = 47;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "imports", "elemento", "declaracion", "declCategoria", "listaAtributos", 
			"atributo", "tipoBasico", "declProposicion", "bloquePropiedades", "listaIdentificadores", 
			"listaPropiedades", "propiedad", "accion", "contingencia", "listaParams", 
			"listaCondiciones", "condicion", "condicionRule", "condicionFuncion", 
			"asignacionVariable", "predicado", "listaArgsPredicado", "paramPredicado", 
			"comparacion", "operando", "funcion", "listaArgsFuncion", "paramFuncion", 
			"operacionLogica", "listaConsecuencias", "consecuencia", "consecuenciaRule", 
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
			"':'", "'int'", "'str'", "'bool'", "'Prep'", "'{'", "'}'", "'Accion'", 
			"'Rule'", "'Condiciones:'", "'Consecuencias:'", "'Pre'", "'Post'", "'Contingencia'", 
			"'rule'", "'.'", "'_'", "'*'", "'DEL'", "'add'", "'Run'", null, "'OR'", 
			"'AND'", "'NOT'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "OpComp", "OR", "AND", "NOT", "OpIgual", 
			"OpAsign", "COMMENT_SIMPLE", "COMMENT_MULTI", "BOOLEAN", "STRING", "NUMBER", 
			"INDIVIDUO", "VARIABLE", "WS"
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
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0) {
				{
				{
				setState(96);
				imports();
				}
				}
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(105);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 103481970704L) != 0)) {
				{
				{
				setState(102);
				elemento();
				}
				}
				setState(107);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(108);
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
			setState(110);
			match(T__0);
			setState(111);
			idName();
			setState(112);
			match(T__1);
			setState(113);
			idName();
			setState(114);
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
			setState(122);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
			case T__11:
				enterOuterAlt(_localctx, 1);
				{
				setState(116);
				declaracion();
				}
				break;
			case T__14:
			case T__15:
				enterOuterAlt(_localctx, 2);
				{
				setState(117);
				accion();
				}
				break;
			case T__26:
				enterOuterAlt(_localctx, 3);
				{
				setState(118);
				inicializacion();
				}
				break;
			case T__27:
				enterOuterAlt(_localctx, 4);
				{
				setState(119);
				ejecucion();
				}
				break;
			case COMMENT_SIMPLE:
				enterOuterAlt(_localctx, 5);
				{
				setState(120);
				comentarioSimple();
				}
				break;
			case COMMENT_MULTI:
				enterOuterAlt(_localctx, 6);
				{
				setState(121);
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
			setState(134);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(124);
				declCategoria();
				setState(125);
				match(T__2);
				setState(127);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
				case 1:
					{
					setState(126);
					comentarioSimple();
					}
					break;
				}
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 2);
				{
				setState(129);
				declProposicion();
				setState(130);
				match(T__2);
				setState(132);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
				case 1:
					{
					setState(131);
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
			setState(136);
			match(T__3);
			setState(137);
			idName();
			setState(138);
			match(T__4);
			setState(140);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INDIVIDUO || _la==VARIABLE) {
				{
				setState(139);
				listaAtributos();
				}
			}

			setState(142);
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
			setState(144);
			atributo();
			setState(149);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(145);
				match(T__6);
				setState(146);
				atributo();
				}
				}
				setState(151);
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
			setState(152);
			idName();
			setState(153);
			match(T__7);
			setState(154);
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
			setState(156);
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
		public List<IdNameContext> idName() {
			return getRuleContexts(IdNameContext.class);
		}
		public IdNameContext idName(int i) {
			return getRuleContext(IdNameContext.class,i);
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
			setState(158);
			match(T__11);
			setState(159);
			idName();
			setState(160);
			match(T__4);
			setState(162);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INDIVIDUO || _la==VARIABLE) {
				{
				setState(161);
				listaIdentificadores();
				}
			}

			setState(164);
			match(T__5);
			setState(167);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__7) {
				{
				setState(165);
				match(T__7);
				setState(166);
				idName();
				}
			}

			setState(170);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(169);
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
			setState(172);
			match(T__12);
			setState(174);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INDIVIDUO || _la==VARIABLE) {
				{
				setState(173);
				listaPropiedades();
				}
			}

			setState(176);
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
			setState(178);
			idName();
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(179);
				match(T__6);
				setState(180);
				idName();
				}
				}
				setState(185);
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
		public List<PropiedadContext> propiedad() {
			return getRuleContexts(PropiedadContext.class);
		}
		public PropiedadContext propiedad(int i) {
			return getRuleContext(PropiedadContext.class,i);
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
			setState(186);
			propiedad();
			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(187);
				match(T__6);
				setState(188);
				propiedad();
				}
				}
				setState(193);
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
	public static class PropiedadContext extends ParserRuleContext {
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public TerminalNode OpIgual() { return getToken(gramaticaParser.OpIgual, 0); }
		public ValorContext valor() {
			return getRuleContext(ValorContext.class,0);
		}
		public PropiedadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_propiedad; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterPropiedad(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitPropiedad(this);
		}
	}

	public final PropiedadContext propiedad() throws RecognitionException {
		PropiedadContext _localctx = new PropiedadContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_propiedad);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			idName();
			setState(197);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OpIgual) {
				{
				setState(195);
				match(OpIgual);
				setState(196);
				valor();
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
		public List<ContingenciaContext> contingencia() {
			return getRuleContexts(ContingenciaContext.class);
		}
		public ContingenciaContext contingencia(int i) {
			return getRuleContext(ContingenciaContext.class,i);
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
		enterRule(_localctx, 26, RULE_accion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(199);
			_la = _input.LA(1);
			if ( !(_la==T__14 || _la==T__15) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(200);
			idName();
			setState(201);
			match(T__4);
			setState(203);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INDIVIDUO || _la==VARIABLE) {
				{
				setState(202);
				listaParams();
				}
			}

			setState(205);
			match(T__5);
			setState(206);
			match(T__7);
			setState(208);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMENT_MULTI) {
				{
				setState(207);
				comentarioMultilineo();
				}
			}

			setState(210);
			match(T__16);
			setState(211);
			listaCondiciones();
			setState(212);
			match(T__17);
			setState(213);
			listaConsecuencias();
			setState(217);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3670016L) != 0)) {
				{
				{
				setState(214);
				contingencia();
				}
				}
				setState(219);
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
	public static class ContingenciaContext extends ParserRuleContext {
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public ListaCondicionesContext listaCondiciones() {
			return getRuleContext(ListaCondicionesContext.class,0);
		}
		public ListaConsecuenciasContext listaConsecuencias() {
			return getRuleContext(ListaConsecuenciasContext.class,0);
		}
		public ComentarioMultilineoContext comentarioMultilineo() {
			return getRuleContext(ComentarioMultilineoContext.class,0);
		}
		public ContingenciaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_contingencia; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterContingencia(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitContingencia(this);
		}
	}

	public final ContingenciaContext contingencia() throws RecognitionException {
		ContingenciaContext _localctx = new ContingenciaContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_contingencia);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__18 || _la==T__19) {
				{
				setState(220);
				_la = _input.LA(1);
				if ( !(_la==T__18 || _la==T__19) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(223);
			match(T__20);
			setState(224);
			idName();
			setState(225);
			match(T__7);
			setState(227);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMENT_MULTI) {
				{
				setState(226);
				comentarioMultilineo();
				}
			}

			setState(229);
			match(T__16);
			setState(230);
			listaCondiciones();
			setState(231);
			match(T__17);
			setState(232);
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
		enterRule(_localctx, 30, RULE_listaParams);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			idName();
			setState(239);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(235);
				match(T__6);
				setState(236);
				idName();
				}
				}
				setState(241);
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
		enterRule(_localctx, 32, RULE_listaCondiciones);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(249);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4268127944704L) != 0)) {
				{
				{
				setState(242);
				condicion();
				setState(243);
				match(T__2);
				setState(245);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMENT_SIMPLE) {
					{
					setState(244);
					comentarioSimple();
					}
				}

				}
				}
				setState(251);
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
		public CondicionRuleContext condicionRule() {
			return getRuleContext(CondicionRuleContext.class,0);
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
		enterRule(_localctx, 34, RULE_condicion);
		try {
			setState(258);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(252);
				predicado();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(253);
				comparacion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(254);
				operacionLogica();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(255);
				asignacionVariable();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(256);
				condicionFuncion();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(257);
				condicionRule();
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
	public static class CondicionRuleContext extends ParserRuleContext {
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public ListaArgsPredicadoContext listaArgsPredicado() {
			return getRuleContext(ListaArgsPredicadoContext.class,0);
		}
		public CondicionRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicionRule; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterCondicionRule(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitCondicionRule(this);
		}
	}

	public final CondicionRuleContext condicionRule() throws RecognitionException {
		CondicionRuleContext _localctx = new CondicionRuleContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_condicionRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			match(T__21);
			setState(261);
			idName();
			setState(262);
			match(T__4);
			setState(263);
			listaArgsPredicado();
			setState(264);
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
		enterRule(_localctx, 38, RULE_condicionFuncion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(266);
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
		public List<TerminalNode> VARIABLE() { return getTokens(gramaticaParser.VARIABLE); }
		public TerminalNode VARIABLE(int i) {
			return getToken(gramaticaParser.VARIABLE, i);
		}
		public TerminalNode OpIgual() { return getToken(gramaticaParser.OpIgual, 0); }
		public PredicadoContext predicado() {
			return getRuleContext(PredicadoContext.class,0);
		}
		public FuncionContext funcion() {
			return getRuleContext(FuncionContext.class,0);
		}
		public ValorContext valor() {
			return getRuleContext(ValorContext.class,0);
		}
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
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
		enterRule(_localctx, 40, RULE_asignacionVariable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			match(VARIABLE);
			setState(269);
			match(OpIgual);
			setState(277);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				{
				setState(270);
				predicado();
				}
				break;
			case 2:
				{
				setState(271);
				funcion();
				}
				break;
			case 3:
				{
				setState(272);
				valor();
				}
				break;
			case 4:
				{
				setState(273);
				match(VARIABLE);
				setState(274);
				match(T__22);
				setState(275);
				idName();
				}
				break;
			case 5:
				{
				setState(276);
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
		enterRule(_localctx, 42, RULE_predicado);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(279);
			idName();
			setState(280);
			match(T__4);
			setState(281);
			listaArgsPredicado();
			setState(282);
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
		enterRule(_localctx, 44, RULE_listaArgsPredicado);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			paramPredicado();
			setState(289);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(285);
				match(T__6);
				setState(286);
				paramPredicado();
				}
				}
				setState(291);
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
		enterRule(_localctx, 46, RULE_paramPredicado);
		try {
			setState(302);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(292);
				match(INDIVIDUO);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(293);
				funcion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(294);
				match(VARIABLE);
				setState(295);
				match(T__22);
				setState(296);
				idName();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(297);
				match(VARIABLE);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(298);
				match(STRING);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(299);
				match(NUMBER);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(300);
				match(BOOLEAN);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(301);
				match(T__23);
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
		enterRule(_localctx, 48, RULE_comparacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(304);
			operando();
			setState(305);
			match(OpComp);
			setState(306);
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
		enterRule(_localctx, 50, RULE_operando);
		try {
			setState(320);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(308);
				funcion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(309);
				match(VARIABLE);
				setState(310);
				match(T__22);
				setState(311);
				idName();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(312);
				match(INDIVIDUO);
				setState(313);
				match(T__22);
				setState(314);
				idName();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(315);
				match(INDIVIDUO);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(316);
				match(VARIABLE);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(317);
				match(NUMBER);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(318);
				match(STRING);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(319);
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
		enterRule(_localctx, 52, RULE_funcion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(322);
			idName();
			setState(323);
			match(T__22);
			setState(324);
			idName();
			setState(325);
			match(T__4);
			setState(327);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4260641112064L) != 0)) {
				{
				setState(326);
				listaArgsFuncion();
				}
			}

			setState(329);
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
		enterRule(_localctx, 54, RULE_listaArgsFuncion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(331);
			paramFuncion();
			setState(336);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(332);
				match(T__6);
				setState(333);
				paramFuncion();
				}
				}
				setState(338);
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
		enterRule(_localctx, 56, RULE_paramFuncion);
		int _la;
		try {
			setState(350);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(339);
				match(INDIVIDUO);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(340);
				match(VARIABLE);
				setState(341);
				match(T__22);
				setState(342);
				idName();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(344);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__24) {
					{
					setState(343);
					match(T__24);
					}
				}

				setState(346);
				match(VARIABLE);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(347);
				match(STRING);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(348);
				match(NUMBER);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(349);
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
		enterRule(_localctx, 58, RULE_operacionLogica);
		try {
			setState(367);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OR:
				_localctx = new OpOrContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(352);
				match(OR);
				setState(353);
				match(T__4);
				setState(354);
				listaCondiciones();
				setState(355);
				match(T__5);
				}
				break;
			case AND:
				_localctx = new OpAndContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(357);
				match(AND);
				setState(358);
				match(T__4);
				setState(359);
				listaCondiciones();
				setState(360);
				match(T__5);
				}
				break;
			case NOT:
				_localctx = new OpNotContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(362);
				match(NOT);
				setState(363);
				match(T__4);
				setState(364);
				condicion();
				setState(365);
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
		enterRule(_localctx, 60, RULE_listaConsecuencias);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(376);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3298606186496L) != 0)) {
				{
				{
				setState(369);
				consecuencia();
				setState(370);
				match(T__2);
				setState(372);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
				case 1:
					{
					setState(371);
					comentarioSimple();
					}
					break;
				}
				}
				}
				setState(378);
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
		public ConsecuenciaRuleContext consecuenciaRule() {
			return getRuleContext(ConsecuenciaRuleContext.class,0);
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
		enterRule(_localctx, 62, RULE_consecuencia);
		int _la;
		try {
			setState(387);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(379);
				asignacion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(380);
				funcion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(381);
				borrado();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(382);
				predicado();
				setState(384);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__12) {
					{
					setState(383);
					bloqueValores();
					}
				}

				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(386);
				consecuenciaRule();
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
	public static class ConsecuenciaRuleContext extends ParserRuleContext {
		public IdNameContext idName() {
			return getRuleContext(IdNameContext.class,0);
		}
		public ListaArgsPredicadoContext listaArgsPredicado() {
			return getRuleContext(ListaArgsPredicadoContext.class,0);
		}
		public ConsecuenciaRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_consecuenciaRule; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterConsecuenciaRule(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitConsecuenciaRule(this);
		}
	}

	public final ConsecuenciaRuleContext consecuenciaRule() throws RecognitionException {
		ConsecuenciaRuleContext _localctx = new ConsecuenciaRuleContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_consecuenciaRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(389);
			match(T__21);
			setState(390);
			idName();
			setState(391);
			match(T__4);
			setState(392);
			listaArgsPredicado();
			setState(393);
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
		enterRule(_localctx, 66, RULE_asignacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(395);
			operandoIzq();
			setState(396);
			_la = _input.LA(1);
			if ( !(_la==OpIgual || _la==OpAsign) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(397);
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
		enterRule(_localctx, 68, RULE_operandoIzq);
		try {
			setState(403);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(399);
				match(VARIABLE);
				setState(400);
				match(T__22);
				setState(401);
				idName();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(402);
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
	public static class OperandoDrcContext extends ParserRuleContext {
		public FuncionContext funcion() {
			return getRuleContext(FuncionContext.class,0);
		}
		public OperandoIzqContext operandoIzq() {
			return getRuleContext(OperandoIzqContext.class,0);
		}
		public TerminalNode NUMBER() { return getToken(gramaticaParser.NUMBER, 0); }
		public TerminalNode VARIABLE() { return getToken(gramaticaParser.VARIABLE, 0); }
		public TerminalNode STRING() { return getToken(gramaticaParser.STRING, 0); }
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
		enterRule(_localctx, 70, RULE_operandoDrc);
		try {
			setState(410);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(405);
				funcion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(406);
				operandoIzq();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(407);
				match(NUMBER);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(408);
				match(VARIABLE);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(409);
				match(STRING);
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
		enterRule(_localctx, 72, RULE_borrado);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(412);
			match(T__25);
			setState(413);
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
		enterRule(_localctx, 74, RULE_inicializacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(415);
			match(T__26);
			}
			setState(416);
			idName();
			setState(417);
			match(T__4);
			setState(418);
			argLit();
			setState(423);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(419);
				match(T__6);
				setState(420);
				argLit();
				}
				}
				setState(425);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(426);
			match(T__5);
			setState(428);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(427);
				bloqueValores();
				}
			}

			setState(430);
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
		enterRule(_localctx, 76, RULE_bloqueValores);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(432);
			match(T__12);
			setState(434);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INDIVIDUO || _la==VARIABLE) {
				{
				setState(433);
				listaParejasValor();
				}
			}

			setState(436);
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
		enterRule(_localctx, 78, RULE_listaParejasValor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(438);
			parejaValor();
			setState(443);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(439);
				match(T__6);
				setState(440);
				parejaValor();
				}
				}
				setState(445);
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
		enterRule(_localctx, 80, RULE_parejaValor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(446);
			idName();
			setState(447);
			match(OpIgual);
			setState(453);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,43,_ctx) ) {
			case 1:
				{
				setState(448);
				valor();
				}
				break;
			case 2:
				{
				setState(449);
				match(VARIABLE);
				setState(450);
				match(T__22);
				setState(451);
				idName();
				}
				break;
			case 3:
				{
				setState(452);
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
		enterRule(_localctx, 82, RULE_valor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(455);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 962072674304L) != 0)) ) {
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
		enterRule(_localctx, 84, RULE_argLit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(457);
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
		enterRule(_localctx, 86, RULE_ejecucion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(459);
			match(T__27);
			setState(460);
			idName();
			setState(461);
			match(T__4);
			setState(463);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STRING || _la==NUMBER) {
				{
				setState(462);
				listaArgLit();
				}
			}

			setState(465);
			match(T__5);
			setState(466);
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
		enterRule(_localctx, 88, RULE_listaArgLit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(468);
			argLit();
			setState(473);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(469);
				match(T__6);
				setState(470);
				argLit();
				}
				}
				setState(475);
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
		enterRule(_localctx, 90, RULE_comentarioSimple);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(476);
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
		enterRule(_localctx, 92, RULE_comentarioMultilineo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(478);
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
		enterRule(_localctx, 94, RULE_idName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(480);
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
		"\u0004\u0001*\u01e3\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007,\u0002"+
		"-\u0007-\u0002.\u0007.\u0002/\u0007/\u0001\u0000\u0005\u0000b\b\u0000"+
		"\n\u0000\f\u0000e\t\u0000\u0001\u0000\u0005\u0000h\b\u0000\n\u0000\f\u0000"+
		"k\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002{\b\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0003\u0003\u0080\b\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0003\u0003\u0085\b\u0003\u0003\u0003\u0087\b\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u008d\b\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005\u0094"+
		"\b\u0005\n\u0005\f\u0005\u0097\t\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0003"+
		"\b\u00a3\b\b\u0001\b\u0001\b\u0001\b\u0003\b\u00a8\b\b\u0001\b\u0003\b"+
		"\u00ab\b\b\u0001\t\u0001\t\u0003\t\u00af\b\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0005\n\u00b6\b\n\n\n\f\n\u00b9\t\n\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0005\u000b\u00be\b\u000b\n\u000b\f\u000b\u00c1\t\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0003\f\u00c6\b\f\u0001\r\u0001\r\u0001\r\u0001\r\u0003"+
		"\r\u00cc\b\r\u0001\r\u0001\r\u0001\r\u0003\r\u00d1\b\r\u0001\r\u0001\r"+
		"\u0001\r\u0001\r\u0001\r\u0005\r\u00d8\b\r\n\r\f\r\u00db\t\r\u0001\u000e"+
		"\u0003\u000e\u00de\b\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0003\u000e\u00e4\b\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00ee\b\u000f"+
		"\n\u000f\f\u000f\u00f1\t\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0003"+
		"\u0010\u00f6\b\u0010\u0005\u0010\u00f8\b\u0010\n\u0010\f\u0010\u00fb\t"+
		"\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0003\u0011\u0103\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0003\u0014\u0116\b\u0014\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0005"+
		"\u0016\u0120\b\u0016\n\u0016\f\u0016\u0123\t\u0016\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0003\u0017\u012f\b\u0017\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0003\u0019\u0141\b\u0019\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0003\u001a\u0148\b\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0005\u001b\u014f\b\u001b"+
		"\n\u001b\f\u001b\u0152\t\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0003\u001c\u0159\b\u001c\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0003\u001c\u015f\b\u001c\u0001\u001d\u0001\u001d\u0001"+
		"\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001"+
		"\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001"+
		"\u001d\u0003\u001d\u0170\b\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0003"+
		"\u001e\u0175\b\u001e\u0005\u001e\u0177\b\u001e\n\u001e\f\u001e\u017a\t"+
		"\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0003"+
		"\u001f\u0181\b\u001f\u0001\u001f\u0003\u001f\u0184\b\u001f\u0001 \u0001"+
		" \u0001 \u0001 \u0001 \u0001 \u0001!\u0001!\u0001!\u0001!\u0001\"\u0001"+
		"\"\u0001\"\u0001\"\u0003\"\u0194\b\"\u0001#\u0001#\u0001#\u0001#\u0001"+
		"#\u0003#\u019b\b#\u0001$\u0001$\u0001$\u0001%\u0001%\u0001%\u0001%\u0001"+
		"%\u0001%\u0005%\u01a6\b%\n%\f%\u01a9\t%\u0001%\u0001%\u0003%\u01ad\b%"+
		"\u0001%\u0001%\u0001&\u0001&\u0003&\u01b3\b&\u0001&\u0001&\u0001\'\u0001"+
		"\'\u0001\'\u0005\'\u01ba\b\'\n\'\f\'\u01bd\t\'\u0001(\u0001(\u0001(\u0001"+
		"(\u0001(\u0001(\u0001(\u0003(\u01c6\b(\u0001)\u0001)\u0001*\u0001*\u0001"+
		"+\u0001+\u0001+\u0001+\u0003+\u01d0\b+\u0001+\u0001+\u0001+\u0001,\u0001"+
		",\u0001,\u0005,\u01d8\b,\n,\f,\u01db\t,\u0001-\u0001-\u0001.\u0001.\u0001"+
		"/\u0001/\u0001/\u0000\u00000\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJLNPR"+
		"TVXZ\\^\u0000\u0007\u0001\u0000\t\u000b\u0001\u0000\u000f\u0010\u0001"+
		"\u0000\u0013\u0014\u0001\u0000!\"\u0001\u0000%\'\u0001\u0000&\'\u0001"+
		"\u0000()\u0203\u0000c\u0001\u0000\u0000\u0000\u0002n\u0001\u0000\u0000"+
		"\u0000\u0004z\u0001\u0000\u0000\u0000\u0006\u0086\u0001\u0000\u0000\u0000"+
		"\b\u0088\u0001\u0000\u0000\u0000\n\u0090\u0001\u0000\u0000\u0000\f\u0098"+
		"\u0001\u0000\u0000\u0000\u000e\u009c\u0001\u0000\u0000\u0000\u0010\u009e"+
		"\u0001\u0000\u0000\u0000\u0012\u00ac\u0001\u0000\u0000\u0000\u0014\u00b2"+
		"\u0001\u0000\u0000\u0000\u0016\u00ba\u0001\u0000\u0000\u0000\u0018\u00c2"+
		"\u0001\u0000\u0000\u0000\u001a\u00c7\u0001\u0000\u0000\u0000\u001c\u00dd"+
		"\u0001\u0000\u0000\u0000\u001e\u00ea\u0001\u0000\u0000\u0000 \u00f9\u0001"+
		"\u0000\u0000\u0000\"\u0102\u0001\u0000\u0000\u0000$\u0104\u0001\u0000"+
		"\u0000\u0000&\u010a\u0001\u0000\u0000\u0000(\u010c\u0001\u0000\u0000\u0000"+
		"*\u0117\u0001\u0000\u0000\u0000,\u011c\u0001\u0000\u0000\u0000.\u012e"+
		"\u0001\u0000\u0000\u00000\u0130\u0001\u0000\u0000\u00002\u0140\u0001\u0000"+
		"\u0000\u00004\u0142\u0001\u0000\u0000\u00006\u014b\u0001\u0000\u0000\u0000"+
		"8\u015e\u0001\u0000\u0000\u0000:\u016f\u0001\u0000\u0000\u0000<\u0178"+
		"\u0001\u0000\u0000\u0000>\u0183\u0001\u0000\u0000\u0000@\u0185\u0001\u0000"+
		"\u0000\u0000B\u018b\u0001\u0000\u0000\u0000D\u0193\u0001\u0000\u0000\u0000"+
		"F\u019a\u0001\u0000\u0000\u0000H\u019c\u0001\u0000\u0000\u0000J\u019f"+
		"\u0001\u0000\u0000\u0000L\u01b0\u0001\u0000\u0000\u0000N\u01b6\u0001\u0000"+
		"\u0000\u0000P\u01be\u0001\u0000\u0000\u0000R\u01c7\u0001\u0000\u0000\u0000"+
		"T\u01c9\u0001\u0000\u0000\u0000V\u01cb\u0001\u0000\u0000\u0000X\u01d4"+
		"\u0001\u0000\u0000\u0000Z\u01dc\u0001\u0000\u0000\u0000\\\u01de\u0001"+
		"\u0000\u0000\u0000^\u01e0\u0001\u0000\u0000\u0000`b\u0003\u0002\u0001"+
		"\u0000a`\u0001\u0000\u0000\u0000be\u0001\u0000\u0000\u0000ca\u0001\u0000"+
		"\u0000\u0000cd\u0001\u0000\u0000\u0000di\u0001\u0000\u0000\u0000ec\u0001"+
		"\u0000\u0000\u0000fh\u0003\u0004\u0002\u0000gf\u0001\u0000\u0000\u0000"+
		"hk\u0001\u0000\u0000\u0000ig\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000"+
		"\u0000jl\u0001\u0000\u0000\u0000ki\u0001\u0000\u0000\u0000lm\u0005\u0000"+
		"\u0000\u0001m\u0001\u0001\u0000\u0000\u0000no\u0005\u0001\u0000\u0000"+
		"op\u0003^/\u0000pq\u0005\u0002\u0000\u0000qr\u0003^/\u0000rs\u0005\u0003"+
		"\u0000\u0000s\u0003\u0001\u0000\u0000\u0000t{\u0003\u0006\u0003\u0000"+
		"u{\u0003\u001a\r\u0000v{\u0003J%\u0000w{\u0003V+\u0000x{\u0003Z-\u0000"+
		"y{\u0003\\.\u0000zt\u0001\u0000\u0000\u0000zu\u0001\u0000\u0000\u0000"+
		"zv\u0001\u0000\u0000\u0000zw\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000"+
		"\u0000zy\u0001\u0000\u0000\u0000{\u0005\u0001\u0000\u0000\u0000|}\u0003"+
		"\b\u0004\u0000}\u007f\u0005\u0003\u0000\u0000~\u0080\u0003Z-\u0000\u007f"+
		"~\u0001\u0000\u0000\u0000\u007f\u0080\u0001\u0000\u0000\u0000\u0080\u0087"+
		"\u0001\u0000\u0000\u0000\u0081\u0082\u0003\u0010\b\u0000\u0082\u0084\u0005"+
		"\u0003\u0000\u0000\u0083\u0085\u0003Z-\u0000\u0084\u0083\u0001\u0000\u0000"+
		"\u0000\u0084\u0085\u0001\u0000\u0000\u0000\u0085\u0087\u0001\u0000\u0000"+
		"\u0000\u0086|\u0001\u0000\u0000\u0000\u0086\u0081\u0001\u0000\u0000\u0000"+
		"\u0087\u0007\u0001\u0000\u0000\u0000\u0088\u0089\u0005\u0004\u0000\u0000"+
		"\u0089\u008a\u0003^/\u0000\u008a\u008c\u0005\u0005\u0000\u0000\u008b\u008d"+
		"\u0003\n\u0005\u0000\u008c\u008b\u0001\u0000\u0000\u0000\u008c\u008d\u0001"+
		"\u0000\u0000\u0000\u008d\u008e\u0001\u0000\u0000\u0000\u008e\u008f\u0005"+
		"\u0006\u0000\u0000\u008f\t\u0001\u0000\u0000\u0000\u0090\u0095\u0003\f"+
		"\u0006\u0000\u0091\u0092\u0005\u0007\u0000\u0000\u0092\u0094\u0003\f\u0006"+
		"\u0000\u0093\u0091\u0001\u0000\u0000\u0000\u0094\u0097\u0001\u0000\u0000"+
		"\u0000\u0095\u0093\u0001\u0000\u0000\u0000\u0095\u0096\u0001\u0000\u0000"+
		"\u0000\u0096\u000b\u0001\u0000\u0000\u0000\u0097\u0095\u0001\u0000\u0000"+
		"\u0000\u0098\u0099\u0003^/\u0000\u0099\u009a\u0005\b\u0000\u0000\u009a"+
		"\u009b\u0003\u000e\u0007\u0000\u009b\r\u0001\u0000\u0000\u0000\u009c\u009d"+
		"\u0007\u0000\u0000\u0000\u009d\u000f\u0001\u0000\u0000\u0000\u009e\u009f"+
		"\u0005\f\u0000\u0000\u009f\u00a0\u0003^/\u0000\u00a0\u00a2\u0005\u0005"+
		"\u0000\u0000\u00a1\u00a3\u0003\u0014\n\u0000\u00a2\u00a1\u0001\u0000\u0000"+
		"\u0000\u00a2\u00a3\u0001\u0000\u0000\u0000\u00a3\u00a4\u0001\u0000\u0000"+
		"\u0000\u00a4\u00a7\u0005\u0006\u0000\u0000\u00a5\u00a6\u0005\b\u0000\u0000"+
		"\u00a6\u00a8\u0003^/\u0000\u00a7\u00a5\u0001\u0000\u0000\u0000\u00a7\u00a8"+
		"\u0001\u0000\u0000\u0000\u00a8\u00aa\u0001\u0000\u0000\u0000\u00a9\u00ab"+
		"\u0003\u0012\t\u0000\u00aa\u00a9\u0001\u0000\u0000\u0000\u00aa\u00ab\u0001"+
		"\u0000\u0000\u0000\u00ab\u0011\u0001\u0000\u0000\u0000\u00ac\u00ae\u0005"+
		"\r\u0000\u0000\u00ad\u00af\u0003\u0016\u000b\u0000\u00ae\u00ad\u0001\u0000"+
		"\u0000\u0000\u00ae\u00af\u0001\u0000\u0000\u0000\u00af\u00b0\u0001\u0000"+
		"\u0000\u0000\u00b0\u00b1\u0005\u000e\u0000\u0000\u00b1\u0013\u0001\u0000"+
		"\u0000\u0000\u00b2\u00b7\u0003^/\u0000\u00b3\u00b4\u0005\u0007\u0000\u0000"+
		"\u00b4\u00b6\u0003^/\u0000\u00b5\u00b3\u0001\u0000\u0000\u0000\u00b6\u00b9"+
		"\u0001\u0000\u0000\u0000\u00b7\u00b5\u0001\u0000\u0000\u0000\u00b7\u00b8"+
		"\u0001\u0000\u0000\u0000\u00b8\u0015\u0001\u0000\u0000\u0000\u00b9\u00b7"+
		"\u0001\u0000\u0000\u0000\u00ba\u00bf\u0003\u0018\f\u0000\u00bb\u00bc\u0005"+
		"\u0007\u0000\u0000\u00bc\u00be\u0003\u0018\f\u0000\u00bd\u00bb\u0001\u0000"+
		"\u0000\u0000\u00be\u00c1\u0001\u0000\u0000\u0000\u00bf\u00bd\u0001\u0000"+
		"\u0000\u0000\u00bf\u00c0\u0001\u0000\u0000\u0000\u00c0\u0017\u0001\u0000"+
		"\u0000\u0000\u00c1\u00bf\u0001\u0000\u0000\u0000\u00c2\u00c5\u0003^/\u0000"+
		"\u00c3\u00c4\u0005!\u0000\u0000\u00c4\u00c6\u0003R)\u0000\u00c5\u00c3"+
		"\u0001\u0000\u0000\u0000\u00c5\u00c6\u0001\u0000\u0000\u0000\u00c6\u0019"+
		"\u0001\u0000\u0000\u0000\u00c7\u00c8\u0007\u0001\u0000\u0000\u00c8\u00c9"+
		"\u0003^/\u0000\u00c9\u00cb\u0005\u0005\u0000\u0000\u00ca\u00cc\u0003\u001e"+
		"\u000f\u0000\u00cb\u00ca\u0001\u0000\u0000\u0000\u00cb\u00cc\u0001\u0000"+
		"\u0000\u0000\u00cc\u00cd\u0001\u0000\u0000\u0000\u00cd\u00ce\u0005\u0006"+
		"\u0000\u0000\u00ce\u00d0\u0005\b\u0000\u0000\u00cf\u00d1\u0003\\.\u0000"+
		"\u00d0\u00cf\u0001\u0000\u0000\u0000\u00d0\u00d1\u0001\u0000\u0000\u0000"+
		"\u00d1\u00d2\u0001\u0000\u0000\u0000\u00d2\u00d3\u0005\u0011\u0000\u0000"+
		"\u00d3\u00d4\u0003 \u0010\u0000\u00d4\u00d5\u0005\u0012\u0000\u0000\u00d5"+
		"\u00d9\u0003<\u001e\u0000\u00d6\u00d8\u0003\u001c\u000e\u0000\u00d7\u00d6"+
		"\u0001\u0000\u0000\u0000\u00d8\u00db\u0001\u0000\u0000\u0000\u00d9\u00d7"+
		"\u0001\u0000\u0000\u0000\u00d9\u00da\u0001\u0000\u0000\u0000\u00da\u001b"+
		"\u0001\u0000\u0000\u0000\u00db\u00d9\u0001\u0000\u0000\u0000\u00dc\u00de"+
		"\u0007\u0002\u0000\u0000\u00dd\u00dc\u0001\u0000\u0000\u0000\u00dd\u00de"+
		"\u0001\u0000\u0000\u0000\u00de\u00df\u0001\u0000\u0000\u0000\u00df\u00e0"+
		"\u0005\u0015\u0000\u0000\u00e0\u00e1\u0003^/\u0000\u00e1\u00e3\u0005\b"+
		"\u0000\u0000\u00e2\u00e4\u0003\\.\u0000\u00e3\u00e2\u0001\u0000\u0000"+
		"\u0000\u00e3\u00e4\u0001\u0000\u0000\u0000\u00e4\u00e5\u0001\u0000\u0000"+
		"\u0000\u00e5\u00e6\u0005\u0011\u0000\u0000\u00e6\u00e7\u0003 \u0010\u0000"+
		"\u00e7\u00e8\u0005\u0012\u0000\u0000\u00e8\u00e9\u0003<\u001e\u0000\u00e9"+
		"\u001d\u0001\u0000\u0000\u0000\u00ea\u00ef\u0003^/\u0000\u00eb\u00ec\u0005"+
		"\u0007\u0000\u0000\u00ec\u00ee\u0003^/\u0000\u00ed\u00eb\u0001\u0000\u0000"+
		"\u0000\u00ee\u00f1\u0001\u0000\u0000\u0000\u00ef\u00ed\u0001\u0000\u0000"+
		"\u0000\u00ef\u00f0\u0001\u0000\u0000\u0000\u00f0\u001f\u0001\u0000\u0000"+
		"\u0000\u00f1\u00ef\u0001\u0000\u0000\u0000\u00f2\u00f3\u0003\"\u0011\u0000"+
		"\u00f3\u00f5\u0005\u0003\u0000\u0000\u00f4\u00f6\u0003Z-\u0000\u00f5\u00f4"+
		"\u0001\u0000\u0000\u0000\u00f5\u00f6\u0001\u0000\u0000\u0000\u00f6\u00f8"+
		"\u0001\u0000\u0000\u0000\u00f7\u00f2\u0001\u0000\u0000\u0000\u00f8\u00fb"+
		"\u0001\u0000\u0000\u0000\u00f9\u00f7\u0001\u0000\u0000\u0000\u00f9\u00fa"+
		"\u0001\u0000\u0000\u0000\u00fa!\u0001\u0000\u0000\u0000\u00fb\u00f9\u0001"+
		"\u0000\u0000\u0000\u00fc\u0103\u0003*\u0015\u0000\u00fd\u0103\u00030\u0018"+
		"\u0000\u00fe\u0103\u0003:\u001d\u0000\u00ff\u0103\u0003(\u0014\u0000\u0100"+
		"\u0103\u0003&\u0013\u0000\u0101\u0103\u0003$\u0012\u0000\u0102\u00fc\u0001"+
		"\u0000\u0000\u0000\u0102\u00fd\u0001\u0000\u0000\u0000\u0102\u00fe\u0001"+
		"\u0000\u0000\u0000\u0102\u00ff\u0001\u0000\u0000\u0000\u0102\u0100\u0001"+
		"\u0000\u0000\u0000\u0102\u0101\u0001\u0000\u0000\u0000\u0103#\u0001\u0000"+
		"\u0000\u0000\u0104\u0105\u0005\u0016\u0000\u0000\u0105\u0106\u0003^/\u0000"+
		"\u0106\u0107\u0005\u0005\u0000\u0000\u0107\u0108\u0003,\u0016\u0000\u0108"+
		"\u0109\u0005\u0006\u0000\u0000\u0109%\u0001\u0000\u0000\u0000\u010a\u010b"+
		"\u00034\u001a\u0000\u010b\'\u0001\u0000\u0000\u0000\u010c\u010d\u0005"+
		")\u0000\u0000\u010d\u0115\u0005!\u0000\u0000\u010e\u0116\u0003*\u0015"+
		"\u0000\u010f\u0116\u00034\u001a\u0000\u0110\u0116\u0003R)\u0000\u0111"+
		"\u0112\u0005)\u0000\u0000\u0112\u0113\u0005\u0017\u0000\u0000\u0113\u0116"+
		"\u0003^/\u0000\u0114\u0116\u0005)\u0000\u0000\u0115\u010e\u0001\u0000"+
		"\u0000\u0000\u0115\u010f\u0001\u0000\u0000\u0000\u0115\u0110\u0001\u0000"+
		"\u0000\u0000\u0115\u0111\u0001\u0000\u0000\u0000\u0115\u0114\u0001\u0000"+
		"\u0000\u0000\u0116)\u0001\u0000\u0000\u0000\u0117\u0118\u0003^/\u0000"+
		"\u0118\u0119\u0005\u0005\u0000\u0000\u0119\u011a\u0003,\u0016\u0000\u011a"+
		"\u011b\u0005\u0006\u0000\u0000\u011b+\u0001\u0000\u0000\u0000\u011c\u0121"+
		"\u0003.\u0017\u0000\u011d\u011e\u0005\u0007\u0000\u0000\u011e\u0120\u0003"+
		".\u0017\u0000\u011f\u011d\u0001\u0000\u0000\u0000\u0120\u0123\u0001\u0000"+
		"\u0000\u0000\u0121\u011f\u0001\u0000\u0000\u0000\u0121\u0122\u0001\u0000"+
		"\u0000\u0000\u0122-\u0001\u0000\u0000\u0000\u0123\u0121\u0001\u0000\u0000"+
		"\u0000\u0124\u012f\u0005(\u0000\u0000\u0125\u012f\u00034\u001a\u0000\u0126"+
		"\u0127\u0005)\u0000\u0000\u0127\u0128\u0005\u0017\u0000\u0000\u0128\u012f"+
		"\u0003^/\u0000\u0129\u012f\u0005)\u0000\u0000\u012a\u012f\u0005&\u0000"+
		"\u0000\u012b\u012f\u0005\'\u0000\u0000\u012c\u012f\u0005%\u0000\u0000"+
		"\u012d\u012f\u0005\u0018\u0000\u0000\u012e\u0124\u0001\u0000\u0000\u0000"+
		"\u012e\u0125\u0001\u0000\u0000\u0000\u012e\u0126\u0001\u0000\u0000\u0000"+
		"\u012e\u0129\u0001\u0000\u0000\u0000\u012e\u012a\u0001\u0000\u0000\u0000"+
		"\u012e\u012b\u0001\u0000\u0000\u0000\u012e\u012c\u0001\u0000\u0000\u0000"+
		"\u012e\u012d\u0001\u0000\u0000\u0000\u012f/\u0001\u0000\u0000\u0000\u0130"+
		"\u0131\u00032\u0019\u0000\u0131\u0132\u0005\u001d\u0000\u0000\u0132\u0133"+
		"\u00032\u0019\u0000\u01331\u0001\u0000\u0000\u0000\u0134\u0141\u00034"+
		"\u001a\u0000\u0135\u0136\u0005)\u0000\u0000\u0136\u0137\u0005\u0017\u0000"+
		"\u0000\u0137\u0141\u0003^/\u0000\u0138\u0139\u0005(\u0000\u0000\u0139"+
		"\u013a\u0005\u0017\u0000\u0000\u013a\u0141\u0003^/\u0000\u013b\u0141\u0005"+
		"(\u0000\u0000\u013c\u0141\u0005)\u0000\u0000\u013d\u0141\u0005\'\u0000"+
		"\u0000\u013e\u0141\u0005&\u0000\u0000\u013f\u0141\u0005%\u0000\u0000\u0140"+
		"\u0134\u0001\u0000\u0000\u0000\u0140\u0135\u0001\u0000\u0000\u0000\u0140"+
		"\u0138\u0001\u0000\u0000\u0000\u0140\u013b\u0001\u0000\u0000\u0000\u0140"+
		"\u013c\u0001\u0000\u0000\u0000\u0140\u013d\u0001\u0000\u0000\u0000\u0140"+
		"\u013e\u0001\u0000\u0000\u0000\u0140\u013f\u0001\u0000\u0000\u0000\u0141"+
		"3\u0001\u0000\u0000\u0000\u0142\u0143\u0003^/\u0000\u0143\u0144\u0005"+
		"\u0017\u0000\u0000\u0144\u0145\u0003^/\u0000\u0145\u0147\u0005\u0005\u0000"+
		"\u0000\u0146\u0148\u00036\u001b\u0000\u0147\u0146\u0001\u0000\u0000\u0000"+
		"\u0147\u0148\u0001\u0000\u0000\u0000\u0148\u0149\u0001\u0000\u0000\u0000"+
		"\u0149\u014a\u0005\u0006\u0000\u0000\u014a5\u0001\u0000\u0000\u0000\u014b"+
		"\u0150\u00038\u001c\u0000\u014c\u014d\u0005\u0007\u0000\u0000\u014d\u014f"+
		"\u00038\u001c\u0000\u014e\u014c\u0001\u0000\u0000\u0000\u014f\u0152\u0001"+
		"\u0000\u0000\u0000\u0150\u014e\u0001\u0000\u0000\u0000\u0150\u0151\u0001"+
		"\u0000\u0000\u0000\u01517\u0001\u0000\u0000\u0000\u0152\u0150\u0001\u0000"+
		"\u0000\u0000\u0153\u015f\u0005(\u0000\u0000\u0154\u0155\u0005)\u0000\u0000"+
		"\u0155\u0156\u0005\u0017\u0000\u0000\u0156\u015f\u0003^/\u0000\u0157\u0159"+
		"\u0005\u0019\u0000\u0000\u0158\u0157\u0001\u0000\u0000\u0000\u0158\u0159"+
		"\u0001\u0000\u0000\u0000\u0159\u015a\u0001\u0000\u0000\u0000\u015a\u015f"+
		"\u0005)\u0000\u0000\u015b\u015f\u0005&\u0000\u0000\u015c\u015f\u0005\'"+
		"\u0000\u0000\u015d\u015f\u0005%\u0000\u0000\u015e\u0153\u0001\u0000\u0000"+
		"\u0000\u015e\u0154\u0001\u0000\u0000\u0000\u015e\u0158\u0001\u0000\u0000"+
		"\u0000\u015e\u015b\u0001\u0000\u0000\u0000\u015e\u015c\u0001\u0000\u0000"+
		"\u0000\u015e\u015d\u0001\u0000\u0000\u0000\u015f9\u0001\u0000\u0000\u0000"+
		"\u0160\u0161\u0005\u001e\u0000\u0000\u0161\u0162\u0005\u0005\u0000\u0000"+
		"\u0162\u0163\u0003 \u0010\u0000\u0163\u0164\u0005\u0006\u0000\u0000\u0164"+
		"\u0170\u0001\u0000\u0000\u0000\u0165\u0166\u0005\u001f\u0000\u0000\u0166"+
		"\u0167\u0005\u0005\u0000\u0000\u0167\u0168\u0003 \u0010\u0000\u0168\u0169"+
		"\u0005\u0006\u0000\u0000\u0169\u0170\u0001\u0000\u0000\u0000\u016a\u016b"+
		"\u0005 \u0000\u0000\u016b\u016c\u0005\u0005\u0000\u0000\u016c\u016d\u0003"+
		"\"\u0011\u0000\u016d\u016e\u0005\u0006\u0000\u0000\u016e\u0170\u0001\u0000"+
		"\u0000\u0000\u016f\u0160\u0001\u0000\u0000\u0000\u016f\u0165\u0001\u0000"+
		"\u0000\u0000\u016f\u016a\u0001\u0000\u0000\u0000\u0170;\u0001\u0000\u0000"+
		"\u0000\u0171\u0172\u0003>\u001f\u0000\u0172\u0174\u0005\u0003\u0000\u0000"+
		"\u0173\u0175\u0003Z-\u0000\u0174\u0173\u0001\u0000\u0000\u0000\u0174\u0175"+
		"\u0001\u0000\u0000\u0000\u0175\u0177\u0001\u0000\u0000\u0000\u0176\u0171"+
		"\u0001\u0000\u0000\u0000\u0177\u017a\u0001\u0000\u0000\u0000\u0178\u0176"+
		"\u0001\u0000\u0000\u0000\u0178\u0179\u0001\u0000\u0000\u0000\u0179=\u0001"+
		"\u0000\u0000\u0000\u017a\u0178\u0001\u0000\u0000\u0000\u017b\u0184\u0003"+
		"B!\u0000\u017c\u0184\u00034\u001a\u0000\u017d\u0184\u0003H$\u0000\u017e"+
		"\u0180\u0003*\u0015\u0000\u017f\u0181\u0003L&\u0000\u0180\u017f\u0001"+
		"\u0000\u0000\u0000\u0180\u0181\u0001\u0000\u0000\u0000\u0181\u0184\u0001"+
		"\u0000\u0000\u0000\u0182\u0184\u0003@ \u0000\u0183\u017b\u0001\u0000\u0000"+
		"\u0000\u0183\u017c\u0001\u0000\u0000\u0000\u0183\u017d\u0001\u0000\u0000"+
		"\u0000\u0183\u017e\u0001\u0000\u0000\u0000\u0183\u0182\u0001\u0000\u0000"+
		"\u0000\u0184?\u0001\u0000\u0000\u0000\u0185\u0186\u0005\u0016\u0000\u0000"+
		"\u0186\u0187\u0003^/\u0000\u0187\u0188\u0005\u0005\u0000\u0000\u0188\u0189"+
		"\u0003,\u0016\u0000\u0189\u018a\u0005\u0006\u0000\u0000\u018aA\u0001\u0000"+
		"\u0000\u0000\u018b\u018c\u0003D\"\u0000\u018c\u018d\u0007\u0003\u0000"+
		"\u0000\u018d\u018e\u0003F#\u0000\u018eC\u0001\u0000\u0000\u0000\u018f"+
		"\u0190\u0005)\u0000\u0000\u0190\u0191\u0005\u0017\u0000\u0000\u0191\u0194"+
		"\u0003^/\u0000\u0192\u0194\u0005)\u0000\u0000\u0193\u018f\u0001\u0000"+
		"\u0000\u0000\u0193\u0192\u0001\u0000\u0000\u0000\u0194E\u0001\u0000\u0000"+
		"\u0000\u0195\u019b\u00034\u001a\u0000\u0196\u019b\u0003D\"\u0000\u0197"+
		"\u019b\u0005\'\u0000\u0000\u0198\u019b\u0005)\u0000\u0000\u0199\u019b"+
		"\u0005&\u0000\u0000\u019a\u0195\u0001\u0000\u0000\u0000\u019a\u0196\u0001"+
		"\u0000\u0000\u0000\u019a\u0197\u0001\u0000\u0000\u0000\u019a\u0198\u0001"+
		"\u0000\u0000\u0000\u019a\u0199\u0001\u0000\u0000\u0000\u019bG\u0001\u0000"+
		"\u0000\u0000\u019c\u019d\u0005\u001a\u0000\u0000\u019d\u019e\u0003*\u0015"+
		"\u0000\u019eI\u0001\u0000\u0000\u0000\u019f\u01a0\u0005\u001b\u0000\u0000"+
		"\u01a0\u01a1\u0003^/\u0000\u01a1\u01a2\u0005\u0005\u0000\u0000\u01a2\u01a7"+
		"\u0003T*\u0000\u01a3\u01a4\u0005\u0007\u0000\u0000\u01a4\u01a6\u0003T"+
		"*\u0000\u01a5\u01a3\u0001\u0000\u0000\u0000\u01a6\u01a9\u0001\u0000\u0000"+
		"\u0000\u01a7\u01a5\u0001\u0000\u0000\u0000\u01a7\u01a8\u0001\u0000\u0000"+
		"\u0000\u01a8\u01aa\u0001\u0000\u0000\u0000\u01a9\u01a7\u0001\u0000\u0000"+
		"\u0000\u01aa\u01ac\u0005\u0006\u0000\u0000\u01ab\u01ad\u0003L&\u0000\u01ac"+
		"\u01ab\u0001\u0000\u0000\u0000\u01ac\u01ad\u0001\u0000\u0000\u0000\u01ad"+
		"\u01ae\u0001\u0000\u0000\u0000\u01ae\u01af\u0005\u0003\u0000\u0000\u01af"+
		"K\u0001\u0000\u0000\u0000\u01b0\u01b2\u0005\r\u0000\u0000\u01b1\u01b3"+
		"\u0003N\'\u0000\u01b2\u01b1\u0001\u0000\u0000\u0000\u01b2\u01b3\u0001"+
		"\u0000\u0000\u0000\u01b3\u01b4\u0001\u0000\u0000\u0000\u01b4\u01b5\u0005"+
		"\u000e\u0000\u0000\u01b5M\u0001\u0000\u0000\u0000\u01b6\u01bb\u0003P("+
		"\u0000\u01b7\u01b8\u0005\u0007\u0000\u0000\u01b8\u01ba\u0003P(\u0000\u01b9"+
		"\u01b7\u0001\u0000\u0000\u0000\u01ba\u01bd\u0001\u0000\u0000\u0000\u01bb"+
		"\u01b9\u0001\u0000\u0000\u0000\u01bb\u01bc\u0001\u0000\u0000\u0000\u01bc"+
		"O\u0001\u0000\u0000\u0000\u01bd\u01bb\u0001\u0000\u0000\u0000\u01be\u01bf"+
		"\u0003^/\u0000\u01bf\u01c5\u0005!\u0000\u0000\u01c0\u01c6\u0003R)\u0000"+
		"\u01c1\u01c2\u0005)\u0000\u0000\u01c2\u01c3\u0005\u0017\u0000\u0000\u01c3"+
		"\u01c6\u0003^/\u0000\u01c4\u01c6\u0005)\u0000\u0000\u01c5\u01c0\u0001"+
		"\u0000\u0000\u0000\u01c5\u01c1\u0001\u0000\u0000\u0000\u01c5\u01c4\u0001"+
		"\u0000\u0000\u0000\u01c6Q\u0001\u0000\u0000\u0000\u01c7\u01c8\u0007\u0004"+
		"\u0000\u0000\u01c8S\u0001\u0000\u0000\u0000\u01c9\u01ca\u0007\u0005\u0000"+
		"\u0000\u01caU\u0001\u0000\u0000\u0000\u01cb\u01cc\u0005\u001c\u0000\u0000"+
		"\u01cc\u01cd\u0003^/\u0000\u01cd\u01cf\u0005\u0005\u0000\u0000\u01ce\u01d0"+
		"\u0003X,\u0000\u01cf\u01ce\u0001\u0000\u0000\u0000\u01cf\u01d0\u0001\u0000"+
		"\u0000\u0000\u01d0\u01d1\u0001\u0000\u0000\u0000\u01d1\u01d2\u0005\u0006"+
		"\u0000\u0000\u01d2\u01d3\u0005\u0003\u0000\u0000\u01d3W\u0001\u0000\u0000"+
		"\u0000\u01d4\u01d9\u0003T*\u0000\u01d5\u01d6\u0005\u0007\u0000\u0000\u01d6"+
		"\u01d8\u0003T*\u0000\u01d7\u01d5\u0001\u0000\u0000\u0000\u01d8\u01db\u0001"+
		"\u0000\u0000\u0000\u01d9\u01d7\u0001\u0000\u0000\u0000\u01d9\u01da\u0001"+
		"\u0000\u0000\u0000\u01daY\u0001\u0000\u0000\u0000\u01db\u01d9\u0001\u0000"+
		"\u0000\u0000\u01dc\u01dd\u0005#\u0000\u0000\u01dd[\u0001\u0000\u0000\u0000"+
		"\u01de\u01df\u0005$\u0000\u0000\u01df]\u0001\u0000\u0000\u0000\u01e0\u01e1"+
		"\u0007\u0006\u0000\u0000\u01e1_\u0001\u0000\u0000\u0000.ciz\u007f\u0084"+
		"\u0086\u008c\u0095\u00a2\u00a7\u00aa\u00ae\u00b7\u00bf\u00c5\u00cb\u00d0"+
		"\u00d9\u00dd\u00e3\u00ef\u00f5\u00f9\u0102\u0115\u0121\u012e\u0140\u0147"+
		"\u0150\u0158\u015e\u016f\u0174\u0178\u0180\u0183\u0193\u019a\u01a7\u01ac"+
		"\u01b2\u01bb\u01c5\u01cf\u01d9";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}