"""
The SyntaxNode is the building block of the SyntaxTree
(abstract syntax tree) of Kale. Each SyntaxNode contains
a list of tokens, a list of children (nodes), and a
reference to its parent node (if any).
"""


class SyntaxNode(object):

    """
    The SyntaxNode is initialized with a list of tokens.
    Its children and parent are initialized to an empty
    list and None, respectively.
    """
    def __init__(self, token):
        self.token = token
        self.children = []
        self.parent = None
    
    def setToken(self, token):
        self.token = token

    """
    The addChild method allows us to append a node to the
    node's list of children.
    """
    def addChild(self, node):
        self.children.append(node)

    """
    Here, we define getters and setters for some of the
    node's properties.
    """
    def getToken(self):
        return self.token

    def getChildren(self):
        return self.children

    def getParent(self):
        return self.parent

    def setParent(self, node):
        self.parent = node

    """
    A SyntaxNode can be printed for debugging reasons.
    Representation is performed recursively; the node's
    tokens are printed and then its children (and their
    tokens are printed). It is usually enough to just
    print a root node to get representations of a tree.
    """
    def printNode(self, node, level):
        output = ""
        output += "N[t={"
        if node.token:
            output += str(node.token)
        output += "}, c={"
        if node.children:
            for child in node.children:
                output += "\n" + " "*level + self.printNode(child, level+2) + ", "
            output += "\n"
        return output + " "*int(level/2) + "}]"
    
    def __repr__(self):
        return self.printNode(self, 2)

"""
The SyntaxTree object is an overlay for the SyntaxNode
that allows for tree construction given statements from
the Parser (Parser.py).

A single SyntaxTree object should define the abstract
syntax tree for a Kale program.
"""


class SyntaxTree(object):

    """
    The SyntaxTree is initialized with a root node that is
    a SyntaxNode with no tokens.

    The tree also has a currentNode variable that keeps track
    of where in the tree an instance of SyntaxTree is, so that
    appendNode knows where to add a node.
    """
    def __init__(self):
        self.root = SyntaxNode(None)
        self.currentNode = None

    """
    AppendNode adds a node to the list of children nodes of the
    currentNode. If the currentNode has yet to be set, the node
    is added to the root of the tree, which is then set as the
    currentNode.
    """
    def appendNode(self, node):
        """if self.currentNode:
            node.setParent(self.currentNode)
            self.currentNode.addChild(node)
        else:
            node.setParent(self.root)
            self.root.addChild(node)
        self.currentNode = node
        """
        node.setParent(self.root)
        self.root.addChild(node)

    """
    Statements, which are just lists of tokens, are added
    to the tree using this wrapper. It takes a list of tokens,
    creates a SyntaxNode to hold them, and calls appendNode with
    the new node.
    """
    def appendStatement(self, tokens):
        newSyntaxNode = SyntaxNode(tokens)
        self.appendNode(newSyntaxNode)

    """
    The getRoot method returns the absolute root of the tree. 

    Currently, access to the currentNode is not provided.
    """
    def getRoot(self):
        return self.root

    """
    We can print out a SyntaxTree by calling __repr__ on its
    root node.
    """
    def __repr__(self):
        return self.root.printNode(self.root, 2)
