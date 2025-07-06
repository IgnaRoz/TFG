from antlr4 import ErrorNode, ParseTreeVisitor, TerminalNode
from antlr4.tree.Tree import ErrorNodeImpl

import importlib
import inspect
from types import MethodType
from func import func

import logging
from gramaticaVisitor import gramaticaVisitor
from gramaticaParser import gramaticaParser
from motorEjecucion import MotorEjecucion, logger
from base import TipoComparacion, TipoOperacion,Variable
from condiciones import CondicionSimple, CondicionComparacion, CondicionLogica, CondicionNegacion, CondicionAsignacion, CondicionFuncion
from consecuencias import (
    ConsecuenciaAsignacion,
    ConsecuenciaEliminacion,
    ConsecuenciaModificacion,
    ConsecuenciaFuncion
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
        #self.store = func_store.FuncStore()
        self.imports = {}
        #modBiblioteca = importlib.import_module("biblioteca")
        #self._import("Biblioteca","biblioteca")

        #prestamo = func(self.imports["Biblioteca"].funcs["concederPrestamo"],("nacho","programacion Python"))
        #prestamo.run()

        #self.imports["Biblioteca"].funcs["concederPrestamo"]("nacho","programacion Python")

    def _import(self,clase,ruta):
        mod =  importlib.import_module(ruta)
        cls = getattr(mod,clase)
        self.imports[clase] = cls
    


    def visitPrograma(self, ctx):
        for child in ctx.getChildren():
            if isinstance(child, gramaticaParser.ElementoContext):
                try:
                    self.visitElemento(child)
                except ValueError as e:
                    start = child.start.line
                    end = getattr(child.stop, "line", start)
                    logger.error(f"Error de sintaxis entre lineas {start}-{end}: {e}")
            elif isinstance(child, gramaticaParser.ImportsContext):
                try:
                    self.visitImports(child)
                except ValueError as e:
                    start = child.start.line
                    end = getattr(child.stop, "line", start)
                    logger.error(f"Error de sintaxis entre lineas {start}-{end}: {e}")

            elif isinstance(child, TerminalNode):
                # Manejar nodos terminales si es necesario
                pass
            else:
                logger.warning(f"Elemento desconocido: {child.getText()}")
        
    def visitImports(self, ctx):
        if any(isinstance(c, ErrorNodeImpl) for c in (getattr(ctx, 'children', None) or [])):
            raise ValueError(
                f"Error de sintaxis en '{ctx.getText()}' en {ctx.start.line}:{ctx.start.column}"
            )
        self._import(ctx.idName(1).getText(),ctx.idName(0).getText())
        

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
        elif getattr(ctx, 'INDIVIDUO', None):
            ind = ctx.INDIVIDUO().getText()
            if ctx.getChildCount() == 3:
                attr = ctx.idName().getText()
                return (ind, attr)
            return ind
        elif getattr(ctx,'funcion',None):
            return self.visit(ctx.funcion())
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.STRING():
            return _texto_string(ctx.STRING().getText())
        elif ctx.BOOLEAN():
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
        # 1. Nombre de la acción
        nombre = ctx.idName().getText()

        # 2. ¿Hay lista de argumentos?
        lista_ctx = ctx.listaArgLit()      # devuelve None si no aparece

        if lista_ctx:
            # Accedemos a los 'argLit' que cuelgan de la lista
            args = [self._parse_arg_lit(a) for a in lista_ctx.argLit()]
        else:
            args = []

        # 3. Ejecutamos la acción con manejo de errores
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
            prop,args = self.visitPredicado(ctx.predicado())
            condicion = CondicionSimple(prop,args)
            
        elif ctx.comparacion():
            condicion = self.visitComparacion(ctx.comparacion())
        elif ctx.operacionLogica():
            condicion = self.visitOperacionLogica(ctx.operacionLogica())
        elif ctx.asignacionVariable():
            condicion = self.visitAsignacionVariable(ctx.asignacionVariable())
        elif ctx.condicionFuncion():
            condicion = self.visitCondicionFuncion(ctx.condicionFuncion())

        return condicion
    
    def visitCondicionFuncion(self, ctx):

        funcion = self.visitFuncion(ctx.funcion())
        condicion = CondicionFuncion(funcion.args,funcion)
        return condicion
        return super().visitCondicionFuncion(ctx)

    def visitFuncion(self, ctx):
        nombre_modulo = ctx.idName(0).getText()
        if nombre_modulo not in self.imports:
            raise ValueError(f"No se ha econtrado el modulo {nombre_modulo}")
        mod = self.imports[nombre_modulo]
        nombre_funcion = ctx.idName(1).getText()
        if nombre_funcion not in mod.funcs:
            raise ValueError(f"No se ha econtrado la funcion {nombre_funcion} en el modulo {nombre_modulo}")
        funcion = mod.funcs[nombre_funcion]
        if ctx.listaArgsFuncion():

            args = tuple(self.visitListaArgsFuncion(ctx.listaArgsFuncion()))
        else:
            args = ()
        funcion = func(funcion,args)
        return funcion
    def visitListaArgsFuncion(self, ctx):
        args = []
        for child in ctx.getChildren():
            if not isinstance(child, TerminalNode):

                param = self.visitParamFuncion(child)
                args.append(param)
        return args
    
    def visitParamFuncion(self, ctx):

        if ctx.VARIABLE():
            if ctx.idName():
                return Variable(ctx.VARIABLE().getText(),ctx.idName().getText())
            else:
                return Variable(ctx.VARIABLE().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.NUMBER():
            valor = ctx.NUMBER().getText()
            valor = int(valor)
            return valor
        
        


        return super().visitParamFuncion(ctx)

    def visitPredicado(self, ctx):
        argumentos = self.visitListaArgsPredicado(ctx.listaArgsPredicado())
        prop = ctx.idName().getText()
        

        return prop,argumentos
    

    def visitListaArgsPredicado(self, ctx):
        argumentos = []
        for arg in ctx.paramPredicado():
            argumentos.append(self.visitParamPredicado(arg))
        return argumentos
    
    def visitParamPredicado(self, ctx):

        if ctx.VARIABLE():
            if ctx.idName():
                return Variable(ctx.VARIABLE().getText(),ctx.idName().getText())
            else:
                return Variable(ctx.VARIABLE().getText())
        elif ctx.getText()=="_":
            return '_'
        return super().visitParamPredicado(ctx)

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
        izq = self.visitOperando(ctx.operando(0))
        der = self.visitOperando(ctx.operando(1))
        op = TipoComparacion(ctx.OpComp().getText())
        variables = []
        if isinstance(izq,Variable):
            variables.append(izq)
        elif isinstance(izq,func):
            variables.append(izq.args)
        if isinstance(der,Variable):
            variables.append(der)
        elif isinstance(der,func):
            variables.append(der.args)

        condicion = CondicionComparacion(izq, op, der, variables)
        self.visitChildren(ctx)
        return condicion
    

    def visitOperando(self, ctx):
        # Si es una función
        if ctx.funcion():
            return self.visitFuncion(ctx.funcion())
        # VARIABLE '.' idName
        elif ctx.VARIABLE() and ctx.idName():
            return Variable(ctx.VARIABLE().getText(), ctx.idName().getText())
        # INDIVIDUO '.' idName
        elif ctx.INDIVIDUO() and ctx.idName():
            return (ctx.INDIVIDUO().getText(), ctx.idName().getText())
        # INDIVIDUO solo
        elif ctx.INDIVIDUO():
            return ctx.INDIVIDUO().getText()
        # VARIABLE sola
        elif ctx.VARIABLE():
            return Variable(ctx.VARIABLE().getText())
        # NUMBER
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        # STRING
        elif ctx.STRING():
            return _texto_string(ctx.STRING().getText())
        # BOOLEAN
        elif ctx.BOOLEAN():
            return ctx.BOOLEAN().getText() == 'True'
        # Fallback
        return ctx.getText()

    def visitAsignacionVariable(self, ctx):

        variable_asignacion = ctx.VARIABLE().getText()
        nombre,argumentos = self.visitPredicado(ctx.predicado())
        return CondicionAsignacion(argumentos,variable_asignacion,nombre)


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
            objetivo  = self.visitOperandoIzq(asign.operandoIzq())
            valor = self.visitOperandoDrc(asign.operandoDrc())
            if(asign.OpAsign()):

                op = TipoOperacion(asign.OpAsign().getText())
            else:
                op = TipoOperacion("=")
            #vars_ = self._collect_vars(objetivo, valor)
            variables = [objetivo]
            if isinstance(valor,Variable):
                variables.append(valor)
            elif isinstance(valor,func):
                variables.append(valor.args)
            consecuencia = ConsecuenciaModificacion(objetivo=objetivo,operacion=op,valor=valor,variables=variables)
        elif ctx.borrado():
            prop, args = self.visitPredicado(ctx.borrado())
            #vars_ = [a for a in args if a[:1].isupper()]
            consecuencia = ConsecuenciaEliminacion(prop, args)
        elif ctx.predicado():
            prop, args = self.visitPredicado(ctx.predicado())
            #vars_ = [a for a in args if a[:1].isupper()]
            consecuencia = ConsecuenciaAsignacion(prop, args)
        elif ctx.funcion():
            funcion = self.visitFuncion(ctx.funcion())
            consecuencia = ConsecuenciaFuncion(funcion.args,funcion)
            
        return consecuencia
    def visitOperandoIzq(self, ctx):

        variable = Variable(ctx.VARIABLE().getText(),ctx.idName().getText())
        return variable
        return super().visitOperandoIzq(ctx)
    def visitOperandoDrc(self, ctx):
        if ctx.operandoIzq():
            return self.visitOperandoIzq(ctx.operandoIzq())
        elif ctx.funcion():
            return self.visitFuncion(ctx.funcion())
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())

        return super().visitOperandoDrc(ctx)

    def visitBorrado(self, ctx):
        return self.visitPredicado(ctx.predicado())
        return super().visitBorrado(ctx)

    def visitErrorNode(self, node: ErrorNode):
        #logger.error(f"Error de sintaxis en '{node.getText()}' en {node.symbol.line}:{node.symbol.column}")    
        raise ValueError(
            f"Error de sintaxis en '{node.getText()}' en {node.symbol.line}:{node.symbol.column}"
        )
        return None
    



