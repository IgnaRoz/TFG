# Generated from d:/source/Universidad/TFG/gramatica.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,285,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,5,0,64,8,0,10,0,12,0,
        67,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,77,8,1,1,2,1,2,1,2,1,
        2,1,2,1,2,3,2,85,8,2,1,3,1,3,1,3,1,3,3,3,91,8,3,1,3,1,3,1,4,1,4,
        1,4,5,4,98,8,4,10,4,12,4,101,9,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,
        1,7,1,7,3,7,113,8,7,1,7,1,7,1,8,1,8,1,8,5,8,120,8,8,10,8,12,8,123,
        9,8,1,9,1,9,1,9,1,9,3,9,129,8,9,1,9,1,9,1,9,3,9,134,8,9,1,9,1,9,
        1,9,1,9,1,9,1,10,1,10,1,10,5,10,144,8,10,10,10,12,10,147,9,10,1,
        11,1,11,1,11,3,11,152,8,11,5,11,154,8,11,10,11,12,11,157,9,11,1,
        12,1,12,1,12,3,12,162,8,12,1,13,1,13,1,13,3,13,167,8,13,1,13,1,13,
        1,14,1,14,1,14,5,14,174,8,14,10,14,12,14,177,9,14,1,15,1,15,1,16,
        1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,3,17,196,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,3,18,213,8,18,1,19,1,19,1,19,3,19,
        218,8,19,5,19,220,8,19,10,19,12,19,223,9,19,1,20,1,20,1,20,3,20,
        228,8,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,3,22,
        240,8,22,1,23,1,23,3,23,244,8,23,1,24,1,24,1,24,1,25,1,25,1,25,1,
        25,1,25,1,25,5,25,255,8,25,10,25,12,25,258,9,25,1,25,1,25,1,25,1,
        26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,5,27,271,8,27,10,27,12,27,
        274,9,27,1,27,1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,30,0,0,31,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,0,4,1,0,7,9,1,0,29,30,1,0,16,17,1,0,27,28,
        289,0,65,1,0,0,0,2,76,1,0,0,0,4,84,1,0,0,0,6,86,1,0,0,0,8,94,1,0,
        0,0,10,102,1,0,0,0,12,106,1,0,0,0,14,108,1,0,0,0,16,116,1,0,0,0,
        18,124,1,0,0,0,20,140,1,0,0,0,22,155,1,0,0,0,24,161,1,0,0,0,26,163,
        1,0,0,0,28,170,1,0,0,0,30,178,1,0,0,0,32,180,1,0,0,0,34,195,1,0,
        0,0,36,212,1,0,0,0,38,221,1,0,0,0,40,227,1,0,0,0,42,229,1,0,0,0,
        44,239,1,0,0,0,46,243,1,0,0,0,48,245,1,0,0,0,50,248,1,0,0,0,52,262,
        1,0,0,0,54,264,1,0,0,0,56,278,1,0,0,0,58,280,1,0,0,0,60,282,1,0,
        0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,
        1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,69,5,0,0,1,69,1,1,0,0,0,70,
        77,3,4,2,0,71,77,3,18,9,0,72,77,3,50,25,0,73,77,3,54,27,0,74,77,
        3,56,28,0,75,77,3,58,29,0,76,70,1,0,0,0,76,71,1,0,0,0,76,72,1,0,
        0,0,76,73,1,0,0,0,76,74,1,0,0,0,76,75,1,0,0,0,77,3,1,0,0,0,78,79,
        3,6,3,0,79,80,5,1,0,0,80,85,1,0,0,0,81,82,3,14,7,0,82,83,5,1,0,0,
        83,85,1,0,0,0,84,78,1,0,0,0,84,81,1,0,0,0,85,5,1,0,0,0,86,87,5,2,
        0,0,87,88,3,60,30,0,88,90,5,3,0,0,89,91,3,8,4,0,90,89,1,0,0,0,90,
        91,1,0,0,0,91,92,1,0,0,0,92,93,5,4,0,0,93,7,1,0,0,0,94,99,3,10,5,
        0,95,96,5,5,0,0,96,98,3,10,5,0,97,95,1,0,0,0,98,101,1,0,0,0,99,97,
        1,0,0,0,99,100,1,0,0,0,100,9,1,0,0,0,101,99,1,0,0,0,102,103,3,60,
        30,0,103,104,5,6,0,0,104,105,3,12,6,0,105,11,1,0,0,0,106,107,7,0,
        0,0,107,13,1,0,0,0,108,109,5,10,0,0,109,110,3,60,30,0,110,112,5,
        3,0,0,111,113,3,16,8,0,112,111,1,0,0,0,112,113,1,0,0,0,113,114,1,
        0,0,0,114,115,5,4,0,0,115,15,1,0,0,0,116,121,3,60,30,0,117,118,5,
        5,0,0,118,120,3,60,30,0,119,117,1,0,0,0,120,123,1,0,0,0,121,119,
        1,0,0,0,121,122,1,0,0,0,122,17,1,0,0,0,123,121,1,0,0,0,124,125,5,
        11,0,0,125,126,3,60,30,0,126,128,5,3,0,0,127,129,3,20,10,0,128,127,
        1,0,0,0,128,129,1,0,0,0,129,130,1,0,0,0,130,131,5,4,0,0,131,133,
        5,6,0,0,132,134,3,58,29,0,133,132,1,0,0,0,133,134,1,0,0,0,134,135,
        1,0,0,0,135,136,5,12,0,0,136,137,3,22,11,0,137,138,5,13,0,0,138,
        139,3,38,19,0,139,19,1,0,0,0,140,145,3,60,30,0,141,142,5,5,0,0,142,
        144,3,60,30,0,143,141,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,
        146,1,0,0,0,146,21,1,0,0,0,147,145,1,0,0,0,148,149,3,24,12,0,149,
        151,5,1,0,0,150,152,3,56,28,0,151,150,1,0,0,0,151,152,1,0,0,0,152,
        154,1,0,0,0,153,148,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,
        156,1,0,0,0,156,23,1,0,0,0,157,155,1,0,0,0,158,162,3,26,13,0,159,
        162,3,32,16,0,160,162,3,36,18,0,161,158,1,0,0,0,161,159,1,0,0,0,
        161,160,1,0,0,0,162,25,1,0,0,0,163,164,3,60,30,0,164,166,5,3,0,0,
        165,167,3,28,14,0,166,165,1,0,0,0,166,167,1,0,0,0,167,168,1,0,0,
        0,168,169,5,4,0,0,169,27,1,0,0,0,170,175,3,30,15,0,171,172,5,5,0,
        0,172,174,3,30,15,0,173,171,1,0,0,0,174,177,1,0,0,0,175,173,1,0,
        0,0,175,176,1,0,0,0,176,29,1,0,0,0,177,175,1,0,0,0,178,179,7,1,0,
        0,179,31,1,0,0,0,180,181,3,34,17,0,181,182,5,19,0,0,182,183,3,34,
        17,0,183,33,1,0,0,0,184,185,5,30,0,0,185,186,5,14,0,0,186,196,3,
        60,30,0,187,188,5,29,0,0,188,189,5,14,0,0,189,196,3,60,30,0,190,
        196,5,29,0,0,191,196,5,30,0,0,192,196,5,28,0,0,193,196,5,27,0,0,
        194,196,5,26,0,0,195,184,1,0,0,0,195,187,1,0,0,0,195,190,1,0,0,0,
        195,191,1,0,0,0,195,192,1,0,0,0,195,193,1,0,0,0,195,194,1,0,0,0,
        196,35,1,0,0,0,197,198,5,20,0,0,198,199,5,3,0,0,199,200,3,22,11,
        0,200,201,5,4,0,0,201,213,1,0,0,0,202,203,5,21,0,0,203,204,5,3,0,
        0,204,205,3,22,11,0,205,206,5,4,0,0,206,213,1,0,0,0,207,208,5,22,
        0,0,208,209,5,3,0,0,209,210,3,24,12,0,210,211,5,4,0,0,211,213,1,
        0,0,0,212,197,1,0,0,0,212,202,1,0,0,0,212,207,1,0,0,0,213,37,1,0,
        0,0,214,215,3,40,20,0,215,217,5,1,0,0,216,218,3,56,28,0,217,216,
        1,0,0,0,217,218,1,0,0,0,218,220,1,0,0,0,219,214,1,0,0,0,220,223,
        1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,39,1,0,0,0,223,221,1,
        0,0,0,224,228,3,42,21,0,225,228,3,48,24,0,226,228,3,26,13,0,227,
        224,1,0,0,0,227,225,1,0,0,0,227,226,1,0,0,0,228,41,1,0,0,0,229,230,
        3,44,22,0,230,231,5,23,0,0,231,232,3,46,23,0,232,43,1,0,0,0,233,
        234,5,30,0,0,234,235,5,14,0,0,235,240,3,60,30,0,236,237,5,29,0,0,
        237,238,5,14,0,0,238,240,3,60,30,0,239,233,1,0,0,0,239,236,1,0,0,
        0,240,45,1,0,0,0,241,244,3,44,22,0,242,244,5,28,0,0,243,241,1,0,
        0,0,243,242,1,0,0,0,244,47,1,0,0,0,245,246,5,15,0,0,246,247,3,26,
        13,0,247,49,1,0,0,0,248,249,7,2,0,0,249,250,3,60,30,0,250,251,5,
        3,0,0,251,256,3,52,26,0,252,253,5,5,0,0,253,255,3,52,26,0,254,252,
        1,0,0,0,255,258,1,0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,259,
        1,0,0,0,258,256,1,0,0,0,259,260,5,4,0,0,260,261,5,1,0,0,261,51,1,
        0,0,0,262,263,7,3,0,0,263,53,1,0,0,0,264,265,5,18,0,0,265,266,3,
        60,30,0,266,267,5,3,0,0,267,272,3,52,26,0,268,269,5,5,0,0,269,271,
        3,52,26,0,270,268,1,0,0,0,271,274,1,0,0,0,272,270,1,0,0,0,272,273,
        1,0,0,0,273,275,1,0,0,0,274,272,1,0,0,0,275,276,5,4,0,0,276,277,
        5,1,0,0,277,55,1,0,0,0,278,279,5,24,0,0,279,57,1,0,0,0,280,281,5,
        25,0,0,281,59,1,0,0,0,282,283,7,1,0,0,283,61,1,0,0,0,24,65,76,84,
        90,99,112,121,128,133,145,151,155,161,166,175,195,212,217,221,227,
        239,243,256,272
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'Categoria'", "'('", "')'", "','", 
                     "':'", "'int'", "'str'", "'bool'", "'Prop'", "'Accion'", 
                     "'Condiciones:'", "'Consecuencias:'", "'.'", "'DEL'", 
                     "'new'", "'add'", "'Run'", "<INVALID>", "'OR'", "'AND'", 
                     "'NOT'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "OpComp", "OR", 
                      "AND", "NOT", "OpAsign", "COMMENT_SIMPLE", "COMMENT_MULTI", 
                      "BOOLEAN", "STRING", "NUMBER", "INDIVIDUO", "VARIABLE", 
                      "WS" ]

    RULE_programa = 0
    RULE_elemento = 1
    RULE_declaracion = 2
    RULE_declCategoria = 3
    RULE_listaAtributos = 4
    RULE_atributo = 5
    RULE_tipoBasico = 6
    RULE_declProposicion = 7
    RULE_listaIdentificadores = 8
    RULE_accion = 9
    RULE_listaParams = 10
    RULE_listaCondiciones = 11
    RULE_condicion = 12
    RULE_predicado = 13
    RULE_listaArgsPredicado = 14
    RULE_paramPredicado = 15
    RULE_comparacion = 16
    RULE_operando = 17
    RULE_operacionLogica = 18
    RULE_listaConsecuencias = 19
    RULE_consecuencia = 20
    RULE_asignacion = 21
    RULE_operandoIzq = 22
    RULE_operandoDrc = 23
    RULE_borrado = 24
    RULE_inicializacion = 25
    RULE_argLit = 26
    RULE_ejecucion = 27
    RULE_comentarioSimple = 28
    RULE_comentarioMultilineo = 29
    RULE_idName = 30

    ruleNames =  [ "programa", "elemento", "declaracion", "declCategoria", 
                   "listaAtributos", "atributo", "tipoBasico", "declProposicion", 
                   "listaIdentificadores", "accion", "listaParams", "listaCondiciones", 
                   "condicion", "predicado", "listaArgsPredicado", "paramPredicado", 
                   "comparacion", "operando", "operacionLogica", "listaConsecuencias", 
                   "consecuencia", "asignacion", "operandoIzq", "operandoDrc", 
                   "borrado", "inicializacion", "argLit", "ejecucion", "comentarioSimple", 
                   "comentarioMultilineo", "idName" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    OpComp=19
    OR=20
    AND=21
    NOT=22
    OpAsign=23
    COMMENT_SIMPLE=24
    COMMENT_MULTI=25
    BOOLEAN=26
    STRING=27
    NUMBER=28
    INDIVIDUO=29
    VARIABLE=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gramaticaParser.EOF, 0)

        def elemento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ElementoContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ElementoContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = gramaticaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 50793476) != 0):
                self.state = 62
                self.elemento()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(gramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(gramaticaParser.DeclaracionContext,0)


        def accion(self):
            return self.getTypedRuleContext(gramaticaParser.AccionContext,0)


        def inicializacion(self):
            return self.getTypedRuleContext(gramaticaParser.InicializacionContext,0)


        def ejecucion(self):
            return self.getTypedRuleContext(gramaticaParser.EjecucionContext,0)


        def comentarioSimple(self):
            return self.getTypedRuleContext(gramaticaParser.ComentarioSimpleContext,0)


        def comentarioMultilineo(self):
            return self.getTypedRuleContext(gramaticaParser.ComentarioMultilineoContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_elemento

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElemento" ):
                return visitor.visitElemento(self)
            else:
                return visitor.visitChildren(self)




    def elemento(self):

        localctx = gramaticaParser.ElementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_elemento)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.declaracion()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.accion()
                pass
            elif token in [16, 17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.inicializacion()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.ejecucion()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 74
                self.comentarioSimple()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 6)
                self.state = 75
                self.comentarioMultilineo()
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


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declCategoria(self):
            return self.getTypedRuleContext(gramaticaParser.DeclCategoriaContext,0)


        def declProposicion(self):
            return self.getTypedRuleContext(gramaticaParser.DeclProposicionContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_declaracion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = gramaticaParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.declCategoria()
                self.state = 79
                self.match(gramaticaParser.T__0)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.declProposicion()
                self.state = 82
                self.match(gramaticaParser.T__0)
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


    class DeclCategoriaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idName(self):
            return self.getTypedRuleContext(gramaticaParser.IdNameContext,0)


        def listaAtributos(self):
            return self.getTypedRuleContext(gramaticaParser.ListaAtributosContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_declCategoria

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclCategoria" ):
                return visitor.visitDeclCategoria(self)
            else:
                return visitor.visitChildren(self)




    def declCategoria(self):

        localctx = gramaticaParser.DeclCategoriaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declCategoria)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(gramaticaParser.T__1)
            self.state = 87
            self.idName()
            self.state = 88
            self.match(gramaticaParser.T__2)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29 or _la==30:
                self.state = 89
                self.listaAtributos()


            self.state = 92
            self.match(gramaticaParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaAtributosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atributo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.AtributoContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.AtributoContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_listaAtributos

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaAtributos" ):
                return visitor.visitListaAtributos(self)
            else:
                return visitor.visitChildren(self)




    def listaAtributos(self):

        localctx = gramaticaParser.ListaAtributosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listaAtributos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.atributo()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 95
                self.match(gramaticaParser.T__4)
                self.state = 96
                self.atributo()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtributoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idName(self):
            return self.getTypedRuleContext(gramaticaParser.IdNameContext,0)


        def tipoBasico(self):
            return self.getTypedRuleContext(gramaticaParser.TipoBasicoContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_atributo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtributo" ):
                return visitor.visitAtributo(self)
            else:
                return visitor.visitChildren(self)




    def atributo(self):

        localctx = gramaticaParser.AtributoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atributo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.idName()
            self.state = 103
            self.match(gramaticaParser.T__5)
            self.state = 104
            self.tipoBasico()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoBasicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_tipoBasico

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoBasico" ):
                return visitor.visitTipoBasico(self)
            else:
                return visitor.visitChildren(self)




    def tipoBasico(self):

        localctx = gramaticaParser.TipoBasicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tipoBasico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
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


    class DeclProposicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idName(self):
            return self.getTypedRuleContext(gramaticaParser.IdNameContext,0)


        def listaIdentificadores(self):
            return self.getTypedRuleContext(gramaticaParser.ListaIdentificadoresContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_declProposicion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclProposicion" ):
                return visitor.visitDeclProposicion(self)
            else:
                return visitor.visitChildren(self)




    def declProposicion(self):

        localctx = gramaticaParser.DeclProposicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declProposicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(gramaticaParser.T__9)
            self.state = 109
            self.idName()
            self.state = 110
            self.match(gramaticaParser.T__2)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29 or _la==30:
                self.state = 111
                self.listaIdentificadores()


            self.state = 114
            self.match(gramaticaParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaIdentificadoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.IdNameContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.IdNameContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_listaIdentificadores

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaIdentificadores" ):
                return visitor.visitListaIdentificadores(self)
            else:
                return visitor.visitChildren(self)




    def listaIdentificadores(self):

        localctx = gramaticaParser.ListaIdentificadoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_listaIdentificadores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.idName()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 117
                self.match(gramaticaParser.T__4)
                self.state = 118
                self.idName()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idName(self):
            return self.getTypedRuleContext(gramaticaParser.IdNameContext,0)


        def listaCondiciones(self):
            return self.getTypedRuleContext(gramaticaParser.ListaCondicionesContext,0)


        def listaConsecuencias(self):
            return self.getTypedRuleContext(gramaticaParser.ListaConsecuenciasContext,0)


        def listaParams(self):
            return self.getTypedRuleContext(gramaticaParser.ListaParamsContext,0)


        def comentarioMultilineo(self):
            return self.getTypedRuleContext(gramaticaParser.ComentarioMultilineoContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_accion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccion" ):
                return visitor.visitAccion(self)
            else:
                return visitor.visitChildren(self)




    def accion(self):

        localctx = gramaticaParser.AccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_accion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(gramaticaParser.T__10)
            self.state = 125
            self.idName()
            self.state = 126
            self.match(gramaticaParser.T__2)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29 or _la==30:
                self.state = 127
                self.listaParams()


            self.state = 130
            self.match(gramaticaParser.T__3)
            self.state = 131
            self.match(gramaticaParser.T__5)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 132
                self.comentarioMultilineo()


            self.state = 135
            self.match(gramaticaParser.T__11)
            self.state = 136
            self.listaCondiciones()
            self.state = 137
            self.match(gramaticaParser.T__12)
            self.state = 138
            self.listaConsecuencias()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.IdNameContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.IdNameContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_listaParams

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaParams" ):
                return visitor.visitListaParams(self)
            else:
                return visitor.visitChildren(self)




    def listaParams(self):

        localctx = gramaticaParser.ListaParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_listaParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.idName()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 141
                self.match(gramaticaParser.T__4)
                self.state = 142
                self.idName()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaCondicionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CondicionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CondicionContext,i)


        def comentarioSimple(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ComentarioSimpleContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ComentarioSimpleContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_listaCondiciones

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaCondiciones" ):
                return visitor.visitListaCondiciones(self)
            else:
                return visitor.visitChildren(self)




    def listaCondiciones(self):

        localctx = gramaticaParser.ListaCondicionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listaCondiciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2087714816) != 0):
                self.state = 148
                self.condicion()
                self.state = 149
                self.match(gramaticaParser.T__0)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 150
                    self.comentarioSimple()


                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicado(self):
            return self.getTypedRuleContext(gramaticaParser.PredicadoContext,0)


        def comparacion(self):
            return self.getTypedRuleContext(gramaticaParser.ComparacionContext,0)


        def operacionLogica(self):
            return self.getTypedRuleContext(gramaticaParser.OperacionLogicaContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_condicion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = gramaticaParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_condicion)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.predicado()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.comparacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.operacionLogica()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicadoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idName(self):
            return self.getTypedRuleContext(gramaticaParser.IdNameContext,0)


        def listaArgsPredicado(self):
            return self.getTypedRuleContext(gramaticaParser.ListaArgsPredicadoContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_predicado

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicado" ):
                return visitor.visitPredicado(self)
            else:
                return visitor.visitChildren(self)




    def predicado(self):

        localctx = gramaticaParser.PredicadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_predicado)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.idName()
            self.state = 164
            self.match(gramaticaParser.T__2)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29 or _la==30:
                self.state = 165
                self.listaArgsPredicado()


            self.state = 168
            self.match(gramaticaParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaArgsPredicadoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramPredicado(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ParamPredicadoContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ParamPredicadoContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_listaArgsPredicado

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaArgsPredicado" ):
                return visitor.visitListaArgsPredicado(self)
            else:
                return visitor.visitChildren(self)




    def listaArgsPredicado(self):

        localctx = gramaticaParser.ListaArgsPredicadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listaArgsPredicado)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.paramPredicado()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 171
                self.match(gramaticaParser.T__4)
                self.state = 172
                self.paramPredicado()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamPredicadoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDIVIDUO(self):
            return self.getToken(gramaticaParser.INDIVIDUO, 0)

        def VARIABLE(self):
            return self.getToken(gramaticaParser.VARIABLE, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_paramPredicado

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamPredicado" ):
                return visitor.visitParamPredicado(self)
            else:
                return visitor.visitChildren(self)




    def paramPredicado(self):

        localctx = gramaticaParser.ParamPredicadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_paramPredicado)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
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


    class ComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.OperandoContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.OperandoContext,i)


        def OpComp(self):
            return self.getToken(gramaticaParser.OpComp, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_comparacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)




    def comparacion(self):

        localctx = gramaticaParser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_comparacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.operando()
            self.state = 181
            self.match(gramaticaParser.OpComp)
            self.state = 182
            self.operando()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_operando

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OperandoVarAttrContext(OperandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.OperandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(gramaticaParser.VARIABLE, 0)
        def idName(self):
            return self.getTypedRuleContext(gramaticaParser.IdNameContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandoVarAttr" ):
                return visitor.visitOperandoVarAttr(self)
            else:
                return visitor.visitChildren(self)


    class OperandoIndAttrContext(OperandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.OperandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INDIVIDUO(self):
            return self.getToken(gramaticaParser.INDIVIDUO, 0)
        def idName(self):
            return self.getTypedRuleContext(gramaticaParser.IdNameContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandoIndAttr" ):
                return visitor.visitOperandoIndAttr(self)
            else:
                return visitor.visitChildren(self)


    class OperandoVarContext(OperandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.OperandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(gramaticaParser.VARIABLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandoVar" ):
                return visitor.visitOperandoVar(self)
            else:
                return visitor.visitChildren(self)


    class OperandoNumContext(OperandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.OperandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandoNum" ):
                return visitor.visitOperandoNum(self)
            else:
                return visitor.visitChildren(self)


    class OperandoBoolContext(OperandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.OperandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(gramaticaParser.BOOLEAN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandoBool" ):
                return visitor.visitOperandoBool(self)
            else:
                return visitor.visitChildren(self)


    class OperandoStrContext(OperandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.OperandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(gramaticaParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandoStr" ):
                return visitor.visitOperandoStr(self)
            else:
                return visitor.visitChildren(self)


    class OperandoIndContext(OperandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.OperandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INDIVIDUO(self):
            return self.getToken(gramaticaParser.INDIVIDUO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandoInd" ):
                return visitor.visitOperandoInd(self)
            else:
                return visitor.visitChildren(self)



    def operando(self):

        localctx = gramaticaParser.OperandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_operando)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = gramaticaParser.OperandoVarAttrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(gramaticaParser.VARIABLE)
                self.state = 185
                self.match(gramaticaParser.T__13)
                self.state = 186
                self.idName()
                pass

            elif la_ == 2:
                localctx = gramaticaParser.OperandoIndAttrContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(gramaticaParser.INDIVIDUO)
                self.state = 188
                self.match(gramaticaParser.T__13)
                self.state = 189
                self.idName()
                pass

            elif la_ == 3:
                localctx = gramaticaParser.OperandoIndContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.match(gramaticaParser.INDIVIDUO)
                pass

            elif la_ == 4:
                localctx = gramaticaParser.OperandoVarContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.match(gramaticaParser.VARIABLE)
                pass

            elif la_ == 5:
                localctx = gramaticaParser.OperandoNumContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 192
                self.match(gramaticaParser.NUMBER)
                pass

            elif la_ == 6:
                localctx = gramaticaParser.OperandoStrContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 193
                self.match(gramaticaParser.STRING)
                pass

            elif la_ == 7:
                localctx = gramaticaParser.OperandoBoolContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 194
                self.match(gramaticaParser.BOOLEAN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionLogicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_operacionLogica

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OpOrContext(OperacionLogicaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.OperacionLogicaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(gramaticaParser.OR, 0)
        def listaCondiciones(self):
            return self.getTypedRuleContext(gramaticaParser.ListaCondicionesContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpOr" ):
                return visitor.visitOpOr(self)
            else:
                return visitor.visitChildren(self)


    class OpNotContext(OperacionLogicaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.OperacionLogicaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(gramaticaParser.NOT, 0)
        def condicion(self):
            return self.getTypedRuleContext(gramaticaParser.CondicionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpNot" ):
                return visitor.visitOpNot(self)
            else:
                return visitor.visitChildren(self)


    class OpAndContext(OperacionLogicaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.OperacionLogicaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(gramaticaParser.AND, 0)
        def listaCondiciones(self):
            return self.getTypedRuleContext(gramaticaParser.ListaCondicionesContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpAnd" ):
                return visitor.visitOpAnd(self)
            else:
                return visitor.visitChildren(self)



    def operacionLogica(self):

        localctx = gramaticaParser.OperacionLogicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_operacionLogica)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = gramaticaParser.OpOrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(gramaticaParser.OR)
                self.state = 198
                self.match(gramaticaParser.T__2)
                self.state = 199
                self.listaCondiciones()
                self.state = 200
                self.match(gramaticaParser.T__3)
                pass
            elif token in [21]:
                localctx = gramaticaParser.OpAndContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.match(gramaticaParser.AND)
                self.state = 203
                self.match(gramaticaParser.T__2)
                self.state = 204
                self.listaCondiciones()
                self.state = 205
                self.match(gramaticaParser.T__3)
                pass
            elif token in [22]:
                localctx = gramaticaParser.OpNotContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.match(gramaticaParser.NOT)
                self.state = 208
                self.match(gramaticaParser.T__2)
                self.state = 209
                self.condicion()
                self.state = 210
                self.match(gramaticaParser.T__3)
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


    class ListaConsecuenciasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def consecuencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ConsecuenciaContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ConsecuenciaContext,i)


        def comentarioSimple(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ComentarioSimpleContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ComentarioSimpleContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_listaConsecuencias

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaConsecuencias" ):
                return visitor.visitListaConsecuencias(self)
            else:
                return visitor.visitChildren(self)




    def listaConsecuencias(self):

        localctx = gramaticaParser.ListaConsecuenciasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_listaConsecuencias)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1610645504) != 0):
                self.state = 214
                self.consecuencia()
                self.state = 215
                self.match(gramaticaParser.T__0)
                self.state = 217
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 216
                    self.comentarioSimple()


                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConsecuenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(gramaticaParser.AsignacionContext,0)


        def borrado(self):
            return self.getTypedRuleContext(gramaticaParser.BorradoContext,0)


        def predicado(self):
            return self.getTypedRuleContext(gramaticaParser.PredicadoContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_consecuencia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConsecuencia" ):
                return visitor.visitConsecuencia(self)
            else:
                return visitor.visitChildren(self)




    def consecuencia(self):

        localctx = gramaticaParser.ConsecuenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_consecuencia)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.borrado()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 226
                self.predicado()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operandoIzq(self):
            return self.getTypedRuleContext(gramaticaParser.OperandoIzqContext,0)


        def OpAsign(self):
            return self.getToken(gramaticaParser.OpAsign, 0)

        def operandoDrc(self):
            return self.getTypedRuleContext(gramaticaParser.OperandoDrcContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_asignacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = gramaticaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.operandoIzq()
            self.state = 230
            self.match(gramaticaParser.OpAsign)
            self.state = 231
            self.operandoDrc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandoIzqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(gramaticaParser.VARIABLE, 0)

        def idName(self):
            return self.getTypedRuleContext(gramaticaParser.IdNameContext,0)


        def INDIVIDUO(self):
            return self.getToken(gramaticaParser.INDIVIDUO, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_operandoIzq

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandoIzq" ):
                return visitor.visitOperandoIzq(self)
            else:
                return visitor.visitChildren(self)




    def operandoIzq(self):

        localctx = gramaticaParser.OperandoIzqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_operandoIzq)
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(gramaticaParser.VARIABLE)
                self.state = 234
                self.match(gramaticaParser.T__13)
                self.state = 235
                self.idName()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(gramaticaParser.INDIVIDUO)
                self.state = 237
                self.match(gramaticaParser.T__13)
                self.state = 238
                self.idName()
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


    class OperandoDrcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operandoIzq(self):
            return self.getTypedRuleContext(gramaticaParser.OperandoIzqContext,0)


        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_operandoDrc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandoDrc" ):
                return visitor.visitOperandoDrc(self)
            else:
                return visitor.visitChildren(self)




    def operandoDrc(self):

        localctx = gramaticaParser.OperandoDrcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_operandoDrc)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.operandoIzq()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(gramaticaParser.NUMBER)
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


    class BorradoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicado(self):
            return self.getTypedRuleContext(gramaticaParser.PredicadoContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_borrado

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBorrado" ):
                return visitor.visitBorrado(self)
            else:
                return visitor.visitChildren(self)




    def borrado(self):

        localctx = gramaticaParser.BorradoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_borrado)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(gramaticaParser.T__14)
            self.state = 246
            self.predicado()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicializacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idName(self):
            return self.getTypedRuleContext(gramaticaParser.IdNameContext,0)


        def argLit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ArgLitContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ArgLitContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_inicializacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicializacion" ):
                return visitor.visitInicializacion(self)
            else:
                return visitor.visitChildren(self)




    def inicializacion(self):

        localctx = gramaticaParser.InicializacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_inicializacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 249
            self.idName()
            self.state = 250
            self.match(gramaticaParser.T__2)
            self.state = 251
            self.argLit()
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 252
                self.match(gramaticaParser.T__4)
                self.state = 253
                self.argLit()
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 259
            self.match(gramaticaParser.T__3)
            self.state = 260
            self.match(gramaticaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(gramaticaParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_argLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgLit" ):
                return visitor.visitArgLit(self)
            else:
                return visitor.visitChildren(self)




    def argLit(self):

        localctx = gramaticaParser.ArgLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_argLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
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


    class EjecucionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idName(self):
            return self.getTypedRuleContext(gramaticaParser.IdNameContext,0)


        def argLit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ArgLitContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ArgLitContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_ejecucion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEjecucion" ):
                return visitor.visitEjecucion(self)
            else:
                return visitor.visitChildren(self)




    def ejecucion(self):

        localctx = gramaticaParser.EjecucionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ejecucion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(gramaticaParser.T__17)
            self.state = 265
            self.idName()
            self.state = 266
            self.match(gramaticaParser.T__2)
            self.state = 267
            self.argLit()
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 268
                self.match(gramaticaParser.T__4)
                self.state = 269
                self.argLit()
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 275
            self.match(gramaticaParser.T__3)
            self.state = 276
            self.match(gramaticaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComentarioSimpleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT_SIMPLE(self):
            return self.getToken(gramaticaParser.COMMENT_SIMPLE, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_comentarioSimple

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComentarioSimple" ):
                return visitor.visitComentarioSimple(self)
            else:
                return visitor.visitChildren(self)




    def comentarioSimple(self):

        localctx = gramaticaParser.ComentarioSimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_comentarioSimple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(gramaticaParser.COMMENT_SIMPLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComentarioMultilineoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT_MULTI(self):
            return self.getToken(gramaticaParser.COMMENT_MULTI, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_comentarioMultilineo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComentarioMultilineo" ):
                return visitor.visitComentarioMultilineo(self)
            else:
                return visitor.visitChildren(self)




    def comentarioMultilineo(self):

        localctx = gramaticaParser.ComentarioMultilineoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_comentarioMultilineo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(gramaticaParser.COMMENT_MULTI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDIVIDUO(self):
            return self.getToken(gramaticaParser.INDIVIDUO, 0)

        def VARIABLE(self):
            return self.getToken(gramaticaParser.VARIABLE, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_idName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdName" ):
                return visitor.visitIdName(self)
            else:
                return visitor.visitChildren(self)




    def idName(self):

        localctx = gramaticaParser.IdNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_idName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
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





