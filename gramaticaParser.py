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
        4,1,28,265,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,75,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,83,8,2,1,3,1,3,1,3,1,3,3,3,89,8,3,1,3,1,3,1,4,1,4,1,4,5,4,96,
        8,4,10,4,12,4,99,9,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,3,7,
        111,8,7,1,7,1,7,1,8,1,8,1,8,5,8,118,8,8,10,8,12,8,121,9,8,1,9,1,
        9,1,9,1,9,3,9,127,8,9,1,9,1,9,1,9,3,9,132,8,9,1,9,1,9,1,9,1,9,1,
        9,1,10,1,10,1,10,5,10,142,8,10,10,10,12,10,145,9,10,1,11,1,11,1,
        11,3,11,150,8,11,5,11,152,8,11,10,11,12,11,155,9,11,1,12,1,12,3,
        12,159,8,12,1,13,1,13,1,13,3,13,164,8,13,1,13,1,13,1,14,1,14,1,14,
        5,14,171,8,14,10,14,12,14,174,9,14,1,15,1,15,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,193,
        8,17,1,18,1,18,1,18,3,18,198,8,18,5,18,200,8,18,10,18,12,18,203,
        9,18,1,19,1,19,1,19,3,19,208,8,19,1,20,1,20,1,20,1,20,1,21,1,21,
        1,21,1,21,1,21,1,21,3,21,220,8,21,1,22,1,22,3,22,224,8,22,1,23,1,
        23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,5,24,235,8,24,10,24,12,24,
        238,9,24,1,24,1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,
        5,26,251,8,26,10,26,12,26,254,9,26,1,26,1,26,1,26,1,27,1,27,1,28,
        1,28,1,29,1,29,1,29,0,0,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,0,4,1,0,7,9,1,0,
        26,27,1,0,16,17,1,0,24,25,267,0,63,1,0,0,0,2,74,1,0,0,0,4,82,1,0,
        0,0,6,84,1,0,0,0,8,92,1,0,0,0,10,100,1,0,0,0,12,104,1,0,0,0,14,106,
        1,0,0,0,16,114,1,0,0,0,18,122,1,0,0,0,20,138,1,0,0,0,22,153,1,0,
        0,0,24,158,1,0,0,0,26,160,1,0,0,0,28,167,1,0,0,0,30,175,1,0,0,0,
        32,177,1,0,0,0,34,192,1,0,0,0,36,201,1,0,0,0,38,207,1,0,0,0,40,209,
        1,0,0,0,42,219,1,0,0,0,44,223,1,0,0,0,46,225,1,0,0,0,48,228,1,0,
        0,0,50,242,1,0,0,0,52,244,1,0,0,0,54,258,1,0,0,0,56,260,1,0,0,0,
        58,262,1,0,0,0,60,62,3,2,1,0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,
        0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,5,0,0,1,67,
        1,1,0,0,0,68,75,3,4,2,0,69,75,3,18,9,0,70,75,3,48,24,0,71,75,3,52,
        26,0,72,75,3,54,27,0,73,75,3,56,28,0,74,68,1,0,0,0,74,69,1,0,0,0,
        74,70,1,0,0,0,74,71,1,0,0,0,74,72,1,0,0,0,74,73,1,0,0,0,75,3,1,0,
        0,0,76,77,3,6,3,0,77,78,5,1,0,0,78,83,1,0,0,0,79,80,3,14,7,0,80,
        81,5,1,0,0,81,83,1,0,0,0,82,76,1,0,0,0,82,79,1,0,0,0,83,5,1,0,0,
        0,84,85,5,2,0,0,85,86,3,58,29,0,86,88,5,3,0,0,87,89,3,8,4,0,88,87,
        1,0,0,0,88,89,1,0,0,0,89,90,1,0,0,0,90,91,5,4,0,0,91,7,1,0,0,0,92,
        97,3,10,5,0,93,94,5,5,0,0,94,96,3,10,5,0,95,93,1,0,0,0,96,99,1,0,
        0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,9,1,0,0,0,99,97,1,0,0,0,100,101,
        3,58,29,0,101,102,5,6,0,0,102,103,3,12,6,0,103,11,1,0,0,0,104,105,
        7,0,0,0,105,13,1,0,0,0,106,107,5,10,0,0,107,108,3,58,29,0,108,110,
        5,3,0,0,109,111,3,16,8,0,110,109,1,0,0,0,110,111,1,0,0,0,111,112,
        1,0,0,0,112,113,5,4,0,0,113,15,1,0,0,0,114,119,3,58,29,0,115,116,
        5,5,0,0,116,118,3,58,29,0,117,115,1,0,0,0,118,121,1,0,0,0,119,117,
        1,0,0,0,119,120,1,0,0,0,120,17,1,0,0,0,121,119,1,0,0,0,122,123,5,
        11,0,0,123,124,3,58,29,0,124,126,5,3,0,0,125,127,3,20,10,0,126,125,
        1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,129,5,4,0,0,129,131,
        5,6,0,0,130,132,3,56,28,0,131,130,1,0,0,0,131,132,1,0,0,0,132,133,
        1,0,0,0,133,134,5,12,0,0,134,135,3,22,11,0,135,136,5,13,0,0,136,
        137,3,36,18,0,137,19,1,0,0,0,138,143,3,58,29,0,139,140,5,5,0,0,140,
        142,3,58,29,0,141,139,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,
        144,1,0,0,0,144,21,1,0,0,0,145,143,1,0,0,0,146,147,3,24,12,0,147,
        149,5,1,0,0,148,150,3,54,27,0,149,148,1,0,0,0,149,150,1,0,0,0,150,
        152,1,0,0,0,151,146,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,
        154,1,0,0,0,154,23,1,0,0,0,155,153,1,0,0,0,156,159,3,26,13,0,157,
        159,3,32,16,0,158,156,1,0,0,0,158,157,1,0,0,0,159,25,1,0,0,0,160,
        161,3,58,29,0,161,163,5,3,0,0,162,164,3,28,14,0,163,162,1,0,0,0,
        163,164,1,0,0,0,164,165,1,0,0,0,165,166,5,4,0,0,166,27,1,0,0,0,167,
        172,3,30,15,0,168,169,5,5,0,0,169,171,3,30,15,0,170,168,1,0,0,0,
        171,174,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,29,1,0,0,0,174,
        172,1,0,0,0,175,176,7,1,0,0,176,31,1,0,0,0,177,178,3,34,17,0,178,
        179,5,19,0,0,179,180,3,34,17,0,180,33,1,0,0,0,181,182,5,27,0,0,182,
        183,5,14,0,0,183,193,3,58,29,0,184,185,5,26,0,0,185,186,5,14,0,0,
        186,193,3,58,29,0,187,193,5,26,0,0,188,193,5,27,0,0,189,193,5,25,
        0,0,190,193,5,24,0,0,191,193,5,23,0,0,192,181,1,0,0,0,192,184,1,
        0,0,0,192,187,1,0,0,0,192,188,1,0,0,0,192,189,1,0,0,0,192,190,1,
        0,0,0,192,191,1,0,0,0,193,35,1,0,0,0,194,195,3,38,19,0,195,197,5,
        1,0,0,196,198,3,54,27,0,197,196,1,0,0,0,197,198,1,0,0,0,198,200,
        1,0,0,0,199,194,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,
        1,0,0,0,202,37,1,0,0,0,203,201,1,0,0,0,204,208,3,40,20,0,205,208,
        3,46,23,0,206,208,3,26,13,0,207,204,1,0,0,0,207,205,1,0,0,0,207,
        206,1,0,0,0,208,39,1,0,0,0,209,210,3,42,21,0,210,211,5,20,0,0,211,
        212,3,44,22,0,212,41,1,0,0,0,213,214,5,27,0,0,214,215,5,14,0,0,215,
        220,3,58,29,0,216,217,5,26,0,0,217,218,5,14,0,0,218,220,3,58,29,
        0,219,213,1,0,0,0,219,216,1,0,0,0,220,43,1,0,0,0,221,224,3,42,21,
        0,222,224,5,25,0,0,223,221,1,0,0,0,223,222,1,0,0,0,224,45,1,0,0,
        0,225,226,5,15,0,0,226,227,3,26,13,0,227,47,1,0,0,0,228,229,7,2,
        0,0,229,230,3,58,29,0,230,231,5,3,0,0,231,236,3,50,25,0,232,233,
        5,5,0,0,233,235,3,50,25,0,234,232,1,0,0,0,235,238,1,0,0,0,236,234,
        1,0,0,0,236,237,1,0,0,0,237,239,1,0,0,0,238,236,1,0,0,0,239,240,
        5,4,0,0,240,241,5,1,0,0,241,49,1,0,0,0,242,243,7,3,0,0,243,51,1,
        0,0,0,244,245,5,18,0,0,245,246,3,58,29,0,246,247,5,3,0,0,247,252,
        3,50,25,0,248,249,5,5,0,0,249,251,3,50,25,0,250,248,1,0,0,0,251,
        254,1,0,0,0,252,250,1,0,0,0,252,253,1,0,0,0,253,255,1,0,0,0,254,
        252,1,0,0,0,255,256,5,4,0,0,256,257,5,1,0,0,257,53,1,0,0,0,258,259,
        5,21,0,0,259,55,1,0,0,0,260,261,5,22,0,0,261,57,1,0,0,0,262,263,
        7,1,0,0,263,59,1,0,0,0,23,63,74,82,88,97,110,119,126,131,143,149,
        153,158,163,172,192,197,201,207,219,223,236,252
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'Categoria'", "'('", "')'", "','", 
                     "':'", "'int'", "'str'", "'bool'", "'Prop'", "'Accion'", 
                     "'Condiciones:'", "'Consecuencias:'", "'.'", "'DEL'", 
                     "'new'", "'add'", "'Run'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "OpComp", "OpAsign", 
                      "COMMENT_SIMPLE", "COMMENT_MULTI", "BOOLEAN", "STRING", 
                      "NUMBER", "INDIVIDUO", "VARIABLE", "WS" ]

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
    RULE_listaConsecuencias = 18
    RULE_consecuencia = 19
    RULE_asignacion = 20
    RULE_operandoIzq = 21
    RULE_operandoDrc = 22
    RULE_borrado = 23
    RULE_inicializacion = 24
    RULE_argLit = 25
    RULE_ejecucion = 26
    RULE_comentarioSimple = 27
    RULE_comentarioMultilineo = 28
    RULE_idName = 29

    ruleNames =  [ "programa", "elemento", "declaracion", "declCategoria", 
                   "listaAtributos", "atributo", "tipoBasico", "declProposicion", 
                   "listaIdentificadores", "accion", "listaParams", "listaCondiciones", 
                   "condicion", "predicado", "listaArgsPredicado", "paramPredicado", 
                   "comparacion", "operando", "listaConsecuencias", "consecuencia", 
                   "asignacion", "operandoIzq", "operandoDrc", "borrado", 
                   "inicializacion", "argLit", "ejecucion", "comentarioSimple", 
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
    OpAsign=20
    COMMENT_SIMPLE=21
    COMMENT_MULTI=22
    BOOLEAN=23
    STRING=24
    NUMBER=25
    INDIVIDUO=26
    VARIABLE=27
    WS=28

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
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6753284) != 0):
                self.state = 60
                self.elemento()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
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
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.declaracion()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.accion()
                pass
            elif token in [16, 17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.inicializacion()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.ejecucion()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.comentarioSimple()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
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
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.declCategoria()
                self.state = 77
                self.match(gramaticaParser.T__0)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.declProposicion()
                self.state = 80
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
            self.state = 84
            self.match(gramaticaParser.T__1)
            self.state = 85
            self.idName()
            self.state = 86
            self.match(gramaticaParser.T__2)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26 or _la==27:
                self.state = 87
                self.listaAtributos()


            self.state = 90
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
            self.state = 92
            self.atributo()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 93
                self.match(gramaticaParser.T__4)
                self.state = 94
                self.atributo()
                self.state = 99
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
            self.state = 100
            self.idName()
            self.state = 101
            self.match(gramaticaParser.T__5)
            self.state = 102
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
            self.state = 104
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
            self.state = 106
            self.match(gramaticaParser.T__9)
            self.state = 107
            self.idName()
            self.state = 108
            self.match(gramaticaParser.T__2)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26 or _la==27:
                self.state = 109
                self.listaIdentificadores()


            self.state = 112
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
            self.state = 114
            self.idName()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 115
                self.match(gramaticaParser.T__4)
                self.state = 116
                self.idName()
                self.state = 121
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
            self.state = 122
            self.match(gramaticaParser.T__10)
            self.state = 123
            self.idName()
            self.state = 124
            self.match(gramaticaParser.T__2)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26 or _la==27:
                self.state = 125
                self.listaParams()


            self.state = 128
            self.match(gramaticaParser.T__3)
            self.state = 129
            self.match(gramaticaParser.T__5)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 130
                self.comentarioMultilineo()


            self.state = 133
            self.match(gramaticaParser.T__11)
            self.state = 134
            self.listaCondiciones()
            self.state = 135
            self.match(gramaticaParser.T__12)
            self.state = 136
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
            self.state = 138
            self.idName()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 139
                self.match(gramaticaParser.T__4)
                self.state = 140
                self.idName()
                self.state = 145
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
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 260046848) != 0):
                self.state = 146
                self.condicion()
                self.state = 147
                self.match(gramaticaParser.T__0)
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 148
                    self.comentarioSimple()


                self.state = 155
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
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.predicado()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.comparacion()
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
            self.state = 160
            self.idName()
            self.state = 161
            self.match(gramaticaParser.T__2)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26 or _la==27:
                self.state = 162
                self.listaArgsPredicado()


            self.state = 165
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
            self.state = 167
            self.paramPredicado()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 168
                self.match(gramaticaParser.T__4)
                self.state = 169
                self.paramPredicado()
                self.state = 174
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
            self.state = 175
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
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
            self.state = 177
            self.operando()
            self.state = 178
            self.match(gramaticaParser.OpComp)
            self.state = 179
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
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = gramaticaParser.OperandoVarAttrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(gramaticaParser.VARIABLE)
                self.state = 182
                self.match(gramaticaParser.T__13)
                self.state = 183
                self.idName()
                pass

            elif la_ == 2:
                localctx = gramaticaParser.OperandoIndAttrContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(gramaticaParser.INDIVIDUO)
                self.state = 185
                self.match(gramaticaParser.T__13)
                self.state = 186
                self.idName()
                pass

            elif la_ == 3:
                localctx = gramaticaParser.OperandoIndContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.match(gramaticaParser.INDIVIDUO)
                pass

            elif la_ == 4:
                localctx = gramaticaParser.OperandoVarContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                self.match(gramaticaParser.VARIABLE)
                pass

            elif la_ == 5:
                localctx = gramaticaParser.OperandoNumContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 189
                self.match(gramaticaParser.NUMBER)
                pass

            elif la_ == 6:
                localctx = gramaticaParser.OperandoStrContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 190
                self.match(gramaticaParser.STRING)
                pass

            elif la_ == 7:
                localctx = gramaticaParser.OperandoBoolContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 191
                self.match(gramaticaParser.BOOLEAN)
                pass


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
        self.enterRule(localctx, 36, self.RULE_listaConsecuencias)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 201359360) != 0):
                self.state = 194
                self.consecuencia()
                self.state = 195
                self.match(gramaticaParser.T__0)
                self.state = 197
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 196
                    self.comentarioSimple()


                self.state = 203
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
        self.enterRule(localctx, 38, self.RULE_consecuencia)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.borrado()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 206
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
        self.enterRule(localctx, 40, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.operandoIzq()
            self.state = 210
            self.match(gramaticaParser.OpAsign)
            self.state = 211
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
        self.enterRule(localctx, 42, self.RULE_operandoIzq)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(gramaticaParser.VARIABLE)
                self.state = 214
                self.match(gramaticaParser.T__13)
                self.state = 215
                self.idName()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(gramaticaParser.INDIVIDUO)
                self.state = 217
                self.match(gramaticaParser.T__13)
                self.state = 218
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
        self.enterRule(localctx, 44, self.RULE_operandoDrc)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.operandoIzq()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
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
        self.enterRule(localctx, 46, self.RULE_borrado)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(gramaticaParser.T__14)
            self.state = 226
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
        self.enterRule(localctx, 48, self.RULE_inicializacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 229
            self.idName()
            self.state = 230
            self.match(gramaticaParser.T__2)
            self.state = 231
            self.argLit()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 232
                self.match(gramaticaParser.T__4)
                self.state = 233
                self.argLit()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 239
            self.match(gramaticaParser.T__3)
            self.state = 240
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
        self.enterRule(localctx, 50, self.RULE_argLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
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
        self.enterRule(localctx, 52, self.RULE_ejecucion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(gramaticaParser.T__17)
            self.state = 245
            self.idName()
            self.state = 246
            self.match(gramaticaParser.T__2)
            self.state = 247
            self.argLit()
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 248
                self.match(gramaticaParser.T__4)
                self.state = 249
                self.argLit()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 255
            self.match(gramaticaParser.T__3)
            self.state = 256
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
        self.enterRule(localctx, 54, self.RULE_comentarioSimple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
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
        self.enterRule(localctx, 56, self.RULE_comentarioMultilineo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
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
        self.enterRule(localctx, 58, self.RULE_idName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
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





