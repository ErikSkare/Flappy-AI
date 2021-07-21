import pygame
from app.actor import Actor


bird_radius = 10
bird_x_pos = 50
bird_color = (255, 255, 255)
bird_down_acceleration = 1500
jump_velocity = -25000


class Bird(Actor):
    def __init__(self, y_start, keyboard_input_enabled = True):
        self.keyboard_input_enabled = keyboard_input_enabled
        self.y_pos = y_start
        self.y_velocity = 0
        self.should_jump = False
        self.is_pressing_space = False

    def update_state(self, events, dt):
        self.y_velocity += bird_down_acceleration * dt

        if self.keyboard_input_enabled: self.process_keyboard_input(events)

        if self.should_jump: 
            self.y_velocity = jump_velocity * dt
            self.should_jump = False

        self.y_pos += self.y_velocity * dt

    def draw(self, screen):
        center = (bird_x_pos, int(self.y_pos))
        pygame.draw.circle(screen, bird_color, center, bird_radius)

    def jump(self):
        self.should_jump = True

    def process_keyboard_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.is_pressing_space:
                self.is_pressing_space = True
                self.jump()
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.is_pressing_space = False

