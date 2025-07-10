// Generated from d:/source/Universidad/TFG/gramatica.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link gramaticaParser}.
 */
public interface gramaticaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(gramaticaParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(gramaticaParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#imports}.
	 * @param ctx the parse tree
	 */
	void enterImports(gramaticaParser.ImportsContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#imports}.
	 * @param ctx the parse tree
	 */
	void exitImports(gramaticaParser.ImportsContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#elemento}.
	 * @param ctx the parse tree
	 */
	void enterElemento(gramaticaParser.ElementoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#elemento}.
	 * @param ctx the parse tree
	 */
	void exitElemento(gramaticaParser.ElementoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracion(gramaticaParser.DeclaracionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracion(gramaticaParser.DeclaracionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#declCategoria}.
	 * @param ctx the parse tree
	 */
	void enterDeclCategoria(gramaticaParser.DeclCategoriaContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#declCategoria}.
	 * @param ctx the parse tree
	 */
	void exitDeclCategoria(gramaticaParser.DeclCategoriaContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#listaAtributos}.
	 * @param ctx the parse tree
	 */
	void enterListaAtributos(gramaticaParser.ListaAtributosContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#listaAtributos}.
	 * @param ctx the parse tree
	 */
	void exitListaAtributos(gramaticaParser.ListaAtributosContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#atributo}.
	 * @param ctx the parse tree
	 */
	void enterAtributo(gramaticaParser.AtributoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#atributo}.
	 * @param ctx the parse tree
	 */
	void exitAtributo(gramaticaParser.AtributoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#tipoBasico}.
	 * @param ctx the parse tree
	 */
	void enterTipoBasico(gramaticaParser.TipoBasicoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#tipoBasico}.
	 * @param ctx the parse tree
	 */
	void exitTipoBasico(gramaticaParser.TipoBasicoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#declProposicion}.
	 * @param ctx the parse tree
	 */
	void enterDeclProposicion(gramaticaParser.DeclProposicionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#declProposicion}.
	 * @param ctx the parse tree
	 */
	void exitDeclProposicion(gramaticaParser.DeclProposicionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#bloquePropiedades}.
	 * @param ctx the parse tree
	 */
	void enterBloquePropiedades(gramaticaParser.BloquePropiedadesContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#bloquePropiedades}.
	 * @param ctx the parse tree
	 */
	void exitBloquePropiedades(gramaticaParser.BloquePropiedadesContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#listaIdentificadores}.
	 * @param ctx the parse tree
	 */
	void enterListaIdentificadores(gramaticaParser.ListaIdentificadoresContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#listaIdentificadores}.
	 * @param ctx the parse tree
	 */
	void exitListaIdentificadores(gramaticaParser.ListaIdentificadoresContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#listaPropiedades}.
	 * @param ctx the parse tree
	 */
	void enterListaPropiedades(gramaticaParser.ListaPropiedadesContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#listaPropiedades}.
	 * @param ctx the parse tree
	 */
	void exitListaPropiedades(gramaticaParser.ListaPropiedadesContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#accion}.
	 * @param ctx the parse tree
	 */
	void enterAccion(gramaticaParser.AccionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#accion}.
	 * @param ctx the parse tree
	 */
	void exitAccion(gramaticaParser.AccionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#listaParams}.
	 * @param ctx the parse tree
	 */
	void enterListaParams(gramaticaParser.ListaParamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#listaParams}.
	 * @param ctx the parse tree
	 */
	void exitListaParams(gramaticaParser.ListaParamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#listaCondiciones}.
	 * @param ctx the parse tree
	 */
	void enterListaCondiciones(gramaticaParser.ListaCondicionesContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#listaCondiciones}.
	 * @param ctx the parse tree
	 */
	void exitListaCondiciones(gramaticaParser.ListaCondicionesContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#condicion}.
	 * @param ctx the parse tree
	 */
	void enterCondicion(gramaticaParser.CondicionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#condicion}.
	 * @param ctx the parse tree
	 */
	void exitCondicion(gramaticaParser.CondicionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#condicionFuncion}.
	 * @param ctx the parse tree
	 */
	void enterCondicionFuncion(gramaticaParser.CondicionFuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#condicionFuncion}.
	 * @param ctx the parse tree
	 */
	void exitCondicionFuncion(gramaticaParser.CondicionFuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#asignacionVariable}.
	 * @param ctx the parse tree
	 */
	void enterAsignacionVariable(gramaticaParser.AsignacionVariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#asignacionVariable}.
	 * @param ctx the parse tree
	 */
	void exitAsignacionVariable(gramaticaParser.AsignacionVariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#predicado}.
	 * @param ctx the parse tree
	 */
	void enterPredicado(gramaticaParser.PredicadoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#predicado}.
	 * @param ctx the parse tree
	 */
	void exitPredicado(gramaticaParser.PredicadoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#listaArgsPredicado}.
	 * @param ctx the parse tree
	 */
	void enterListaArgsPredicado(gramaticaParser.ListaArgsPredicadoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#listaArgsPredicado}.
	 * @param ctx the parse tree
	 */
	void exitListaArgsPredicado(gramaticaParser.ListaArgsPredicadoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#paramPredicado}.
	 * @param ctx the parse tree
	 */
	void enterParamPredicado(gramaticaParser.ParamPredicadoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#paramPredicado}.
	 * @param ctx the parse tree
	 */
	void exitParamPredicado(gramaticaParser.ParamPredicadoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#comparacion}.
	 * @param ctx the parse tree
	 */
	void enterComparacion(gramaticaParser.ComparacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#comparacion}.
	 * @param ctx the parse tree
	 */
	void exitComparacion(gramaticaParser.ComparacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#operando}.
	 * @param ctx the parse tree
	 */
	void enterOperando(gramaticaParser.OperandoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#operando}.
	 * @param ctx the parse tree
	 */
	void exitOperando(gramaticaParser.OperandoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#funcion}.
	 * @param ctx the parse tree
	 */
	void enterFuncion(gramaticaParser.FuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#funcion}.
	 * @param ctx the parse tree
	 */
	void exitFuncion(gramaticaParser.FuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#listaArgsFuncion}.
	 * @param ctx the parse tree
	 */
	void enterListaArgsFuncion(gramaticaParser.ListaArgsFuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#listaArgsFuncion}.
	 * @param ctx the parse tree
	 */
	void exitListaArgsFuncion(gramaticaParser.ListaArgsFuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#paramFuncion}.
	 * @param ctx the parse tree
	 */
	void enterParamFuncion(gramaticaParser.ParamFuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#paramFuncion}.
	 * @param ctx the parse tree
	 */
	void exitParamFuncion(gramaticaParser.ParamFuncionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code opOr}
	 * labeled alternative in {@link gramaticaParser#operacionLogica}.
	 * @param ctx the parse tree
	 */
	void enterOpOr(gramaticaParser.OpOrContext ctx);
	/**
	 * Exit a parse tree produced by the {@code opOr}
	 * labeled alternative in {@link gramaticaParser#operacionLogica}.
	 * @param ctx the parse tree
	 */
	void exitOpOr(gramaticaParser.OpOrContext ctx);
	/**
	 * Enter a parse tree produced by the {@code opAnd}
	 * labeled alternative in {@link gramaticaParser#operacionLogica}.
	 * @param ctx the parse tree
	 */
	void enterOpAnd(gramaticaParser.OpAndContext ctx);
	/**
	 * Exit a parse tree produced by the {@code opAnd}
	 * labeled alternative in {@link gramaticaParser#operacionLogica}.
	 * @param ctx the parse tree
	 */
	void exitOpAnd(gramaticaParser.OpAndContext ctx);
	/**
	 * Enter a parse tree produced by the {@code opNot}
	 * labeled alternative in {@link gramaticaParser#operacionLogica}.
	 * @param ctx the parse tree
	 */
	void enterOpNot(gramaticaParser.OpNotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code opNot}
	 * labeled alternative in {@link gramaticaParser#operacionLogica}.
	 * @param ctx the parse tree
	 */
	void exitOpNot(gramaticaParser.OpNotContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#listaConsecuencias}.
	 * @param ctx the parse tree
	 */
	void enterListaConsecuencias(gramaticaParser.ListaConsecuenciasContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#listaConsecuencias}.
	 * @param ctx the parse tree
	 */
	void exitListaConsecuencias(gramaticaParser.ListaConsecuenciasContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#consecuencia}.
	 * @param ctx the parse tree
	 */
	void enterConsecuencia(gramaticaParser.ConsecuenciaContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#consecuencia}.
	 * @param ctx the parse tree
	 */
	void exitConsecuencia(gramaticaParser.ConsecuenciaContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(gramaticaParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(gramaticaParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#operandoIzq}.
	 * @param ctx the parse tree
	 */
	void enterOperandoIzq(gramaticaParser.OperandoIzqContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#operandoIzq}.
	 * @param ctx the parse tree
	 */
	void exitOperandoIzq(gramaticaParser.OperandoIzqContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#operandoDrc}.
	 * @param ctx the parse tree
	 */
	void enterOperandoDrc(gramaticaParser.OperandoDrcContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#operandoDrc}.
	 * @param ctx the parse tree
	 */
	void exitOperandoDrc(gramaticaParser.OperandoDrcContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#borrado}.
	 * @param ctx the parse tree
	 */
	void enterBorrado(gramaticaParser.BorradoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#borrado}.
	 * @param ctx the parse tree
	 */
	void exitBorrado(gramaticaParser.BorradoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#inicializacion}.
	 * @param ctx the parse tree
	 */
	void enterInicializacion(gramaticaParser.InicializacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#inicializacion}.
	 * @param ctx the parse tree
	 */
	void exitInicializacion(gramaticaParser.InicializacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#bloqueValores}.
	 * @param ctx the parse tree
	 */
	void enterBloqueValores(gramaticaParser.BloqueValoresContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#bloqueValores}.
	 * @param ctx the parse tree
	 */
	void exitBloqueValores(gramaticaParser.BloqueValoresContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#listaParejasValor}.
	 * @param ctx the parse tree
	 */
	void enterListaParejasValor(gramaticaParser.ListaParejasValorContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#listaParejasValor}.
	 * @param ctx the parse tree
	 */
	void exitListaParejasValor(gramaticaParser.ListaParejasValorContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#parejaValor}.
	 * @param ctx the parse tree
	 */
	void enterParejaValor(gramaticaParser.ParejaValorContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#parejaValor}.
	 * @param ctx the parse tree
	 */
	void exitParejaValor(gramaticaParser.ParejaValorContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#valor}.
	 * @param ctx the parse tree
	 */
	void enterValor(gramaticaParser.ValorContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#valor}.
	 * @param ctx the parse tree
	 */
	void exitValor(gramaticaParser.ValorContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#argLit}.
	 * @param ctx the parse tree
	 */
	void enterArgLit(gramaticaParser.ArgLitContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#argLit}.
	 * @param ctx the parse tree
	 */
	void exitArgLit(gramaticaParser.ArgLitContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#ejecucion}.
	 * @param ctx the parse tree
	 */
	void enterEjecucion(gramaticaParser.EjecucionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#ejecucion}.
	 * @param ctx the parse tree
	 */
	void exitEjecucion(gramaticaParser.EjecucionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#listaArgLit}.
	 * @param ctx the parse tree
	 */
	void enterListaArgLit(gramaticaParser.ListaArgLitContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#listaArgLit}.
	 * @param ctx the parse tree
	 */
	void exitListaArgLit(gramaticaParser.ListaArgLitContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#comentarioSimple}.
	 * @param ctx the parse tree
	 */
	void enterComentarioSimple(gramaticaParser.ComentarioSimpleContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#comentarioSimple}.
	 * @param ctx the parse tree
	 */
	void exitComentarioSimple(gramaticaParser.ComentarioSimpleContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#comentarioMultilineo}.
	 * @param ctx the parse tree
	 */
	void enterComentarioMultilineo(gramaticaParser.ComentarioMultilineoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#comentarioMultilineo}.
	 * @param ctx the parse tree
	 */
	void exitComentarioMultilineo(gramaticaParser.ComentarioMultilineoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#idName}.
	 * @param ctx the parse tree
	 */
	void enterIdName(gramaticaParser.IdNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#idName}.
	 * @param ctx the parse tree
	 */
	void exitIdName(gramaticaParser.IdNameContext ctx);
}