import unittest
from Tokenizer.Token import Token
from Tokenizer.Tokenizer import Tokenizer

class testTokenizer(unittest.TestCase):

    def setUp(self):
        self.filename = "test.kl"
        self.tokenizer = Tokenizer(self.filename)
    
    def testInit(self):
        self.tokenizer = Tokenizer(self.filename)
        self.assertEqual(self.tokenizer.tokens,
                         [], "Tokens not initialized correctly")
        with open(self.filename, "r") as f:
            thisFile = f.readlines()
            self.assertEqual(self.tokenizer.file,
                             thisFile,
                             "File not initialized correctly")
    
    def testTokenize(self):
        lines = ["a line", "the four"]
        tokens = []
        tokens.append(Token(0, "a", None))
        tokens.append(Token(1, "line", None))
        tokens.append(Token(2, "the", None))
        tokens.append(Token(3, "four", None))
        self.tokenizer.file = lines
        self.tokenizer.tokenize()
        for token1, token2 in zip(self.tokenizer.tokens, tokens):
            self.assertEqual(token1.id, token2.id,
                            "Tokenization incorect")
            self.assertEqual(token1.literal, token2.literal,
                            "Tokenization incorect")
            self.assertEqual(type(token1.type), type(token2.type),
                            "Tokenization incorect")
    
    def testGetTokens(self):
        lines = ["a line", "the four"]
        tokens = []
        tokens.append(Token(0, "a", None))
        tokens.append(Token(1, "line", None))
        tokens.append(Token(2, "the", None))
        tokens.append(Token(3, "four", None))
        self.tokenizer.file = lines
        self.tokenizer.tokenize()
        for token1, token2 in zip(self.tokenizer.getTokens(), tokens):
            self.assertEqual(token1.id, token2.id,
                            "Tokenization incorect")
            self.assertEqual(token1.literal, token2.literal,
                            "Tokenization incorect")
            self.assertEqual(type(token1.type), type(token2.type),
                            "Tokenization incorect")
