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
        4,1,31,289,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,5,0,64,8,0,10,0,12,0,
        67,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,77,8,1,1,2,1,2,1,2,3,
        2,82,8,2,1,2,1,2,1,2,3,2,87,8,2,3,2,89,8,2,1,3,1,3,1,3,1,3,3,3,95,
        8,3,1,3,1,3,1,4,1,4,1,4,5,4,102,8,4,10,4,12,4,105,9,4,1,5,1,5,1,
        5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,3,7,117,8,7,1,7,1,7,1,8,1,8,1,8,5,
        8,124,8,8,10,8,12,8,127,9,8,1,9,1,9,1,9,1,9,3,9,133,8,9,1,9,1,9,
        1,9,3,9,138,8,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,5,10,148,8,10,
        10,10,12,10,151,9,10,1,11,1,11,1,11,3,11,156,8,11,5,11,158,8,11,
        10,11,12,11,161,9,11,1,12,1,12,1,12,3,12,166,8,12,1,13,1,13,1,13,
        3,13,171,8,13,1,13,1,13,1,14,1,14,1,14,5,14,178,8,14,10,14,12,14,
        181,9,14,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,3,17,200,8,17,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,217,
        8,18,1,19,1,19,1,19,3,19,222,8,19,5,19,224,8,19,10,19,12,19,227,
        9,19,1,20,1,20,1,20,3,20,232,8,20,1,21,1,21,1,21,1,21,1,22,1,22,
        1,22,1,22,1,22,1,22,3,22,244,8,22,1,23,1,23,3,23,248,8,23,1,24,1,
        24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,5,25,259,8,25,10,25,12,25,
        262,9,25,1,25,1,25,1,25,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,
        5,27,275,8,27,10,27,12,27,278,9,27,1,27,1,27,1,27,1,28,1,28,1,29,
        1,29,1,30,1,30,1,30,0,0,31,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,0,5,1,0,7,9,1,
        0,26,30,1,0,16,17,1,0,27,28,1,0,29,30,295,0,65,1,0,0,0,2,76,1,0,
        0,0,4,88,1,0,0,0,6,90,1,0,0,0,8,98,1,0,0,0,10,106,1,0,0,0,12,110,
        1,0,0,0,14,112,1,0,0,0,16,120,1,0,0,0,18,128,1,0,0,0,20,144,1,0,
        0,0,22,159,1,0,0,0,24,165,1,0,0,0,26,167,1,0,0,0,28,174,1,0,0,0,
        30,182,1,0,0,0,32,184,1,0,0,0,34,199,1,0,0,0,36,216,1,0,0,0,38,225,
        1,0,0,0,40,231,1,0,0,0,42,233,1,0,0,0,44,243,1,0,0,0,46,247,1,0,
        0,0,48,249,1,0,0,0,50,252,1,0,0,0,52,266,1,0,0,0,54,268,1,0,0,0,
        56,282,1,0,0,0,58,284,1,0,0,0,60,286,1,0,0,0,62,64,3,2,1,0,63,62,
        1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,
        67,65,1,0,0,0,68,69,5,0,0,1,69,1,1,0,0,0,70,77,3,4,2,0,71,77,3,18,
        9,0,72,77,3,50,25,0,73,77,3,54,27,0,74,77,3,56,28,0,75,77,3,58,29,
        0,76,70,1,0,0,0,76,71,1,0,0,0,76,72,1,0,0,0,76,73,1,0,0,0,76,74,
        1,0,0,0,76,75,1,0,0,0,77,3,1,0,0,0,78,79,3,6,3,0,79,81,5,1,0,0,80,
        82,3,56,28,0,81,80,1,0,0,0,81,82,1,0,0,0,82,89,1,0,0,0,83,84,3,14,
        7,0,84,86,5,1,0,0,85,87,3,56,28,0,86,85,1,0,0,0,86,87,1,0,0,0,87,
        89,1,0,0,0,88,78,1,0,0,0,88,83,1,0,0,0,89,5,1,0,0,0,90,91,5,2,0,
        0,91,92,3,60,30,0,92,94,5,3,0,0,93,95,3,8,4,0,94,93,1,0,0,0,94,95,
        1,0,0,0,95,96,1,0,0,0,96,97,5,4,0,0,97,7,1,0,0,0,98,103,3,10,5,0,
        99,100,5,5,0,0,100,102,3,10,5,0,101,99,1,0,0,0,102,105,1,0,0,0,103,
        101,1,0,0,0,103,104,1,0,0,0,104,9,1,0,0,0,105,103,1,0,0,0,106,107,
        3,60,30,0,107,108,5,6,0,0,108,109,3,12,6,0,109,11,1,0,0,0,110,111,
        7,0,0,0,111,13,1,0,0,0,112,113,5,10,0,0,113,114,3,60,30,0,114,116,
        5,3,0,0,115,117,3,16,8,0,116,115,1,0,0,0,116,117,1,0,0,0,117,118,
        1,0,0,0,118,119,5,4,0,0,119,15,1,0,0,0,120,125,3,60,30,0,121,122,
        5,5,0,0,122,124,3,60,30,0,123,121,1,0,0,0,124,127,1,0,0,0,125,123,
        1,0,0,0,125,126,1,0,0,0,126,17,1,0,0,0,127,125,1,0,0,0,128,129,5,
        11,0,0,129,130,3,60,30,0,130,132,5,3,0,0,131,133,3,20,10,0,132,131,
        1,0,0,0,132,133,1,0,0,0,133,134,1,0,0,0,134,135,5,4,0,0,135,137,
        5,6,0,0,136,138,3,58,29,0,137,136,1,0,0,0,137,138,1,0,0,0,138,139,
        1,0,0,0,139,140,5,12,0,0,140,141,3,22,11,0,141,142,5,13,0,0,142,
        143,3,38,19,0,143,19,1,0,0,0,144,149,3,60,30,0,145,146,5,5,0,0,146,
        148,3,60,30,0,147,145,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,
        150,1,0,0,0,150,21,1,0,0,0,151,149,1,0,0,0,152,153,3,24,12,0,153,
        155,5,1,0,0,154,156,3,56,28,0,155,154,1,0,0,0,155,156,1,0,0,0,156,
        158,1,0,0,0,157,152,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,
        160,1,0,0,0,160,23,1,0,0,0,161,159,1,0,0,0,162,166,3,26,13,0,163,
        166,3,32,16,0,164,166,3,36,18,0,165,162,1,0,0,0,165,163,1,0,0,0,
        165,164,1,0,0,0,166,25,1,0,0,0,167,168,3,60,30,0,168,170,5,3,0,0,
        169,171,3,28,14,0,170,169,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,
        0,172,173,5,4,0,0,173,27,1,0,0,0,174,179,3,30,15,0,175,176,5,5,0,
        0,176,178,3,30,15,0,177,175,1,0,0,0,178,181,1,0,0,0,179,177,1,0,
        0,0,179,180,1,0,0,0,180,29,1,0,0,0,181,179,1,0,0,0,182,183,7,1,0,
        0,183,31,1,0,0,0,184,185,3,34,17,0,185,186,5,19,0,0,186,187,3,34,
        17,0,187,33,1,0,0,0,188,189,5,30,0,0,189,190,5,14,0,0,190,200,3,
        60,30,0,191,192,5,29,0,0,192,193,5,14,0,0,193,200,3,60,30,0,194,
        200,5,29,0,0,195,200,5,30,0,0,196,200,5,28,0,0,197,200,5,27,0,0,
        198,200,5,26,0,0,199,188,1,0,0,0,199,191,1,0,0,0,199,194,1,0,0,0,
        199,195,1,0,0,0,199,196,1,0,0,0,199,197,1,0,0,0,199,198,1,0,0,0,
        200,35,1,0,0,0,201,202,5,20,0,0,202,203,5,3,0,0,203,204,3,22,11,
        0,204,205,5,4,0,0,205,217,1,0,0,0,206,207,5,21,0,0,207,208,5,3,0,
        0,208,209,3,22,11,0,209,210,5,4,0,0,210,217,1,0,0,0,211,212,5,22,
        0,0,212,213,5,3,0,0,213,214,3,24,12,0,214,215,5,4,0,0,215,217,1,
        0,0,0,216,201,1,0,0,0,216,206,1,0,0,0,216,211,1,0,0,0,217,37,1,0,
        0,0,218,219,3,40,20,0,219,221,5,1,0,0,220,222,3,56,28,0,221,220,
        1,0,0,0,221,222,1,0,0,0,222,224,1,0,0,0,223,218,1,0,0,0,224,227,
        1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,39,1,0,0,0,227,225,1,
        0,0,0,228,232,3,42,21,0,229,232,3,48,24,0,230,232,3,26,13,0,231,
        228,1,0,0,0,231,229,1,0,0,0,231,230,1,0,0,0,232,41,1,0,0,0,233,234,
        3,44,22,0,234,235,5,23,0,0,235,236,3,46,23,0,236,43,1,0,0,0,237,
        238,5,30,0,0,238,239,5,14,0,0,239,244,3,60,30,0,240,241,5,29,0,0,
        241,242,5,14,0,0,242,244,3,60,30,0,243,237,1,0,0,0,243,240,1,0,0,
        0,244,45,1,0,0,0,245,248,3,44,22,0,246,248,5,28,0,0,247,245,1,0,
        0,0,247,246,1,0,0,0,248,47,1,0,0,0,249,250,5,15,0,0,250,251,3,26,
        13,0,251,49,1,0,0,0,252,253,7,2,0,0,253,254,3,60,30,0,254,255,5,
        3,0,0,255,260,3,52,26,0,256,257,5,5,0,0,257,259,3,52,26,0,258,256,
        1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,263,
        1,0,0,0,262,260,1,0,0,0,263,264,5,4,0,0,264,265,5,1,0,0,265,51,1,
        0,0,0,266,267,7,3,0,0,267,53,1,0,0,0,268,269,5,18,0,0,269,270,3,
        60,30,0,270,271,5,3,0,0,271,276,3,52,26,0,272,273,5,5,0,0,273,275,
        3,52,26,0,274,272,1,0,0,0,275,278,1,0,0,0,276,274,1,0,0,0,276,277,
        1,0,0,0,277,279,1,0,0,0,278,276,1,0,0,0,279,280,5,4,0,0,280,281,
        5,1,0,0,281,55,1,0,0,0,282,283,5,24,0,0,283,57,1,0,0,0,284,285,5,
        25,0,0,285,59,1,0,0,0,286,287,7,4,0,0,287,61,1,0,0,0,26,65,76,81,
        86,88,94,103,116,125,132,137,149,155,159,165,170,179,199,216,221,
        225,231,243,247,260,276
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


        def comentarioSimple(self):
            return self.getTypedRuleContext(gramaticaParser.ComentarioSimpleContext,0)


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
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.declCategoria()
                self.state = 79
                self.match(gramaticaParser.T__0)
                self.state = 81
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 80
                    self.comentarioSimple()


                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.declProposicion()
                self.state = 84
                self.match(gramaticaParser.T__0)
                self.state = 86
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 85
                    self.comentarioSimple()


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
            self.state = 90
            self.match(gramaticaParser.T__1)
            self.state = 91
            self.idName()
            self.state = 92
            self.match(gramaticaParser.T__2)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29 or _la==30:
                self.state = 93
                self.listaAtributos()


            self.state = 96
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
            self.state = 98
            self.atributo()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 99
                self.match(gramaticaParser.T__4)
                self.state = 100
                self.atributo()
                self.state = 105
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
            self.state = 106
            self.idName()
            self.state = 107
            self.match(gramaticaParser.T__5)
            self.state = 108
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
            self.state = 110
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
            self.state = 112
            self.match(gramaticaParser.T__9)
            self.state = 113
            self.idName()
            self.state = 114
            self.match(gramaticaParser.T__2)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29 or _la==30:
                self.state = 115
                self.listaIdentificadores()


            self.state = 118
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
            self.state = 120
            self.idName()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 121
                self.match(gramaticaParser.T__4)
                self.state = 122
                self.idName()
                self.state = 127
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
            self.state = 128
            self.match(gramaticaParser.T__10)
            self.state = 129
            self.idName()
            self.state = 130
            self.match(gramaticaParser.T__2)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29 or _la==30:
                self.state = 131
                self.listaParams()


            self.state = 134
            self.match(gramaticaParser.T__3)
            self.state = 135
            self.match(gramaticaParser.T__5)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 136
                self.comentarioMultilineo()


            self.state = 139
            self.match(gramaticaParser.T__11)
            self.state = 140
            self.listaCondiciones()
            self.state = 141
            self.match(gramaticaParser.T__12)
            self.state = 142
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
            self.state = 144
            self.idName()
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 145
                self.match(gramaticaParser.T__4)
                self.state = 146
                self.idName()
                self.state = 151
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
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2087714816) != 0):
                self.state = 152
                self.condicion()
                self.state = 153
                self.match(gramaticaParser.T__0)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 154
                    self.comentarioSimple()


                self.state = 161
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
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.predicado()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.comparacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
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
            self.state = 167
            self.idName()
            self.state = 168
            self.match(gramaticaParser.T__2)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080374784) != 0):
                self.state = 169
                self.listaArgsPredicado()


            self.state = 172
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
            self.state = 174
            self.paramPredicado()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 175
                self.match(gramaticaParser.T__4)
                self.state = 176
                self.paramPredicado()
                self.state = 181
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

        def STRING(self):
            return self.getToken(gramaticaParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(gramaticaParser.BOOLEAN, 0)

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
            self.state = 182
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2080374784) != 0)):
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
            self.state = 184
            self.operando()
            self.state = 185
            self.match(gramaticaParser.OpComp)
            self.state = 186
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
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = gramaticaParser.OperandoVarAttrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(gramaticaParser.VARIABLE)
                self.state = 189
                self.match(gramaticaParser.T__13)
                self.state = 190
                self.idName()
                pass

            elif la_ == 2:
                localctx = gramaticaParser.OperandoIndAttrContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(gramaticaParser.INDIVIDUO)
                self.state = 192
                self.match(gramaticaParser.T__13)
                self.state = 193
                self.idName()
                pass

            elif la_ == 3:
                localctx = gramaticaParser.OperandoIndContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.match(gramaticaParser.INDIVIDUO)
                pass

            elif la_ == 4:
                localctx = gramaticaParser.OperandoVarContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.match(gramaticaParser.VARIABLE)
                pass

            elif la_ == 5:
                localctx = gramaticaParser.OperandoNumContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 196
                self.match(gramaticaParser.NUMBER)
                pass

            elif la_ == 6:
                localctx = gramaticaParser.OperandoStrContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 197
                self.match(gramaticaParser.STRING)
                pass

            elif la_ == 7:
                localctx = gramaticaParser.OperandoBoolContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 198
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
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = gramaticaParser.OpOrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(gramaticaParser.OR)
                self.state = 202
                self.match(gramaticaParser.T__2)
                self.state = 203
                self.listaCondiciones()
                self.state = 204
                self.match(gramaticaParser.T__3)
                pass
            elif token in [21]:
                localctx = gramaticaParser.OpAndContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(gramaticaParser.AND)
                self.state = 207
                self.match(gramaticaParser.T__2)
                self.state = 208
                self.listaCondiciones()
                self.state = 209
                self.match(gramaticaParser.T__3)
                pass
            elif token in [22]:
                localctx = gramaticaParser.OpNotContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 211
                self.match(gramaticaParser.NOT)
                self.state = 212
                self.match(gramaticaParser.T__2)
                self.state = 213
                self.condicion()
                self.state = 214
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
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1610645504) != 0):
                self.state = 218
                self.consecuencia()
                self.state = 219
                self.match(gramaticaParser.T__0)
                self.state = 221
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 220
                    self.comentarioSimple()


                self.state = 227
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
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.borrado()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
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
            self.state = 233
            self.operandoIzq()
            self.state = 234
            self.match(gramaticaParser.OpAsign)
            self.state = 235
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
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(gramaticaParser.VARIABLE)
                self.state = 238
                self.match(gramaticaParser.T__13)
                self.state = 239
                self.idName()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(gramaticaParser.INDIVIDUO)
                self.state = 241
                self.match(gramaticaParser.T__13)
                self.state = 242
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
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.operandoIzq()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
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
            self.state = 249
            self.match(gramaticaParser.T__14)
            self.state = 250
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
            self.state = 252
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 253
            self.idName()
            self.state = 254
            self.match(gramaticaParser.T__2)
            self.state = 255
            self.argLit()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 256
                self.match(gramaticaParser.T__4)
                self.state = 257
                self.argLit()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 263
            self.match(gramaticaParser.T__3)
            self.state = 264
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
            self.state = 266
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
            self.state = 268
            self.match(gramaticaParser.T__17)
            self.state = 269
            self.idName()
            self.state = 270
            self.match(gramaticaParser.T__2)
            self.state = 271
            self.argLit()
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 272
                self.match(gramaticaParser.T__4)
                self.state = 273
                self.argLit()
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 279
            self.match(gramaticaParser.T__3)
            self.state = 280
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
            self.state = 282
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
            self.state = 284
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
            self.state = 286
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





