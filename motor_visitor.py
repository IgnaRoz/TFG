from antlr4 import ErrorNode, ParseTreeVisitor, TerminalNode
from antlr4.tree.Tree import ErrorNodeImpl

import logging
from gramaticaVisitor import gramaticaVisitor
from gramaticaParser import gramaticaParser
from motorEjecucion import MotorEjecucion, logger
from base import TipoComparacion, TipoOperacion
from condiciones import CondicionSimple, CondicionComparacion, CondicionLogica, CondicionNegacion, CondicionAsignacion
from consecuencias import (
    ConsecuenciaAsignacion,
    ConsecuenciaEliminacion,
    ConsecuenciaModificacion,
)
from reglas import Regla


def _texto_string(token: str) -> str:
    if token.startswith('"') or token.startswith('\u201C'):
        return token[1:-1]
    return token


class MotorVisitor(gramaticaVisitor):
    def __init__(self, motor: MotorEjecucion):
        super().__init__()
        self.motor = motor

    def visitPrograma(self, ctx):
        for child in ctx.getChildren():
            if isinstance(child, gramaticaParser.ElementoContext):
                try:
                    self.visitElemento(child)
                except ValueError as e:
                    start = child.start.line
                    end = getattr(child.stop, "line", start)
                    logger.error(f"Error de sintaxis entre lineas {start}-{end}: {e}")

            elif isinstance(child, TerminalNode):
                # Manejar nodos terminales si es necesario
                pass
            else:
                logger.warning(f"Elemento desconocido: {child.getText()}")
        

    # Helpers --------------------------------------------------------------
    def _parse_arg_lit(self, ctx: gramaticaParser.ArgLitContext):
        text = ctx.getText()
        if ctx.NUMBER():
            return int(text)
        return _texto_string(text)

    def _parse_operando(self, ctx):
        # Puede ser OperandoContext, OperandoIzqContext o OperandoDrcContext

                
        if getattr(ctx, 'VARIABLE', None):
            var = ctx.VARIABLE().getText()
            if ctx.getChildCount() == 3:  # VARIABLE '.' idName
                attr = ctx.idName().getText()
                return (var, attr)
            return var
        if getattr(ctx, 'INDIVIDUO', None):
            ind = ctx.INDIVIDUO().getText()
            if ctx.getChildCount() == 3:
                attr = ctx.idName().getText()
                return (ind, attr)
            return ind
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        if ctx.STRING():
            return _texto_string(ctx.STRING().getText())
        if ctx.BOOLEAN():
            return ctx.BOOLEAN().getText() == 'True'
        return ctx.getText()

    def _collect_vars(self, *values):
        vars_ = []
        for v in values:
            if isinstance(v, tuple):
                token = v[0]
            else:
                token = v
            if isinstance(token, str) and token[:1].isupper():
                if token not in vars_:
                    vars_.append(token)
        return vars_

    def _parse_predicado(self, ctx: gramaticaParser.PredicadoContext):
        nombre = ctx.idName().getText()
        args = []
        if ctx.listaArgsPredicado():
            for p in ctx.listaArgsPredicado().paramPredicado():
                args.append(p.getText())
        return nombre, args

    # Visit helpers -------------------------------------------------------
    def visitListaAtributos(self, ctx: gramaticaParser.ListaAtributosContext):
        valores = []
        for atr in ctx.atributo():
            valores.append(self.visit(atr))
        return valores

    def visitAtributo(self, ctx: gramaticaParser.AtributoContext):
        nombre = ctx.idName().getText()
        tipo_token = ctx.tipoBasico().getText()
        tipo = {"int": int, "str": str, "bool": bool}[tipo_token]
        return nombre, tipo

    def visitListaIdentificadores(self, ctx: gramaticaParser.ListaIdentificadoresContext):
        return [idn.getText() for idn in ctx.idName()]

    # Visitor methods -----------------------------------------------------

    def visitDeclCategoria(self, ctx: gramaticaParser.DeclCategoriaContext):
        if any(isinstance(c, ErrorNodeImpl) for c in (getattr(ctx, 'children', None) or [])):
            raise ValueError(
                f"Error de sintaxis en '{ctx.getText()}' en {ctx.start.line}:{ctx.start.column}"
            )
        self.visit(ctx.idName())  # Asegurarse de que el nombre de la categoría se visite
        nombre = ctx.idName().getText()
        esquema = {}
        if ctx.listaAtributos():
            for n, t in self.visit(ctx.listaAtributos()):
                esquema[n] = t
        try:
            self.motor.crear_categoria(nombre, esquema)
            logger.info(f"[Categoría:{nombre}] Creada con esquema {esquema}")
        except Exception as e:
            logger.error(str(e))
        return None

    def visitDeclCategoria2(self, ctx: gramaticaParser.DeclCategoriaContext):
        nombre = ctx.idName().getText()
        esquema = {}
        if ctx.listaAtributos():
            for n, t in self.visit(ctx.listaAtributos()):
                esquema[n] = t
        try:
            self.motor.crear_categoria(nombre, esquema)
        except Exception as e:
            logger.error(str(e))
        return None

    def visitDeclProposicion(self, ctx: gramaticaParser.DeclProposicionContext):
        nombre = ctx.idName().getText()
        lista_parametros = []
        descripcion = None
        #comprobamos si en el contexto del padre hay un comentario simple
        if ctx.parentCtx and ctx.parentCtx.comentarioSimple():
            descripcion = ctx.parentCtx.comentarioSimple().getText()

        if ctx.listaIdentificadores():
            lista_parametros =self.visit(ctx.listaIdentificadores())
            


        atributos = {}
        if ctx.bloquePropiedades():
            atributos = self.visit(ctx.bloquePropiedades())
        try:
            if descripcion:
                self.motor.crear_proposicion(nombre,lista_parametros, descripcion=descripcion,atributos=atributos)
            else: self.motor.crear_proposicion(nombre, lista_parametros,atributos=atributos)
        except Exception as e:
            logger.error(str(e))
        return None
    
    def visitBloquePropiedades(self, ctx):
        if any(isinstance(c, ErrorNodeImpl) for c in (getattr(ctx, 'children', None) or [])):
            raise ValueError(
                f"Error de sintaxis en '{ctx.getText()}' en {ctx.start.line}:{ctx.start.column}"
            )
        if ctx.listaPropiedades():
            return self.visit(ctx.listaPropiedades())
        else:
            return []
        
    def visitListaPropiedades(self, ctx):
        if any(isinstance(c, ErrorNodeImpl) for c in (getattr(ctx, 'children', None) or [])):
            raise ValueError(
                f"Error de sintaxis en '{ctx.getText()}' en {ctx.start.line}:{ctx.start.column}"
            )
        atributos =[]
        for atributo in ctx.idName():
            atributos.append(atributo.getText())
        return atributos



    def visitInicializacion(self, ctx: gramaticaParser.InicializacionContext):
        modo = ctx.getChild(0).getText()
        nombre = ctx.idName().getText()
        args = [self._parse_arg_lit(a) for a in ctx.argLit()]

        atributos={}
        if ctx.bloqueValores():
            atributos = self.visit(ctx.bloqueValores())
        try:
            if modo == 'new':#BORRAR
                self.motor.nuevo_individuo(nombre, args)
            elif modo == 'add':
                #self.motor.add_proposicion(nombre, args,atributos=atributos)
                self.motor.base.proposiciones[nombre].add(tuple(args),atributos=atributos)
        except Exception as e:
            logger.error(str(e))
        return None
    def visitBloqueValores(self, ctx):
         
         if ctx.listaParejasValor():
            retorno = self.visit(ctx.listaParejasValor())

            return retorno 
         return {}   

         #return self.visit(ctx.listaParejasValor()) if ctx.listaParejasValor() else {}
    def visitListaParejasValor(self, ctx):
        return {k: v for k, v in (self.visit(p) for p in ctx.parejaValor())}

    def visitParejaValor(self, ctx):
        nombre =   ctx.idName().getText()
        valor = self.visit(ctx.valor())
        print(valor)
        return nombre,valor
    def visitValor(self, ctx):
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())

        #  STRING → quitar comillas (“…” o "…")
        if ctx.STRING():
            return _texto_string(ctx.STRING().getText())

        #  BOOLEAN → True/False
        if ctx.BOOLEAN():
            return ctx.BOOLEAN().getText().lower() == "true"

        #  idName → nombre tal cual
        if ctx.idName():
            return ctx.idName().getText()

        #  Fallback
        return ctx.getText()
    def visitEjecucion(self, ctx: gramaticaParser.EjecucionContext):
        nombre = ctx.idName().getText()
        args = [self._parse_arg_lit(a) for a in ctx.argLit()]
        try:
            self.motor.ejecutar_accion(nombre, args)
        except Exception as e:
            logger.error(str(e))
        return None

    def visitElemento(self, ctx: gramaticaParser.ElementoContext):
        try:
            return self.visitChildren(ctx) 

        except Exception as e:
            start = ctx.start.line
            end = getattr(ctx.stop, "line", start)
            logger.warning(f"Elemento ignorado entre lineas {start}-{end}")
            raise e # para que el error se propague hacia programa


    
        

    def visitAccion(self, ctx: gramaticaParser.AccionContext):
        if any(isinstance(c, ErrorNodeImpl) for c in (getattr(ctx, 'children', None) or [])):
            raise ValueError(
                f"Error de sintaxis en '{ctx.getText()}' en {ctx.start.line}:{ctx.start.column}"
            )
        descripcion = None
        if ctx.comentarioMultilineo():
            descripcion = ctx.comentarioMultilineo().getText()
        nombre = ctx.idName().getText()
        params = []
        if ctx.listaParams():
            params = [p.getText() for p in ctx.listaParams().idName()]
        condiciones = []
        if ctx.listaCondiciones():
            condiciones = self.visitListaCondiciones(ctx.listaCondiciones())
        if not condiciones:
            #Modificarr el warning, no debe permitir 0 condiciones,pero quizas debe elevar el error
            raise ValueError(
                f"Error de sintaxis en '{ctx.getText()}' en {ctx.start.line}:{ctx.start.column}"
            )
            #pero de este modo no se lanzan los errores en consecuencias
            logger.warning(f"[Acción:{nombre}] No se definieron condiciones, acción ignorada")
            return None
        regla = Regla(nombre, params, condiciones,descripcion)
        consecuencias = []
        if ctx.listaConsecuencias():
            consecuencias = self.visitListaConsecuencias(ctx.listaConsecuencias())  
        if not consecuencias:
            logger.warning(f"[Acción:{nombre}] No se definieron consecuencias, acción ignorada")
            return None
        regla.consecuencias = consecuencias
        try:
            self.motor.add_regla(regla, accion=True)
            logger.info(f"[Acción:{nombre}] Agregada con {len(condiciones)} condiciones y {len(consecuencias)} consecuencias")
        except Exception as e:
            logger.error(str(e))
        return None


    def visitListaCondiciones(self, ctx):
        condiciones = []
        for c in ctx.condicion():
            cond = self.visitCondicion(c)
            if cond:
                condiciones.append(cond)
            
        return condiciones
    def visitCondicion(self, ctx):
#COMPROBAR SI ES UN PREDICADO VALIDO O HACERLO AL REGISTRAR LA REGLA???
        condicion = None
        if ctx.predicado():
            prop, vars_ = self._parse_predicado(ctx.predicado())
            condicion = CondicionSimple(prop, vars_)
        elif ctx.comparacion():
            condicion = self.visitComparacion(ctx.comparacion())
        elif ctx.operacionLogica():
            condicion = self.visitOperacionLogica(ctx.operacionLogica())
        elif ctx.asignacionVariable():
            condicion = self.visitAsignacionVariable(ctx.asignacionVariable())

        return condicion
    def visitOperacionLogica(self, ctx: gramaticaParser.OperacionLogicaContext):
        if any(isinstance(c, ErrorNodeImpl) for c in (getattr(ctx, 'children', None) or [])):
            raise ValueError(
                f"Error de sintaxis en '{ctx.getText()}' en {ctx.start.line}:{ctx.start.column}"
            )
        operador = ctx.start.type
        if operador == gramaticaParser.AND:
            op = "AND"
            condiciones = self.visitListaCondiciones(ctx.listaCondiciones())
            return CondicionLogica(condiciones, op)
        elif operador == gramaticaParser.OR:
            op = "OR"
            condiciones = self.visitListaCondiciones(ctx.listaCondiciones())
            return CondicionLogica(condiciones, op)
        elif operador == gramaticaParser.NOT:
            condicion = self.visitCondicion(ctx.condicion())
            return CondicionNegacion(condicion)
        else:
            raise ValueError(
                f"Operador lógico desconocido '{ctx.getText()}' en {ctx.start.line}:{ctx.start.column}"
            )
    def visitComparacion(self, ctx):
        if any(isinstance(c, ErrorNodeImpl) for c in (getattr(ctx, 'children', None) or [])):
            raise ValueError(
                f"Error de sintaxis en '{ctx.getText()}' en {ctx.start.line}:{ctx.start.column}"
            )
        izq = self._parse_operando(ctx.operando(0))
        der = self._parse_operando(ctx.operando(1))
        op = TipoComparacion(ctx.OpComp().getText())
        vars_ = self._collect_vars(izq, der)
        condicion = CondicionComparacion(izq, op, der, vars_)
        self.visitChildren(ctx)
        return condicion
    

    def visitAsignacionVariable(self, ctx):

        variable_asignacion = ctx.VARIABLE().getText()
        predicado,variables = self._parse_predicado(ctx.predicado())
        condicion = None
        return CondicionAsignacion(variables,variable_asignacion,predicado)
        return super().visitAsignacionVariable(ctx)


    def visitListaConsecuencias(self, ctx: gramaticaParser.ListaConsecuenciasContext):
        consecuencias = []
        for c in ctx.consecuencia():
            cons = self.visit(c)
            if cons:
                consecuencias.append(cons)
        return consecuencias
    def visitConsecuencia(self, ctx):
        consecuencia = None
        if ctx.asignacion():
            asign = ctx.asignacion()
            objetivo  = self._parse_operando(asign.operandoIzq())
            valor = self._parse_operando(asign.operandoDrc())
            op = TipoOperacion(asign.OpAsign().getText())
            vars_ = self._collect_vars(objetivo, valor)
            consecuencia = ConsecuenciaModificacion(objetivo, op, valor, variables=vars_)
        elif ctx.borrado():
            prop, args = self._parse_predicado(ctx.borrado().predicado())
            #vars_ = [a for a in args if a[:1].isupper()]
            consecuencia = ConsecuenciaEliminacion(prop, args)
        elif ctx.predicado():
            prop, args = self._parse_predicado(ctx.predicado())
            #vars_ = [a for a in args if a[:1].isupper()]
            consecuencia = ConsecuenciaAsignacion(prop, args)
        return consecuencia
    
    def visitErrorNode(self, node: ErrorNode):
        #logger.error(f"Error de sintaxis en '{node.getText()}' en {node.symbol.line}:{node.symbol.column}")    
        raise ValueError(
            f"Error de sintaxis en '{node.getText()}' en {node.symbol.line}:{node.symbol.column}"
        )
        return None
    



