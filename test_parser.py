from antlr4 import FileStream, CommonTokenStream
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser

# 1) Lee el fichero de entrada
input_stream = FileStream('ejemplo.txt', encoding='utf-8')

# 2) Tokeniza
lexer = gramaticaLexer(input_stream)
token_stream = CommonTokenStream(lexer)

# 3) Parsea
parser = gramaticaParser(token_stream)
tree = parser.programa()   # regla inicial: programa

# 4) Muestra el árbol de parseo
print(tree.toStringTree(recog=parser))