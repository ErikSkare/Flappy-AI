import random
from app.ai.neuron import Neuron
from app.ai.connection import Connection


class NeuralNetwork(object):
    def __init__(self, input_num, hidden_num, output_num):
        self.input_neurons = []
        for i in range(input_num):
            self.input_neurons.append(Neuron([], random.uniform(-1, 1)))
        
        self.hidden_neurons = []
        for i in range(hidden_num):
            connections = NeuralNetwork.get_random_connections(self.input_neurons)
            self.hidden_neurons.append(Neuron(connections, random.uniform(-1, 1)))
        
        self.output_neurons = []
        for i in range(output_num):
            connections = NeuralNetwork.get_random_connections(self.hidden_neurons)
            self.output_neurons.append(Neuron(connections, random.uniform(-1, 1)))

    def get_result(self, inputs):
        if len(inputs) != len(self.input_neurons): raise ValueError("wrong dimension")
        self.reset()
        for i in range(len(inputs)):
            self.input_neurons[i].value = inputs[i]

        results = []
        # calculating in depth-first manner.
        for neuron in self.output_neurons:
            results.append(neuron.get_value())

        return results

    def reset(self):
        for neuron in self.input_neurons:
            neuron.reset()

        for neuron in self.hidden_neurons:
            neuron.reset()

        for neuron in self.output_neurons:
            neuron.reset()

    @staticmethod
    def get_random_connections(neurons):
        connections = []
        for neuron in neurons:
            connections.append(Connection(neuron, random.uniform(-1, 1)))
        return connections
