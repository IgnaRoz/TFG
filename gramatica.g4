grammar gramatica;

programa
    : elemento* EOF
    ;

elemento
    : declaracion
    | accion
    | inicializacion
    | ejecucion
    | comentarioSimple
    | comentarioMultilineo
    ;

declaracion
    : declCategoria ';'
    | declProposicion ';'
    ;

declCategoria
    : 'Categoria' idName '(' listaAtributos? ')'
    ;
listaAtributos
    : atributo (',' atributo)*
    ;
atributo
    : idName ':' tipoBasico
    ;
tipoBasico
    : 'int'
    | 'str'
    | 'bool'
    ;

declProposicion
    : 'Prop' idName '(' listaIdentificadores? ')'
    ;
listaIdentificadores
    : idName (',' idName)*
    ;

accion
    : 'Accion' idName '(' listaParams? ')' ':'
      comentarioMultilineo?
      'Condiciones:' listaCondiciones
      'Consecuencias:' listaConsecuencias
    ;
listaParams
    : idName (',' idName)*
    ;

// **Cada condición termina en ';', antes de comentarioSimple opcional**
listaCondiciones
    : ( condicion ';' comentarioSimple? )*
    ;
condicion
    : predicado
    | comparacion
    | operacionLogica
    ;

predicado
    : idName '(' listaArgsPredicado? ')'
    ;
listaArgsPredicado
    : paramPredicado (',' paramPredicado)*
    ;
paramPredicado
    : INDIVIDUO
    | VARIABLE
    ;

comparacion
    : operando OpComp operando
    ;
OpComp
    : '<'  
    | '>'  
    | '==' 
    | '!=' 
    | '<=' 
    | '>=' 
    ;

operando
    : VARIABLE '.' idName        # operandoVarAttr
    | INDIVIDUO '.' idName       # operandoIndAttr
    | INDIVIDUO                  # operandoInd
    | VARIABLE                   # operandoVar
    | NUMBER                     # operandoNum
    | STRING                     # operandoStr
    | BOOLEAN                    # operandoBool
    ;

operacionLogica
    : OR '(' listaCondiciones ')'        #opOr
    | AND '(' listaCondiciones ')'       #opAnd
    | NOT '(' condicion ')'              #opNot
    ;

OR  : 'OR'  ;
AND : 'AND' ;
NOT : 'NOT' ;


 // **Cada consecuencia termina en ';', antes de comentarioSimple opcional**
listaConsecuencias
    : ( consecuencia ';' comentarioSimple? )*
    ;
consecuencia
    : asignacion
    | borrado
    | predicado
    ;

asignacion
    : operandoIzq OpAsign operandoDrc
    ;
operandoIzq
    : VARIABLE '.' idName
    | INDIVIDUO '.' idName
    ;
operandoDrc
    : operandoIzq
    | NUMBER
    ;
OpAsign
    : '+='
    | '-='
    | '='
    ;

borrado
    : 'DEL' predicado
    ;

inicializacion
    : ('new' | 'add') idName '(' argLit (',' argLit)* ')' ';'
    ;
argLit
    : STRING
    | NUMBER
    ;

ejecucion
    : 'Run' idName '(' argLit (',' argLit)* ')' ';'
    ;

comentarioSimple
    : COMMENT_SIMPLE
    ;
comentarioMultilineo
    : COMMENT_MULTI
    ;

// ------------------------------------------------------------------
// LEXER RULES
// ------------------------------------------------------------------
fragment LQUOTE : '\u201C' ;  // “
fragment RQUOTE : '\u201D' ;  // ”  

COMMENT_SIMPLE
    : '//' ~[\r\n]* 
    ;

COMMENT_MULTI
    : '"""' .*? '"""'
    ;

BOOLEAN
    : 'True'
    | 'False'
    ;

STRING
    : ( '"' | LQUOTE )
      (~['"\r\n\u201C\u201D])* 
      ( '"' | RQUOTE )
    ;

NUMBER
    : [0-9]+
    ;
// ── Fragmentos Unicode ──────────────────────────────────────
fragment LETTER   : [\p{L}] ;       // cualquier letra de cualquier alfabeto
fragment LETTER_L : [\p{Ll}] ;      // letra minuscula
fragment LETTER_U : [\p{Lu}] ;      // letra mayuscula
fragment DIGIT    : [\p{Nd}] ;      // dígito decimal

// ── Identificadores ────────────────────────────────────────
// individuo = identificador que empieza por minúscula
INDIVIDUO
    : LETTER_L (LETTER | DIGIT | '_')*
    ;

// variable = identificador que empieza por mayúscula
VARIABLE
    : LETTER_U (LETTER | DIGIT | '_')*
    ;

// para todo nombre genérico (categorias, props, acciones…)
idName
    : INDIVIDUO
    | VARIABLE
    ;
WS
    : [ \t\r\n]+ -> skip
    ;
