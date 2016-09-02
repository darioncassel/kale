"""
The Lexer requires the Token class because it needs
to be able to generate Statement-type Tokens.
"""
from Tokenizer.Token import Token

"""
Here, we import all of the Types individually (to
help IDEs recoginize the imports).
"""
from Types.Types import commentType, numType, addOpType, \
    subOpType, multOpType, divOpType, statementBeginType, \
    statementEndType, nameType, defnType, assignType, \
    valType, varType, outputType

"""
The Lexer class takes a list of Tokens and assigns
a Kale Type (from Types.py) to them.
"""


class Lexer(object):

    """
    We give the Lexer a list of Tokens.
    """
    def __init__(self, tokens):
        self.tokens = tokens

    """
    The lex method assigns Kale types.

    Currently it has a cumbersome method of assigning
    comment types that amounts to flipping a switch
    when a comment symbol ('#') is encountered and
    tagging all of the following tokens as comment-type
    until the next comment symbol is encountered.

    TODO: Find a better method of annotating commentTypes
    """
    def lex(self):
        skipForComment = False
        for token in self.tokens:
            if token.getLiteral() == "#":
                token.setType(commentType())
                skipForComment = not skipForComment
            elif skipForComment:
                token.setType(commentType())
            elif not skipForComment:
                if token.getLiteral() == "(":
                    token.setType(statementBeginType())
                elif token.getLiteral() == ")":
                    token.setType(statementEndType())
                elif token.getLiteral() == "+":
                    token.setType(addOpType())
                elif token.getLiteral() == "-":
                    token.setType(subOpType())
                elif token.getLiteral() == "*":
                    token.setType(multOpType())
                elif token.getLiteral() == "/":
                    token.setType(divOpType())
                elif token.getLiteral().isdigit():
                    token.setLiteral(int(token.getLiteral()))
                    token.setType(numType())
                elif token.getLiteral() != "":
                    if token.getLiteral() == "defn":
                        token.setType(defnType())
                    elif token.getLiteral() == "var":
                        token.setType(varType())
                    elif token.getLiteral() == "val":
                        token.setType(valType())
                    elif token.getLiteral() == "set":
                        token.setType(assignType())
                    elif token.getLiteral() == "say":
                        token.setType(outputType())
                    else:
                        token.setType(nameType())

    """
    Here, we define a getter for the tokens property.
    """
    def getTokens(self):
        return self.tokens
