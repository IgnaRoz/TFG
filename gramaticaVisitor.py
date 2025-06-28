# Generated from d:/source/Universidad/TFG/gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#programa.
    def visitPrograma(self, ctx:gramaticaParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#elemento.
    def visitElemento(self, ctx:gramaticaParser.ElementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#declaracion.
    def visitDeclaracion(self, ctx:gramaticaParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#declCategoria.
    def visitDeclCategoria(self, ctx:gramaticaParser.DeclCategoriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#listaAtributos.
    def visitListaAtributos(self, ctx:gramaticaParser.ListaAtributosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#atributo.
    def visitAtributo(self, ctx:gramaticaParser.AtributoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#tipoBasico.
    def visitTipoBasico(self, ctx:gramaticaParser.TipoBasicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#declProposicion.
    def visitDeclProposicion(self, ctx:gramaticaParser.DeclProposicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#bloquePropiedades.
    def visitBloquePropiedades(self, ctx:gramaticaParser.BloquePropiedadesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#listaIdentificadores.
    def visitListaIdentificadores(self, ctx:gramaticaParser.ListaIdentificadoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#listaPropiedades.
    def visitListaPropiedades(self, ctx:gramaticaParser.ListaPropiedadesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#accion.
    def visitAccion(self, ctx:gramaticaParser.AccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#listaParams.
    def visitListaParams(self, ctx:gramaticaParser.ListaParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#listaCondiciones.
    def visitListaCondiciones(self, ctx:gramaticaParser.ListaCondicionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#condicion.
    def visitCondicion(self, ctx:gramaticaParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#asignacionVariable.
    def visitAsignacionVariable(self, ctx:gramaticaParser.AsignacionVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#predicado.
    def visitPredicado(self, ctx:gramaticaParser.PredicadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#listaArgsPredicado.
    def visitListaArgsPredicado(self, ctx:gramaticaParser.ListaArgsPredicadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#paramPredicado.
    def visitParamPredicado(self, ctx:gramaticaParser.ParamPredicadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#comparacion.
    def visitComparacion(self, ctx:gramaticaParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operandoVarAttr.
    def visitOperandoVarAttr(self, ctx:gramaticaParser.OperandoVarAttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operandoIndAttr.
    def visitOperandoIndAttr(self, ctx:gramaticaParser.OperandoIndAttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operandoInd.
    def visitOperandoInd(self, ctx:gramaticaParser.OperandoIndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operandoVar.
    def visitOperandoVar(self, ctx:gramaticaParser.OperandoVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operandoNum.
    def visitOperandoNum(self, ctx:gramaticaParser.OperandoNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operandoStr.
    def visitOperandoStr(self, ctx:gramaticaParser.OperandoStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operandoBool.
    def visitOperandoBool(self, ctx:gramaticaParser.OperandoBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#opOr.
    def visitOpOr(self, ctx:gramaticaParser.OpOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#opAnd.
    def visitOpAnd(self, ctx:gramaticaParser.OpAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#opNot.
    def visitOpNot(self, ctx:gramaticaParser.OpNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#listaConsecuencias.
    def visitListaConsecuencias(self, ctx:gramaticaParser.ListaConsecuenciasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#consecuencia.
    def visitConsecuencia(self, ctx:gramaticaParser.ConsecuenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#asignacion.
    def visitAsignacion(self, ctx:gramaticaParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operandoIzq.
    def visitOperandoIzq(self, ctx:gramaticaParser.OperandoIzqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operandoDrc.
    def visitOperandoDrc(self, ctx:gramaticaParser.OperandoDrcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#borrado.
    def visitBorrado(self, ctx:gramaticaParser.BorradoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#inicializacion.
    def visitInicializacion(self, ctx:gramaticaParser.InicializacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#bloqueValores.
    def visitBloqueValores(self, ctx:gramaticaParser.BloqueValoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#listaParejasValor.
    def visitListaParejasValor(self, ctx:gramaticaParser.ListaParejasValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#parejaValor.
    def visitParejaValor(self, ctx:gramaticaParser.ParejaValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#valor.
    def visitValor(self, ctx:gramaticaParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#argLit.
    def visitArgLit(self, ctx:gramaticaParser.ArgLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ejecucion.
    def visitEjecucion(self, ctx:gramaticaParser.EjecucionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#comentarioSimple.
    def visitComentarioSimple(self, ctx:gramaticaParser.ComentarioSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#comentarioMultilineo.
    def visitComentarioMultilineo(self, ctx:gramaticaParser.ComentarioMultilineoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#idName.
    def visitIdName(self, ctx:gramaticaParser.IdNameContext):
        return self.visitChildren(ctx)



del gramaticaParser