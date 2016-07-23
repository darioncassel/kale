class ByteCode(object):

    def stackPush():
        def func(machine, data):
            machine.stack.append(data)
        return func
    
    def stackPop():
        def func(machine, data):
            x = machine.stack.pop()
            machine.temp.append(x)
        return func
    
    def checkIsVar():
        def func(machine, data):
            var = machine.temp.pop()
            if var in machine.vars.keys():
                machine.stack.append(1)
            else:
                machine.stack.append(0)
        return func
    
    def branch():
        def func(machine, data):
            x = machine.stack.pop()
            if x == 0:
                machine.skip1 = True
            elif x == 1:
                machine.skip2 = True
            else:
                raise Exception("Invalid call to branch!")
        return func
    
    def accessVar():
        def func(machine, data):
            var = machine.temp.pop()
            if var in machine.vars.keys():
                value = machine.vars[var]
                machine.stack.append(value)
            else:
                raise Exception("Invalid var accessed!")
        return func
    
    def addrPush():
        def func(machine, data):
            var = machine.temp.pop()
            val = machine.temp.pop()
            if var in machine.vars.keys():
                machine.vars[var] = val
            else:
                raise Exception("Invalid var accessed!")
        return func

    def addOp():
        def func(machine, data):
            x = machine.temp.pop()
            y = machine.temp.pop()
            sum = x + y
            machine.stack.append(sum)
            machine.temp = []
        return func
    
    def subOp():
        def func(machine, data):
            x = machine.temp.pop()
            y = machine.temp.pop()
            sum = x - y
            machine.stack.append(sum)
            machine.temp = []
        return func
    
    def multOp():
        def func(machine, data):
            x = machine.temp.pop()
            y = machine.temp.pop()
            sum = x * y
            machine.stack.append(sum)
            machine.temp = []
        return func
    
    def divOp():
        def func(machine, data):
            x = machine.temp.pop()
            y = machine.temp.pop()
            sum = x / float(y)
            machine.stack.append(sum)
            machine.temp = []
        return func
    
    def allocateVar():
        def func(machine, data):
            name = machine.temp.pop()
            machine.vars[name] = None
        return func
    
    opToFuncMap = {
        "None" : None,
        "stackPush": stackPush,
        "stackPop": stackPop,
        "addOp": addOp,
        "subOp": subOp,
        "multOp": multOp,
        "divOp": divOp,
        "allocateVar": allocateVar,
        "checkIsVar": checkIsVar,
        "branch": branch,
        "accessVar": accessVar,
        "addrPush": addrPush
    }
    
    def getOperation(self, opString):
        func = self.opToFuncMap[opString]
        if func:
            return func()
            
    

