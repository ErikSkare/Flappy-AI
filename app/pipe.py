import pygame
from app.actor import Actor
from app.utils import collision_rect_circle
from app.constants import bird_x_pos, bird_radius, pipe_width, pipe_gap, pipe_color, pipe_velocity_x


class Pipe(Actor):
    def __init__(self, x_start, gap_y_start):
        self.x_pos = x_start
        self.gap_y_start = gap_y_start

    def update_state(self, events, dt, window):
        self.x_pos += pipe_velocity_x * dt

    def draw(self, window):
        width, height = window.screen.get_size()
        top_rect = (self.x_pos,
                    0,
                    pipe_width,
                    self.gap_y_start)
        bottom_rect = (self.x_pos,
                       self.gap_y_start + pipe_gap,
                       pipe_width,
                       height - (self.gap_y_start + pipe_gap))
        pygame.draw.rect(window.screen, pipe_color, top_rect)
        pygame.draw.rect(window.screen, pipe_color, bottom_rect)

    def collision_with_bird(self, screen, bird):
        width, height = screen.get_size()

        with_top_rect = collision_rect_circle(self.x_pos, 
                                              0, 
                                              pipe_width, 
                                              self.gap_y_start, 
                                              bird_x_pos,
                                              int(bird.y_pos),
                                              bird_radius)

        with_bottom_rect = collision_rect_circle(self.x_pos,
                                                 self.gap_y_start + pipe_gap,
                                                 pipe_width,
                                                 height - (self.gap_y_start + pipe_gap),
                                                 bird_x_pos,
                                                 int(bird.y_pos),
                                                 bird_radius)

        return with_top_rect or with_bottom_rect