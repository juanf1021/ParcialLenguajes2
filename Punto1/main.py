from antlr4 import *
from RationalLexer import RationalLexer
from RationalParser import RationalParser
from MyVisitor import MyVisitor

def main(input_file):
    input_stream = FileStream(input_file)
    lexer = RationalLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RationalParser(stream)
    tree = parser.expr()
    
    print(f"Árbol sintáctico: {tree.toStringTree(recog=parser)}")
    
    visitor = MyVisitor()
    try:
        result = visitor.visit(tree)
        
        if result is not None:
            print(f"Resultado final: {result}")
        else:
            print("Error: No se pudo calcular el resultado.")
    except Exception as e:
        print(f"Se produjo una excepción: {str(e)}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Por favor, proporciona un archivo de entrada.")
