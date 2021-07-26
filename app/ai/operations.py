import copy, random
from app.constants import mutation_rate


def mutate(network):
    def group(neurons):
        for neuron in neurons:
            if random.uniform(0, 1) <= mutation_rate:
                neuron.bias = random.uniform(-1, 1)
            for connection in neuron.connections:
                if random.uniform(0, 1) <= mutation_rate:
                    connection.weight = random.uniform(-1, 1)
    
    network_cpy = copy.deepcopy(network)
    
    group(network_cpy.hidden_neurons)
    group(network_cpy.output_neurons)
    
    return network_cpy


def mate(network1, network2):
    def group(result_neurons, merging_neurons):
        for i in range(len(result_neurons)):
            if random.uniform(0, 1) >= 0.5:
                result_neurons[i].bias = merging_neurons[i].bias
            for j in range(len(result_neurons[i].connections)):
                if random.uniform(0, 1) >= 0.5:
                    result_neurons[i].connections[j].weight = merging_neurons[i].connections[j].weight
    
    result = copy.deepcopy(network1)
    
    group(result.hidden_neurons, network2.hidden_neurons)
    group(result.output_neurons, network2.output_neurons)
    
    return mutate(result)


def view(network):
    def group(neurons):
        for neuron in neurons:
            print(neuron.bias)
            for connection in neuron.connections:
                print(connection.weight, end = " ")
            print("\n")
    
    print("Hidden neurons")
    group(network.hidden_neurons)
    
    print("Output neurons")
    group(network.output_neurons)