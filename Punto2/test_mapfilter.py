import sys
from antlr4 import *
from MapFilterLexer import MapFilterLexer
from MapFilterParser import MapFilterParser
from MapFilterListener import MapFilterListener

class MapFilterExecutor(MapFilterListener):
    def __init__(self):
        self.result = None

    def exitMapOperation(self, ctx):
        function_name = ctx.function().getText()
        iterable = eval(ctx.iterable().getText())
        
        functions = {
            'square': lambda x: x ** 2,
            'cube': lambda x: x ** 3,
            'str': str,
            'len': len,
            'negative': lambda x: -x,
            'double': lambda x: x * 2,
            'is_even': lambda x: x % 2 == 0,
            'uppercase': lambda x: x.upper() if isinstance(x, str) else x,
        }
        
        if function_name not in functions:
            raise ValueError(f"Unknown function: {function_name}")
        
        self.result = list(map(functions[function_name], iterable))

    def exitFilterOperation(self, ctx):
        condition = ctx.condition().getText()
        iterable = eval(ctx.iterable().getText())
        
        op = ctx.condition().comparisonOp().getText()
        right = ctx.condition().expr().getText()
        
        ops = {
            '>': lambda x, y: x > y,
            '<': lambda x, y: x < y,
            '>=': lambda x, y: x >= y,
            '<=': lambda x, y: x <= y,
            '==': lambda x, y: x == y,
            '!=': lambda x, y: x != y
        }
        
        if op not in ops:
            raise ValueError(f"Unknown operator: {op}")
        
        if right.replace('.', '').lstrip('-').isdigit():
            right_val = float(right)
        elif right.startswith("'") and right.endswith("'"):
            right_val = right.strip("'")
        else:
            right_val = right
        
        function = lambda x: ops[op](x, right_val)
        self.result = list(filter(function, iterable))

def main(input_string):
    lexer = MapFilterLexer(InputStream(input_string))
    stream = CommonTokenStream(lexer)
    parser = MapFilterParser(stream)
    tree = parser.program()

    executor = MapFilterExecutor()
    walker = ParseTreeWalker()
    walker.walk(executor, tree)

    return executor.result

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python test_mapfilter.py 'MAP(function, iterable)' or 'FILTER(condition, iterable)'")
        sys.exit(1)

    input_string = sys.argv[1]

    try:
        result = main(input_string)
        print(f"Input: {input_string}")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")
