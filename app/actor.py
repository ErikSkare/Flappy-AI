from abc import ABC, abstractmethod


class Actor(ABC):
	def render(self, screen, events, dt):
		self.update_state(events, dt)
		self.draw(screen)

	@abstractmethod
	def update_state(self, events, dt):
		pass
	
	@abstractmethod
	def draw(self, screen):
		pass

