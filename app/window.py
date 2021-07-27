import sys, random, pygame
from app.bird import Bird
from app.pipe import Pipe
from app.population_manager import PopulationManager
from app.constants import window_bg_color, pipes_distance_between, pipes_range_margin, pipe_width, pipe_gap, pipe_velocity_x, bird_x_pos, bird_radius


class Window(object):
    def __init__(self, width, height, ai_enabled=True):
        pygame.init()
        self.width = width
        self.height = height
        self.ai_enabled = ai_enabled
        self.screen = pygame.display.set_mode((width, height))
        if ai_enabled: self.population_manager = PopulationManager(100)

    def start_game_loop(self, max_fps):
        clock = pygame.time.Clock()
        self.reset_game()

        while True:
            events = pygame.event.get()
            dt = clock.tick(max_fps) / 1000

            self.should_close(events)
            self.screen.fill(window_bg_color)
            
            if not (self.frame_count % (max_fps * pipes_distance_between / abs(pipe_velocity_x))): 
                self.pipes.append(Pipe(self.width, random.randint(pipes_range_margin, self.height - pipe_gap - pipes_range_margin)))

            if self.pipes[0].x_pos < -pipe_width: self.pipes.remove(self.pipes[0])

            next_pipe = self.get_next_pipe()

            for bird in self.birds:
                if (next_pipe.collision_with_bird(self.screen, bird) or
                    bird.y_pos < bird_radius or 
                    bird.y_pos > self.height - bird_radius): 
                        if self.ai_enabled: self.population_manager.add_dead_network(bird.brain)
                        self.birds.remove(bird)
                else: bird.render(self, events, dt)

            for pipe in self.pipes:
                pipe.render(self, events, dt)

            pygame.display.update()
            self.frame_count += 1
            
            if len(self.birds) == 0: self.reset_game()

    def should_close(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def get_next_pipe(self):
        for pipe in self.pipes:
            if pipe.x_pos + pipe_width >= bird_x_pos - bird_radius: return pipe

    def reset_game(self):
        if self.ai_enabled:
            self.birds = self.population_manager.get_next_population()
        else: self.birds = [Bird(150, True)]
        print(len(self.birds))
        self.pipes = [Pipe(self.width, random.randint(pipes_range_margin, self.height - pipe_gap - pipes_range_margin))]
        self.frame_count = 1
