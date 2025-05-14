import sys, os
from antlr4 import *

from CompiledFiles.SampleLexer import SampleLexer
from CompiledFiles.SampleParser import SampleParser
from Logic.bot import FashionBot
from nlp.vn_to_dsl import vn_to_dsl

def runOutfit(input_str):
    lexer = SampleLexer(InputStream(input_str))
    stream = CommonTokenStream(lexer)
    parser = SampleParser(stream)
    tree = parser.query()
    bot = FashionBot()
    result = bot.visit(tree)
    print(result)

def printUsage():
    print('Usage:')
    print('  python run.py run "outfit(...)"    # chạy DSL trực tiếp')
    print('  python run.py vn "câu tiếng Việt" # nhập tiếng Việt và chạy')

def main(argv):
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'run':
        if len(argv) < 2:
            print("Vui lòng nhập DSL")
        else:
            input_str = ' '.join(argv[1:])
            runOutfit(input_str)
    elif argv[0] == 'vn':
        if len(argv) < 2:
            print("Vui lòng nhập câu tiếng Việt")
        else:
            text = ' '.join(argv[1:])
            dsl = vn_to_dsl(text)
            print("DSL:", dsl)
            runOutfit(dsl)
    else:
        printUsage()

if __name__ == '__main__':
    main(sys.argv[1:])
