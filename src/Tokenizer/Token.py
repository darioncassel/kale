"""
This is the Token class. It defines the base object level
of Kale and is used in the Tokenizer to perform the first
pass through a Kale (.kl) source file.

Currently the Token inherits from the Python base object
because the Python interpreter is being used as a backend.

TODO: Possible switch to Enum as parent class?
"""


class Token(object):

    """
    The Token object initializes with an id, literal, and
    a type.

    Currently, the id does not have much effect and
    is just there because it might be useful later.

    The literal represents the exact ascii value found in
    the source file for that Token.

    The type currently is one of the TypeDef classes found
    in the Types.py file. Currently most of these types
    are just overlays of basic Python types.
    """
    def __init__(self, literal, type):
        self.literal = literal
        self.type = type

    """
    Here, we define getters and setters for the properties of
    the object.
    """

    def getLiteral(self):
        return self.literal

    def getType(self):
        return self.type

    def setLiteral(self, literal):
        self.literal = literal

    def setType(self, type):
        self.type = type

    """
    The Token object can be printed for debugging reasons.

    The KaleType of the object is just a wrapper for the
    self.type because the that value might be None, which
    cannot be coerced to a Python str.
    """
    def __repr__(self):
        if self.type is None:
            KaleType = "None"
        else:
            KaleType = self.type
        return "T(literal=" + \
            str(self.literal) + " type=" + str(KaleType) + ")"
