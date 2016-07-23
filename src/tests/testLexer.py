import unittest
from Tokenizer.Token import Token
from Lexer.Lexer import Lexer
from Types.Types import commentType, numType, addOpType, \
    subOpType, multOpType, divOpType, statementBeginType, \
    statementEndType

class testLexer(unittest.TestCase):

    def setUp(self):
        self.lexer = Lexer(None)

    def testInit(self):
        tokens = []
        tokens.append(Token(0, "a", None))
        tokens.append(Token(1, "line", None))
        tokens.append(Token(2, "the", None))
        tokens.append(Token(3, "four", None))
        self.lexer = Lexer(tokens)
        self.assertEqual(self.lexer.tokens, tokens,
                         "Initialization not correct")
    
    def testLexNoComments(self):
        tokens = []
        tokens.append(Token(0, "(", None))
        tokens.append(Token(1, ")", None))
        tokens.append(Token(2, "+", None))
        tokens.append(Token(3, "-", None))
        tokens.append(Token(4, "*", None))
        tokens.append(Token(5, "/", None))
        tokens.append(Token(6, "11", None))
        self.lexer = Lexer(tokens)
        self.lexer.lex()
        tokens = []
        tokens.append(Token(0, "(", statementBeginType()))
        tokens.append(Token(1, ")", statementEndType()))
        tokens.append(Token(2, "+", addOpType()))
        tokens.append(Token(3, "-", subOpType()))
        tokens.append(Token(4, "*", multOpType()))
        tokens.append(Token(5, "/", divOpType()))
        tokens.append(Token(6, 11, numType()))
        for token1, token2 in zip(self.lexer.tokens, tokens):
            self.assertEqual(token1.id, token2.id,
                            "Tokenization incorect")
            self.assertEqual(token1.literal, token2.literal,
                            "Tokenization incorect")
            self.assertEqual(type(token1.type), type(token2.type),
                            "Tokenization incorect")
    def testLexComments(self):
        tokens = []
        tokens.append(Token(0, "#", None))
        tokens.append(Token(1, ")", None))
        tokens.append(Token(2, "+", None))
        tokens.append(Token(3, "-", None))
        tokens.append(Token(4, "*", None))
        tokens.append(Token(5, "/", None))
        tokens.append(Token(6, "#", None))
        self.lexer = Lexer(tokens)
        self.lexer.lex()
        tokens = []
        tokens.append(Token(0, "#", commentType()))
        tokens.append(Token(1, ")", commentType()))
        tokens.append(Token(2, "+", commentType()))
        tokens.append(Token(3, "-", commentType()))
        tokens.append(Token(4, "*", commentType()))
        tokens.append(Token(5, "/", commentType()))
        tokens.append(Token(6, "#", commentType()))
        for token1, token2 in zip(self.lexer.tokens, tokens):
            self.assertEqual(token1.id, token2.id,
                            "Tokenization incorect")
            self.assertEqual(token1.literal, token2.literal,
                            "Tokenization incorect")
            self.assertEqual(type(token1.type), type(token2.type),
                            "Tokenization incorect")
    
    def testGetTokensPreLex(self):
        tokens = []
        tokens.append(Token(0, "#", None))
        tokens.append(Token(1, ")", None))
        tokens.append(Token(2, "+", None))
        tokens.append(Token(3, "-", None))
        tokens.append(Token(4, "*", None))
        tokens.append(Token(5, "/", None))
        tokens.append(Token(6, "#", None))
        self.lexer = Lexer(tokens)
        for token1, token2 in zip(self.lexer.getTokens(), tokens):
            self.assertEqual(token1.id, token2.id,
                            "Tokenization incorect")
            self.assertEqual(token1.literal, token2.literal,
                            "Tokenization incorect")
            self.assertEqual(type(token1.type), type(token2.type),
                            "Tokenization incorect")
    
    def testGetTokensPostLex(self):
        tokens = []
        tokens.append(Token(0, "(", None))
        tokens.append(Token(1, ")", None))
        tokens.append(Token(2, "+", None))
        tokens.append(Token(3, "-", None))
        tokens.append(Token(4, "*", None))
        tokens.append(Token(5, "/", None))
        tokens.append(Token(6, "11", None))
        self.lexer = Lexer(tokens)
        self.lexer.lex()
        tokens = []
        tokens.append(Token(0, "(", statementBeginType()))
        tokens.append(Token(1, ")", statementEndType()))
        tokens.append(Token(2, "+", addOpType()))
        tokens.append(Token(3, "-", subOpType()))
        tokens.append(Token(4, "*", multOpType()))
        tokens.append(Token(5, "/", divOpType()))
        tokens.append(Token(6, 11, numType()))
        for token1, token2 in zip(self.lexer.getTokens(), tokens):
            self.assertEqual(token1.id, token2.id,
                            "Tokenization incorect")
            self.assertEqual(token1.literal, token2.literal,
                            "Tokenization incorect")
            self.assertEqual(type(token1.type), type(token2.type),
                            "Tokenization incorect")
