import pygame
from app.actor import Actor


pipe_width = 30
pipe_gap = 50
pipe_color = (255, 255, 255)
pipe_velocity_x = 200


class Pipe(Actor):
    def __init__(self, x_start, gap_y_start):
        self.x_pos = x_start
        self.gap_y_start = gap_y_start

    def update_state(self, events, dt):
        self.x_pos -= pipe_velocity_x * dt

    def draw(self, screen):
        width, height = screen.get_size()
        top_rect = (self.x_pos,
                    0,
                    pipe_width,
                    self.gap_y_start)
        bottom_rect = (self.x_pos,
                       self.gap_y_start + pipe_gap,
                       pipe_width,
                       height - (self.gap_y_start + pipe_gap))
        pygame.draw.rect(screen, pipe_color, top_rect)
        pygame.draw.rect(screen, pipe_color, bottom_rect)

