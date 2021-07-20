import pygame
from app.actor import Actor


bird_radius = 10
bird_x_pos = 50
bird_color = (255, 255, 255)
bird_down_acceleration = 1000


class Bird(Actor):
	def __init__(self, y_start):
		self.y_pos = y_start
		self.y_velocity = 0

	def update_state(self, events, dt):
		self.y_velocity += bird_down_acceleration * dt
		self.y_pos += self.y_velocity * dt

	def draw(self, screen):
		center = (bird_x_pos, int(self.y_pos))
		pygame.draw.circle(screen, bird_color, center, bird_radius)

