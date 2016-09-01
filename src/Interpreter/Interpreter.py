"""
The Interpreter needs access to functional types
in order to run the program.
"""
from Interpreter.Grammar import GrammarApply
from Interpreter.ByteCode import ByteCode
from Interpreter.Machine import Machine
from Types.Types import numType, addOpType, \
    subOpType, multOpType, divOpType


"""
The goal of the Interpreter is to take a SyntaxTree
(Kale abstract syntax tree) and evaulate it (using
stack-based evaluation).
"""


class Interpreter(object):

    """
    The Interpreter is initalized with a SyntaxTree
    (from the Parser). It initializes an empty stack
    (the Python list is being used as a stack).
    """
    def __init__(self, syntaxTree):
        self.tree = syntaxTree
        self.grammarApply = GrammarApply()
        self.byteCode = ByteCode()
        self.machine = Machine()

    """
    The interpretNode method evaluates the tokens
    contained in a given SyntaxNode object using the
    instance's stack.

    Types and manipulations are converted to their
    stack-based Python equivalent.
    """
    def interpretNode(self, node):
        _head = 0
        _tail = -1
        operator = node.getToken()
        print(operator)
        print(node.children)
        if operator:
            opList = self.grammarApply.applyToToken(operator)
            print(operator.type)
            if len(opList) > 1:
                _cIndex = 0
                for opString in opList[:_tail]:
                    func = self.byteCode.getOperation(opString)
                    if func:
                        token = node.getChildren()[_cIndex]
                        self.interpretNode(token)
                        _cIndex += 1
                print("Called: " + opList[_tail])
                func = self.byteCode.getOperation(opList[_tail])
                func(self.machine, None)
            else:
                print("Called: " + opList[_tail])
                func = self.byteCode.getOperation(opList[_head])
                func(self.machine, operator.literal)
                print(self.machine.stack)
            print(self.machine)
        else:
            for child in node.children:
                self.interpretNode(child)
            

    """
    The _interpret method calls interpretNode on
    a given node, and recursively calls _interpret
    on the node's children.
    """
    def _interpret(self, node):
        self.interpretNode(node)

    """
    The interpret method is an entrypoint for the
    real interpret method (_interpret). Using this
    allows the final Interpret call to not have to
    know about the SyntaxTree and its root.
    """
    def interpret(self):
        root = self.tree.getRoot()
        self._interpret(root)

    """
    The output method returns out whatever the stack
    contains as a single space-seperated string.
    """
    def output(self):
        return " ".join([str(x) for x in self.machine.stack])
