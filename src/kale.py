"""
This file composes the various pieces of the Kale
interpreter in order to evaluate a given Kale
(.kl) file.
"""
import sys
from Lexer.Lexer import Lexer
from Parser.Parser import Parser
from Tokenizer.Tokenizer import Tokenizer
from Interpreter.Interpreter import Interpreter

"""
It takes a filename and performs the following
data flow:

    File -> Tokenize -> Lex -> Parse -> Interpret

The result of the interpretation is returned.
"""


def main(filename):
    tokenizer = Tokenizer(filename)
    tokenizer.tokenize()
    lexer = Lexer(tokenizer.getTokens())
    lexer.lex()
    parser = Parser(lexer.getTokens())
    parser.parse()
    interpreter = Interpreter(parser.getTree())
    interpreter.interpret()
    return interpreter.output()

"""
If the file is called from a command line (with a 
filename arg), main() is called and the result is
printed.
"""
if __name__ == "__main__":
    result = main(sys.argv[1])
    print(result)
