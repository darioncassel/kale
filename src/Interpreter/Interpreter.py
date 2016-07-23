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
        statement = node.getTokens()
        if statement:
            for token in statement:
                print("Token: " + str(token.type))
                opList = self.grammarApply.applyToToken(token)
                once = False
                for opString in opList:
                    func = self.byteCode.getOperation(opString)
                    if func and not self.machine.skip1:
                        if self.machine.skip2:
                            self.machine.skip1 = True
                            self.machine.skip2 = False
                        print("Called: " + opString)
                        func(self.machine, token.literal)
                        print(str(self.machine)+"\n")
                    elif self.machine.skip1:
                        self.machine.skip1 = False

    """
    The _interpret method calls interpretNode on
    a given node, and recursively calls _interpret
    on the node's children.
    """
    def _interpret(self, node):
        self.interpretNode(node)
        for childNode in node.getChildren():
            self._interpret(childNode)

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
