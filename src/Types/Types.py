"""
The TypeDef class is the parent class of all of
the Kale types.

It currently inherits from the Python object class
but perhaps this will be changed/improved in the
near future.
"""

class Singleton(object):
    class __Singleton:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton(arg)
        else:
            Singleton.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)


class TypeDef(Singleton):

    """
    The TypeDef object is currently initialized with a literal,
    a pyType (the Python equivalent type), an "expectsNext"
    literal (to give the Parser an idea of what should come
    next, but this isn't implemented yet), and a requiresClose
    (bool) that indicates whether this Type needs a closing
    symbol (this probably will be removed and isn't used right
    now).
    """
    def __init__(self, literal, pyType, expectsNext, requiresClose):
        self.literal = literal
        self.pyType = pyType
        self.expectsNext = expectsNext
        self.requiresClose = requiresClose

    """
    To represent a TypeDef object, we just return its Class name
    as a Python str.
    """
    def __repr__(self):
        return self.__class__.__name__

"""
The Statement is the most complex Kale type. It currently represents
a set of Tokens that semantically go together.

FIXME: This should be removed.
"""


class Statement(TypeDef):

    """
    The Statement, unlike the other Kale types is currently
    initialized with an id.

    FIXME: remove.
    """
    def __init__(self, id):
        self.type = Statement
        self.id = id
        self.tokens = []
        super().__init__(None, None, None, True)

    """
    Because the Statement type needs to contain a list of
    Tokens (which may be other Statements!) it needs a method
    that provides abstracted access to its tokens.
    """
    def addToken(self, token):
        self.tokens.append(token)

    """
    In order to represent this type, we overload the TypeDef
    __repr__ method and instead print out the Statement's id
    and the Tokens it contains.
    """
    def __repr__(self):
        return "S[id=" + str(self.id) + \
            ", tokens=" + str(self.tokens) + "]"

"""
The statementBeginType, which will probably actually be kept
(as opposed to the Statement type), simply recognizes an open
parenthesis.
"""


class statementBeginType(TypeDef):

    def __init__(self):
        super().__init__("(", None, None, True)

"""
The statementEndType recognizes a close parenthesis.
"""


class statementEndType(TypeDef):

    def __init__(self):
        super().__init__(")", None, None, False)

"""
The commentType is applied to a ('#') symbol as well
as any literals that fall after the first '#' but
before the last '#'.
"""


class commentType(TypeDef):

    def __init__(self):
        super().__init__("#", None, None, True)

"""
The numType is a wrapper for the Python int. Currently,
to keep things simple, Kale has no support for other
numeric types.
"""


class numType(TypeDef):
    def __init__(self):
        super().__init__("", int, None, False)

class nameType(TypeDef):
     def __init__(self):
        super().__init__("", str, None, False)

class varType(TypeDef):
    def __init__(self):
        super().__init__("var", str, None, False)

class defnType(TypeDef):
    def __init__(self):
        super().__init__("defn", str, None, False)

class valType(TypeDef):
    def __init__(self):
        super().__init__("val", str, None, False)

class assignType(TypeDef):
    def __init__(self):
        super().__init__("=", str, None, False)

class outputType(TypeDef):
    def __init__(self):
        super().__init__("say", str, None, False)


"""
The addOpType is a wrapper for the (Python) +
Operator.
"""


class addOpType(TypeDef):

    def __init__(self):
        super().__init__("+", None, int, False)

"""
The subOpType is a wrapper for the (Python) -
operator.
"""


class subOpType(TypeDef):

    def __init__(self):
        super().__init__("-", None, int, False)

"""
The multOpType is a wrapper for the (Python) *
operator.
"""


class multOpType(TypeDef):

    def __init__(self):
        super().__init__("+", None, int, False)

"""
The divOpType is a wrapper for the (Python) /
operator.
"""


class divOpType(TypeDef):

    def __init__(self):
        super().__init__("/", None, int, False)


class gCondOpType(TypeDef):

    def __init__(self):
        super().__init__("/", None, int, False)


class gCondOpType(TypeDef):

    def __init__(self):
        super().__init__("/", None, int, False)


class gCondOpType(TypeDef):

    def __init__(self):
        super().__init__(">", None, int, False)


class geCondOpType(TypeDef):

    def __init__(self):
        super().__init__(">=", None, int, False)


class lCondOpType(TypeDef):

    def __init__(self):
        super().__init__("<", None, int, False)

    
class leCondOpType(TypeDef):

    def __init__(self):
        super().__init__("<=", None, int, False)


class eqCondOpType(TypeDef):

    def __init__(self):
        super().__init__("==", None, int, False)


