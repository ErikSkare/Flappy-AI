from app.utils import sigmoid


class Neuron(object):
    def __init__(self, connections, bias):
        self.connections = connections
        self.bias = bias
        self.value = None

    def get_value(self):
        if self.value != None: return self.value

        total = self.bias
        for connection in self.connections:
            total += connection.evaluate()

        self.value = sigmoid(total)
        return self.value

    def reset(self):
        self.value = None

