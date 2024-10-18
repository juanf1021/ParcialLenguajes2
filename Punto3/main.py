import sys
from antlr4 import *
from LaPlaceLexer import LaPlaceLexer
from LaPlaceParser import LaPlaceParser
from LaPlaceListener import LaPlaceListener

class MyLaplaceListener(LaPlaceListener):
    def __init__(self):
        super().__init__()
        self.transform_table = {
            't': '1/s^2',             
            'e': '1/(s - a)',         
            'cos': 's/(s^2 + a^2)',   
            'sin': 'a/(s^2 + a^2)',   
            't^2': '2/s^3',           
        }
        self.transformations = []

    def exitIntegral(self, ctx):
        print("Integral detectada:")
        print("Límite inferior: 0")
        print("Límite superior: infinity")
        
        # Verificar que la expresión esté presente
        if ctx.expression():
            expression_text = ctx.expression().getText()  
            print(f"Expresión: {expression_text}")
        else:
            print("No se encontró una expresión en la integral.")

    def exitTerm(self, ctx):
        for child in ctx.children:
            # Ignorar operadores
            if isinstance(child, TerminalNode) and child.getSymbol().type in [LaPlaceParser.MULT, LaPlaceParser.DIV]:
                continue
            self.exitFactor(child)

    def exitFactor(self, ctx):
        if ctx.INT() is not None:
            self.transformations.append(f"Transformada de {ctx.INT().getText()}: {ctx.INT().getText()} / s")
        elif ctx.ID() is not None:
            func_name = ctx.ID().getText()
            if func_name in self.transform_table:
                self.transformations.append(f"Transformada de {func_name}: {self.transform_table[func_name]}")
            else:
                self.transformations.append(f"No se encontró la transformada para {func_name}")
        elif ctx.MINUS() is not None:
            # Manejo de números negativos
            print("Se detectó un signo negativo.")
        # Aquí puedes añadir más condiciones según tu gramática.

def main():
    input_stream = InputStream(input("Ingrese la función para la transformada de Laplace: "))
    lexer = LaPlaceLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LaPlaceParser(stream)

    tree = parser.start()  # Llama a la regla 'start'

    listener = MyLaplaceListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()
