from app.bird import Bird
from app.ai.operations import mate


class PopulationManager(object):
    def __init__(self, population_size):
        self.population_size = population_size
        self.order = []

    def add_dead_network(self, network):
        self.order.append(network)

    def get_next_population(self):
        if not len(self.order): return self.get_random_population()
        self.order.reverse()
        birds = []
        for i in range(self.population_size - 2):
            new_bird = Bird(150, False)
            new_brain = mate(self.order[0], self.order[1])
            new_bird.brain = new_brain
            birds.append(new_bird)

        for i in range(2):
            new_bird = Bird(150, False)
            new_brain = self.order[i]
            new_bird.brain = new_brain
            birds.append(new_bird)

        self.order = []
        return birds

    def get_random_population(self):
        birds = []
        for i in range(self.population_size):
            birds.append(Bird(150, False))
        return birds