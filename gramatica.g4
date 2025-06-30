grammar gramatica;

programa
    : imports* elemento* EOF
    ;
imports
    : 'from' idName 'import' idName ';'
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
    : declCategoria ';' comentarioSimple?
    | declProposicion ';' comentarioSimple?
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
    : 'Prop' idName '(' listaIdentificadores? ')' bloquePropiedades? 
    ;
bloquePropiedades
    : '{' listaPropiedades? '}'            
    ;
listaIdentificadores
    : idName (',' idName)*
    ;
listaPropiedades
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
    | asignacionVariable
    | condicionFuncion
    ;
condicionFuncion
    : funcion
    ;
asignacionVariable
    : VARIABLE OpIgual predicado
    ;
predicado
    : idName '(' listaArgsPredicado ')'
    ;
listaArgsPredicado
    : paramPredicado (',' paramPredicado)*
    ;
paramPredicado
    : INDIVIDUO
    | funcion
    | VARIABLE '.' idName
    | VARIABLE
    | STRING
    | NUMBER
    | BOOLEAN
    | '_'
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
    : funcion                    # operandoFunc
    | VARIABLE '.' idName        # operandoVarAttr //No llega a entrar porque variable.atributo tambien es una variable. Pero no importa
    | INDIVIDUO '.' idName       # operandoIndAttr
    | INDIVIDUO                  # operandoInd
    | VARIABLE                   # operandoVar
    | NUMBER                     # operandoNum
    | STRING                     # operandoStr
    | BOOLEAN                    # operandoBool
    ;
funcion
    : idName  '.' idName '(' listaArgsFuncion? ')' //hay que añadir una regla semantica para que no se pueda incluir una funcion dentro de una funcion
    ;

listaArgsFuncion
    : paramFuncion (',' paramFuncion)*
    ;
paramFuncion
    : INDIVIDUO
    | VARIABLE '.' idName
    | VARIABLE
    | STRING
    | NUMBER
    | BOOLEAN
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
    | funcion
    | borrado
    | predicado
    ;

asignacion
    : operandoIzq (OpAsign|OpIgual) operandoDrc
    ;
operandoIzq
    : VARIABLE '.' idName
    ;
operandoDrc
    : funcion
    | operandoIzq
    | NUMBER
    ;

OpIgual
    : '='
    ; 
OpAsign
    : '+='
    | '-='
    ;

borrado
    : 'DEL' predicado
    ;

inicializacion
    : ('add') idName '(' argLit (',' argLit)* ')' bloqueValores? ';'
    ;

bloqueValores
    : '{' listaParejasValor? '}'
    ;

listaParejasValor
    : parejaValor (',' parejaValor)*
    ;

parejaValor
    : idName '=' valor
    ;   

valor                           
    : NUMBER
    | STRING
    | BOOLEAN
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
    : LETTER_U (LETTER | DIGIT | '_' )*
    ;
    
// para todo nombre genérico (categorias, props, acciones…)
idName
    : INDIVIDUO
    | VARIABLE
    ;
WS
    : [ \t\r\n]+ -> skip
    ;
