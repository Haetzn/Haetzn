import pygame

class Img:
	def __init__(self, _d):
		self._d = _d
		self.loadimgs()

	def loadimgs(self):
		snakesize = int(self._d.currentres[1] * (16/1080))
		

		self.icon = pygame.image.load("data/imgs/snake_head.png").convert_alpha()
		#Snake
		
		self.snakebody = pygame.image.load("data/imgs/snake_body.png").convert()
		self.snakebody = pygame.transform.scale(self.snakebody, (snakesize, snakesize))
		self.snakebody.set_colorkey((255, 255, 255))
		self.snakebodyeat = pygame.image.load("data/imgs/snake_eat0.png").convert()
		self.snakebodyeat = pygame.transform.scale(self.snakebodyeat, (snakesize, snakesize))
		self.snakebodyeat.set_colorkey((255, 255, 255))
		self.snakebodyturn = pygame.image.load("data/imgs/snake_body0.png").convert()
		self.snakebodyturn = pygame.transform.scale(self.snakebodyturn, (snakesize, snakesize))
		self.snakebodyturn.set_colorkey((255, 255, 255))
		self.snakebodytail = pygame.image.load("data/imgs/snake_body2.png").convert()
		self.snakebodytail = pygame.transform.scale(self.snakebodytail, (snakesize, snakesize))
		self.snakebodytail.set_colorkey((255, 255, 255))
		self.snakehead = pygame.image.load("data/imgs/snake_head.png").convert()
		self.snakehead = pygame.transform.scale(self.snakehead, (snakesize, snakesize))
		self.snakehead.set_colorkey((255, 255, 255))
		self.snakeheadeat = pygame.image.load("data/imgs/snake_eat1.png").convert()
		self.snakeheadeat = pygame.transform.scale(self.snakeheadeat, (snakesize, snakesize))
		self.snakeheadeat.set_colorkey((255, 255, 255))

		

		#Items
		self.apple = pygame.image.load("data/imgs/apple.png").convert()
		self.apple = pygame.transform.scale(self.apple, (snakesize, snakesize))
		self.apple.set_colorkey((255, 255, 255))
		self.bomb = pygame.image.load("data/imgs/bomb.png").convert()
		self.bomb = pygame.transform.scale(self.bomb, (snakesize, snakesize))
		self.bomb.set_colorkey((255, 255, 255))

		#cursor
		self.cursor = pygame.image.load("data/imgs/cursor.png").convert()
		self.cursor.set_colorkey((255, 255, 255))
		self.cursor = pygame.transform.scale(self.cursor, (int(self._d.currentres[0]/ 60), int(self._d.currentres[0] /60)))
		self.cursorpressed = pygame.image.load("data/imgs/cursorpressed.png").convert()
		
		self.cursorpressed.set_colorkey((255, 255, 255))
		self.cursorpressed = pygame.transform.scale(self.cursorpressed, (int(self._d.currentres[0]/60), int(self._d.currentres[0]/60)))
		self.cursorright = pygame.image.load("data/imgs/cursorright.png").convert()
		self.cursorright.set_colorkey((255, 255, 255))
		self.cursorright = pygame.transform.scale(self.cursorright, (int(self._d.currentres[0]/60), int(self._d.currentres[0]/60)))
		self.cursorrightpressed = pygame.image.load("data/imgs/cursorrightpressed.png").convert()
		self.cursorrightpressed.set_colorkey((255, 255, 255))
		self.cursorrightpressed = pygame.transform.scale(self.cursorrightpressed, (int(self._d.currentres[0]/60), int(self._d.currentres[0]/60)))
