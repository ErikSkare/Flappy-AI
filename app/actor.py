from abc import ABC, abstractmethod


class Actor(ABC):
	def render(self, window, events, dt):
		self.update_state(events, dt, window)
		self.draw(window)

	@abstractmethod
	def update_state(self, events, dt, window):
		pass
	
	@abstractmethod
	def draw(self, window):
		pass

