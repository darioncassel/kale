import unittest
from Tokenizer.Token import Token
from Types.Types import numType


class testToken(unittest.TestCase):

    def setUp(self):
        self.token = Token(None, None, None)
    
    def testInit(self):
        self.token = Token(11, "11", numType())
        id = self.token.getId()
        self.assertEqual(id, 11, 
                         "Id not set correctly")
        literal = self.token.getLiteral()
        self.assertEqual(literal, "11", 
                         "Literal not set correctly")
        thisType = type(self.token.getType())
        self.assertEqual(thisType, numType,
                         "Type not set correctly")
    
    def testGetId(self):
        id = self.token.getId()
        self.assertEqual(id, None, 
                         "Id not set correctly")
    def testGetLiteral(self):
        literal = self.token.getLiteral()
        self.assertEqual(literal, None, 
                         "Literal not set correctly")
    
    def testGetType(self):
        thisType = type(self.token.getType())
        self.assertEqual(thisType, type(None),
                         "Type not set correctly")
    
    def testSetId(self):
        self.token.setId(11)
        id = self.token.getId()
        self.assertEqual(id, 11, 
                         "Id not set correctly")
    
    def testSetLiteral(self):
        self.token.setLiteral("11")
        literal = self.token.getLiteral()
        self.assertEqual(literal, "11", 
                         "Literal not set correctly")
    
    def testSetType(self):
        self.token.setType(numType())
        thisType = type(self.token.getType())
        self.assertEqual(thisType, numType,
                         "Type not set correctly")
    
    def testRepr(self):
        self.token = Token(11, "11", numType())
        repr = str(self.token)
        setStr = "T(id=11 literal=11 type=numType)"
        self.assertEqual(repr, setStr,
                         "Repr not working correctly")
