"""
The Tokenizer uses the Token object because it
converts literals to Tokens.
"""
from Tokenizer.Token import Token

"""
The Tokenizer takes a source file and generates a
list of Token objects based on the literals in
the file.
"""


class Tokenizer(object):

    """
    We initialize the Tokenizer with a filename that
    indicates a Kale (.kl) source file.

    A List that will contain the generated Tokens is
    initialized.
    """
    def __init__(self, filename):
        self.tokens = []
        with open(filename, "r") as file:
            self.file = file.readlines()

    """
    The Tokenizer splits the source file into discrete
    unit literals based on spacing, and then generates
    untyped Tokens with filled with literals and an id
    based on their position in the file (relative to
    other tokens, not to a byte position).
    """
    def tokenize(self):
        lineString = " ".join(self.file)
        charArray = list(lineString)
        aggregate = ""
        index = 0
        while index < len(charArray):
            char = charArray[index]
            if char != "\r" and char != "\n":
                if char == "(" or char == ")":
                    if aggregate != "":
                        self.tokens.append(Token(aggregate, None))
                        aggregate = ""
                    self.tokens.append(Token(char, None))
                elif char == " ":
                    self.tokens.append(Token(aggregate, None))
                    aggregate = ""
                else:
                    aggregate += char
            index += 1
        if aggregate != "":
            self.tokens.append(Token(aggregate, None))
            aggregate = ""
    
    """
    Here, we define a getter for the tokens property.
    """
    def getTokens(self):
        return self.tokens
