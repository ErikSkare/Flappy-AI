import sys, random, pygame
from app.bird import Bird
from app.pipe import Pipe, pipe_width, pipe_gap, pipe_velocity_x


window_bg_color = (0, 0, 0)
pipes_distance_between = 200
pipes_range_margin = 20


class Window(object):
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.birds = [Bird(100)]
        self.pipes = [Pipe(width, 100)]
        self.frame_count = 1

    def start_game_loop(self, max_fps):
        clock = pygame.time.Clock()
    
        while True:
            events = pygame.event.get()
            dt = clock.tick(max_fps) / 1000
            
            self.should_close(events)
            self.screen.fill(window_bg_color)
            
            if not (self.frame_count % (max_fps * pipes_distance_between / abs(pipe_velocity_x))): 
                self.pipes.append(Pipe(self.width, random.randint(pipes_range_margin, self.height - pipe_gap - pipes_range_margin)))

            if self.pipes[0].x_pos < -pipe_width: self.pipes.remove(self.pipes[0])
    
            for bird in self.birds:
                bird.render(self.screen, events, dt)

            for pipe in self.pipes:
                pipe.render(self.screen, events, dt)

            pygame.display.update()
            self.frame_count += 1

    def should_close(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

