class Connection(object):
    def __init__(self, from_neuron, weight):
        self.from_neuron = from_neuron
        self.weight = weight

    def evaluate(self):
        return self.from_neuron.get_value() * self.weight

