from antlr4 import ParseTreeVisitor
from gramaticaVisitor import gramaticaVisitor
from gramaticaParser import gramaticaParser
from motorEjecucion import MotorEjecucion
from base import TipoComparacion, TipoOperacion
from condiciones import CondicionSimple, CondicionComparacion
from consecuencias import ConsecuenciaAsignacion, ConsecuenciaEliminacion, ConsecuenciaModificacion
from reglas import Regla


def _texto_string(token: str) -> str:
    if token.startswith('"') or token.startswith('\u201C'):
        return token[1:-1]
    return token


class MotorVisitor(gramaticaVisitor):
    def __init__(self, motor: MotorEjecucion):
        super().__init__()
        self.motor = motor

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

    # Visitor methods -----------------------------------------------------
    def visitDeclCategoria(self, ctx: gramaticaParser.DeclCategoriaContext):
        nombre = ctx.idName().getText()
        esquema = {}
        if ctx.listaAtributos():
            for atr in ctx.listaAtributos().atributo():
                attr_nombre = atr.idName().getText()
                tipo_token = atr.tipoBasico().getText()
                tipo = {'int': int, 'str': str, 'bool': bool}[tipo_token]
                esquema[attr_nombre] = tipo
        self.motor.crear_categoria(nombre, esquema)
        return None

    def visitDeclProposicion(self, ctx: gramaticaParser.DeclProposicionContext):
        nombre = ctx.idName().getText()
        n = 0
        if ctx.listaIdentificadores():
            n = len(ctx.listaIdentificadores().idName())
        self.motor.crear_proposicion(nombre, n)
        return None

    def visitInicializacion(self, ctx: gramaticaParser.InicializacionContext):
        modo = ctx.getChild(0).getText()
        nombre = ctx.idName().getText()
        args = [self._parse_arg_lit(a) for a in ctx.argLit()]
        if modo == 'new':
            self.motor.nuevo_individuo(nombre, args)
        else:
            self.motor.add_proposicion(nombre, args)
        return None

    def visitEjecucion(self, ctx: gramaticaParser.EjecucionContext):
        nombre = ctx.idName().getText()
        args = [self._parse_arg_lit(a) for a in ctx.argLit()]
        self.motor.ejecutar_accion(nombre, args)
        return None

    def visitAccion(self, ctx: gramaticaParser.AccionContext):
        nombre = ctx.idName().getText()
        params = []
        if ctx.listaParams():
            params = [p.getText() for p in ctx.listaParams().idName()]
        condiciones = []
        for c in ctx.listaCondiciones().condicion():
            if c.predicado():
                prop, vars_ = self._parse_predicado(c.predicado())
                condiciones.append(CondicionSimple(prop, vars_))
            else:
                comp = c.comparacion()
                izq = self._parse_operando(comp.operando(0))
                der = self._parse_operando(comp.operando(1))
                op = TipoComparacion(comp.OpComp().getText())
                vars_ = self._collect_vars(izq, der)
                condiciones.append(CondicionComparacion(izq, op, der, vars_))
        regla = Regla(nombre, params, condiciones)
        for cons in ctx.listaConsecuencias().consecuencia():
            if cons.asignacion():
                asign = cons.asignacion()
                objetivo, atributo = self._parse_operando(asign.operandoIzq())
                valor = self._parse_operando(asign.operandoDrc())
                op = TipoOperacion(asign.OpAsign().getText())
                vars_ = self._collect_vars(objetivo, valor)
                regla.consecuencias.append(
                    ConsecuenciaModificacion(objetivo, atributo, op, valor, variables=vars_)
                )
            elif cons.borrado():
                prop, args = self._parse_predicado(cons.borrado().predicado())
                vars_ = [a for a in args if a[:1].isupper()]
                regla.consecuencias.append(ConsecuenciaEliminacion(prop, args, vars_))
            else:
                prop, args = self._parse_predicado(cons.predicado())
                vars_ = [a for a in args if a[:1].isupper()]
                regla.consecuencias.append(ConsecuenciaAsignacion(prop, args, vars_))
        self.motor.add_regla(regla, accion=True)
        return None
