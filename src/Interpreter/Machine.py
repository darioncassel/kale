class Machine(object):

    def __init__(self):
        self.skip1 = False
        self.skip2 = False
        self.stack = []
        self.temp = []
        self.vars = {}
    
    def __repr__(self):
        output = "Stack: " + str(self.stack)
        output += "\nTemp: " + str(self.temp)
        output += "\nVars: " + str(self.vars)
        output += "\nSkip1: " + str(self.skip1)
        output += "\nSkip2: " + str(self.skip2)
        return output
