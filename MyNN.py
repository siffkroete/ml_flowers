e = 2.718281828459 

class MyNN:
    layer = [3, 3, 2]
    bias = [0, 0, 0]
    weights = []

    def activationFunc(self, z):
        return (1/(1+pow(e, -z)))

    def inputFunc(self, inputVec, bias, layerNr):
        return sum(inputVec) + bias

    def neuron(self, inputVec, bias, layerNr):
        r = self.inputFunc(inputVec, bias, layerNr)
        return self.activationFunc(r)

    def costFunc(self):
        return 0

    def forward(self):
        return 0

    def backpropagation(self):
        return 0