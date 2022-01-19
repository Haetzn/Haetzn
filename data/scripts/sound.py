import pygame

class Sound:
	def __init__(self):
		self.load()

	def load(self):
		#load sounds:
		self.clicksound = pygame.mixer.Sound("data/sounds/click.wav")
		self.hoversound = pygame.mixer.Sound("data/sounds/hover.wav")
		self.bonksound = pygame.mixer.Sound("data/sounds/bonk.wav")
		self.boomsound = pygame.mixer.Sound("data/sounds/boom.wav")
		self.eatsound = pygame.mixer.Sound("data/sounds/eat.wav")