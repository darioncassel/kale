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
    
    def allocateVar():
        def func(machine, data):
            name = machine.stack.pop()
            machine.vars[name] = None
        return func
    
    def accessVar():
        def func(machine, data):
            var = machine.stack.pop()
            if var in machine.vars.keys():
                value = machine.vars[var]
                machine.stack.append(value)
            else:
                raise Exception("Invalid var accessed!")
        return func
    
    def addrPush():
        def func(machine, data):
            val = machine.stack.pop()
            var = machine.stack.pop()
            if var in machine.vars.keys():
                machine.vars[var] = val
            else:
                raise Exception("Invalid var accessed!")
        return func

    def addOp():
        def func(machine, data):
            y = machine.stack.pop()
            x = machine.stack.pop()
            sum = x + y
            machine.stack.append(sum)
        return func
    
    def subOp():
        def func(machine, data):
            y = machine.stack.pop()
            x = machine.stack.pop()
            sum = x - y
            machine.stack.append(sum)
        return func
    
    def multOp():
        def func(machine, data):
            y = machine.stack.pop()
            x = machine.stack.pop()
            sum = x * y
            machine.stack.append(sum)
        return func
    
    def divOp():
        def func(machine, data):
            y = machine.stack.pop()
            x = machine.stack.pop()
            sum = x / float(y)
            machine.stack.append(sum)
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
        "accessVar": accessVar,
        "addrPush": addrPush
    }
    
    def getOperation(self, opString):
        func = self.opToFuncMap[opString]
        if func:
            return func()
            
    

