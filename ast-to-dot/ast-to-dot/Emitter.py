class Emitter():
    END = ";\n"
    

    def __init__(self, filename):
        self.filename = filename
        self.code = ""
        self.p = 0
        self.IO = 0
        self.d = 0

    def Code(self):
        return self.code

    def emitStartGraph(self, name):
        '''
            Start a graph
        '''
        self.code += "digraph" + name + "\n{"

    def emitTerminal(self, begin: bool):
        '''
            Emit terminal node of graph
                begin == true -> Begin node
                else -> End node
            Return name of node
        '''
        if begin:
            self.code += "_begin_" + '[shape=oval,label="Begin"]' + Emitter.END
            return "_begin_"

        else:
            self.code += "_end_" + '[shape=oval,label="End"]' + Emitter.END
            return "_end_"

    def emitProcess(self, label: str):
        '''
            Emit process node of graph
            label: content of process
            Return name of node
        '''
        self.code += "p" + str(self.p) + '"[shape=rectangle,label="' + label + '"]' + Emitter.END
        self.p += 1
        return "p" + str(self.p - 1)

    def emitIO(self, label: str, input: bool):
        '''
            Emit Input/Output node of graph
                input == true -> Input node
                else -> Output node
            label: content of process
            Return name of node
        '''
        if input:
            prefix = "Input"
        else:
            prefix = "Return"

        self.code += "io" + str(self.IO) + '[shape=parallelogram,label="' + label + '"]' + Emitter.END
        self.IO += 1
        return "io" + str(self.IO - 1)

    def emitDecision(self, label: str):
        '''
            Emit Decision node of graph
            label: content of condition
            Return name of node
        '''
        self.code += "d" + str(self.d) + '[shape=diamond,label="' + label + '"]' + Emitter.END
        self.d += 1
        return "d" + str(self.d - 1)

    def emitConnect(self, fromNode: str, toNode: str):
        '''
            Emit direct from node to node
        '''
        self.code += fromNode + " -> " + toNode + Emitter.END

    def emitTrueBranch(self, fromNode: str, toNode: str):
        '''
            Emit true branch direct from node to node
        '''
        self.code += fromNode + " -> " + toNode + '[label="True"]' + Emitter.END

    def emitFalseBranch(self, fromNode: str, toNode: str):
        '''
            Emit false branch direct from node to node
        '''
        self.code += fromNode + " -> " + toNode + '[label="False"]' + Emitter.END

    def emitEndGraph(self):
        '''
            End a graph
        '''
        self.code += "}\n"