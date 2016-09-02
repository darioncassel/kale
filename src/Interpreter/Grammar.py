"""
class GrammarNode(object):

    def __init__(self, typeString):
        self.typeString = typeString
        self.children = {}

    def addChild(self, node):
        self.children.append(node)
"""

class GrammarRules(object):

    rules = [
        "NoneType :: None",
        "commentType :: None",
        "statementBeginType :: None",
        "statementEndType :: None",
        "numType :: stackPush",
        "nameType :: stackPush",
        "valType :: stackPush accessVar",
        "addOpType :: stackPush stackPush addOp",
        "subOpType :: stackPush stackPush subOp",
        "multOpType :: stackPush stackPush multOp",
        "divOpType :: stackPush stackPush divOp",
        "varType :: stackPush allocateVar",
        "assignType :: stackPush stackPush addrPush",
        "outputType :: stackPush stdOut"
    ]

    def __init__(self):
        self.tokenRules = self.parseRulesToDict()
        # self.grammarTree = self.parseRulesToTree()

    def parseRulesToDict(self):
        tokenRules = {}
        for rule in self.rules:
            typeStr, ops = rule.split("::")
            newRule = []
            for op in ops.split(" "):
                if op != "":
                    newRule.append(op.strip())
            tokenRules[typeStr.strip()] = newRule
        return tokenRules

    def getTokenRules(self):
        return self.tokenRules

    """
    def parseRulesToTree(self):
        rootNode = GrammarNode(None)
        for tokenRule in self.tokenRules:
            currentNode = rootNode
            for part in tokenRule:
                partNode = GrammarNode(part)
                if part in currentNode.children.keys():
                    currentNode = currentNode.children[part]
                else:
                    currentNode.children[part] = partNode
        return rootNode
    """


class GrammarApply(object):

    def __init__(self):
        self.rules = GrammarRules().getTokenRules()

    def applyToToken(self, token):
        tokenType = token.getType().__class__.__name__
        if tokenType in self.rules.keys():
            return self.rules[tokenType]
        else:
            raise Exception("Token type not valid!")
