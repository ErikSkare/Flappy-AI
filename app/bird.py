import pygame
from app.actor import Actor
from app.ai.neural_network import NeuralNetwork
from app.constants import bird_radius, bird_x_pos, bird_color, bird_down_acceleration, bird_jump_velocity, pipe_gap


class Bird(Actor):
    def __init__(self, y_start, keyboard_input_enabled = True):
        self.keyboard_input_enabled = keyboard_input_enabled
        self.y_pos = y_start
        self.y_velocity = 0
        self.should_jump = False
        self.is_pressing_space = False
        if not keyboard_input_enabled: self.brain = NeuralNetwork(4, 6, 1)

    def update_state(self, events, dt, window):
        if self.keyboard_input_enabled: self.process_keyboard_input(events)
        else: self.predict_with_network(window)

        self.y_velocity += bird_down_acceleration * dt
        
        if self.should_jump: 
            self.y_velocity = bird_jump_velocity
            self.should_jump = False

        self.y_pos += self.y_velocity * dt

    def draw(self, window):
        center = (bird_x_pos, int(self.y_pos))
        pygame.draw.circle(window.screen, bird_color, center, bird_radius)

    def jump(self):
        self.should_jump = True

    def process_keyboard_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.is_pressing_space:
                self.is_pressing_space = True
                self.jump()
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.is_pressing_space = False

    def predict_with_network(self, window):
            next_pipe = window.get_next_pipe()
            
            gap_y_start_normalized = next_pipe.gap_y_start / window.height
            gap_y_end_normalized = (next_pipe.gap_y_start + pipe_gap) / window.height
            pipe_x_pos_normalized = next_pipe.x_pos / window.width
            bird_y_pos_normalized = self.y_pos / window.height
            
            result = self.brain.get_result([pipe_x_pos_normalized, 
                                            gap_y_start_normalized, 
                                            gap_y_end_normalized, 
                                            bird_y_pos_normalized])[0]
            if result > 0.5: self.jump()   

