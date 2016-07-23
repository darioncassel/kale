"""
The Parser needs to have access to the SyntaxTree to
construct one.
"""
from SyntaxTree.SyntaxTree import SyntaxTree

"""
The Parser only cares about recognizing the beginning
and end of statements.
"""
from Types.Types import statementBeginType, \
    statementEndType


"""
The Parser takes a list of tokens and transforms it into
a SyntaxTree composed of statements.

A statement is a group of related tokens (recognized because
they are contained within an open and corresponding close
parenthesis).
"""


class Parser(object):

    """
    We initialize the Parser with a list of typed Tokens (from
    the Lexer).

    The Parser initalizes a SyntaxTree (that will have just a
    root node).
    """
    def __init__(self, tokens):
        self.tokens = tokens
        self.tree = SyntaxTree()

    """
    The parse method goes through the list of tokens and constructs
    statements from groups of tokens;

        A statement is something of the form

            T:statementBeginType T:[T] T:statementEndType

        Where T:[T] is a list of one or more Tokens.

    This job is make tricky because the statements nest. Thus, a
    "balance" variable is needed to check when the parenthesis are
    or aren't balanced.

    New Statements (currentStatement) are appended to the SyntaxTree
    with the appendStatement method.
    """
    def parse(self):
        inStatement = False
        currentStatement = None
        balance = 0
        for token in self.tokens:
            KaleType = type(token.getType())
            if KaleType == statementBeginType:
                balance += 1
                inStatement = True
                currentStatement = []
            elif KaleType == statementEndType:
                balance -= 1
                if balance == 0:
                    inStatement = False
                self.tree.appendStatement(currentStatement)
                currentStatement = []
            elif inStatement:
                currentStatement.append(token)

    """
    Here we define a getter for the SyntaxTree.
    """
    def getTree(self):
        return self.tree
