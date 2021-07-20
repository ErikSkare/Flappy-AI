import sys, pygame
from app.bird import Bird
#from app.pipe import Pipe


window_bg_color = (0, 0, 0)


class Window(object):
	def __init__(self, width, height):
		pygame.init()
		self.screen = pygame.display.set_mode((width, height))
		self.birds = [Bird(100)]
		self.pipes = []

	def start_game_loop(self, max_fps):
		clock = pygame.time.Clock()
	
		while True:
			events = pygame.event.get()
			dt = clock.tick(max_fps) / 1000
			
			self.should_close(events)
			self.screen.fill(window_bg_color)

			for bird in self.birds:
				bird.render(self.screen, events, dt)

			for pipe in self.pipes:
				pipe.render(self.screen, events, dt)

			pygame.display.update()

	def should_close(self, events):
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

