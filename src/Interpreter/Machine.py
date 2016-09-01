class Machine(object):

    def __init__(self):
        self.stack = []
        self.vars = {}

    def __repr__(self):
        output = "Stack: " + str(self.stack)
        output += "\nVars: " + str(self.vars)
        return output
