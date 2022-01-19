import pygame, random

class Main:
	def __init__(self, data, funks, img, sound):
		self._d = data
		self._f = funks
		self._i = img
		self._s = sound


		self.start()

	def start(self):
		#Game vars
		self.GRIDSIZE = int(self._d.currentres[1]/67.5)
		self.GRIDxy = int(self._d.currentres[1]/2.7)
		self._f.gridmuster = self._f.schachmuster(self.GRIDxy, self.GRIDSIZE, (31, 31, 31), (100, 100, 100))
		

		self._d.score = 0
		self._d.pausescreen = False

		self.update_time_max = 7
		self.update_time = self.update_time_max
		self.snake_direction = "right"

		self.snake_posx = [0,-1,-2,-3]
		self.snake_posy = [1, 1, 1, 1]
		self.eat = False

		self.bonk = False
		self.deadtimer = 10

		self.snakefall_time_max = 10
		self.snakefall_time = 0

		self.newhighscore = False

		self.runninggame = True
		self.onekey = False
		self.w_down = False
		self.d_down = False
		self.s_down = False
		self.a_down = False

		self.holddowntime = 10
		self.holdspeed = 2.5

		self.w_down_timer = self.holddowntime
		self.d_down_timer = self.holddowntime
		self.s_down_timer = self.holddowntime
		self.a_down_timer = self.holddowntime

		self.shakes = []

		#Apples
		self.apple_xgrid = -2
		self.apple_ygrid = -2
		self.apple_x = -2
		self.apple_y = -2

		#Bombs
		self.bomb_xgrid = []
		self.bomb_ygrid = []
		self.bomb_x = []
		self.bomb_y = []
		self.bombspawntimermax = 50
		self.bombspawntimer = 0

		self.runninggame = True

		self.spawnApple()

	def gameloop(self, mouse_pos, click):
		if self._d.ingame and not self._d.pausescreen and not self._d.exitscreen and self.runninggame:
		
			self.update_time -= 1

			if self.w_down:
				self.w_down_timer -= 1
			if self.a_down:
				self.a_down_timer -= 1
			if self.s_down:
				self.s_down_timer -= 1
			if self.d_down:
				self.d_down_timer -= 1

			if self.w_down_timer <= 0 or self.a_down_timer <= 0 or self.d_down_timer <= 0 or self.s_down_timer <= 0:
				self.update_time -= self.holdspeed
			

			if self.update_time <= 0:
				self.update_time = self.update_time_max
				self._d.surf.fill((31,31,31))
				self._d.surf.blit(self._f.gridmuster, ((self._d.surfsize[0]/2) - (self.GRIDxy/2), (self._d.surfsize[1]/2) - (self.GRIDxy/2)))
				if not self.bonk:
					self.move(self.snake_direction)
					self.onekey = False
				else:
					for i in range(20):
						self._f.particles.append([[((self.snake_posx[0]*self.GRIDSIZE) + (self._d.surfsize[0]/2) - (self.GRIDxy/2))*2, ((self.snake_posy[0]*self.GRIDSIZE) + (self._d.surfsize[1]/2) - (self.GRIDxy/2))*2], [random.randint(-10, 10)/10, random.randint(-10, 10)/10 ], random.randint(6, self.GRIDSIZE), (0, 255, 69)])
					self.snakefall()
					self.deadtimer -= 1
					#nach bonk soll nach den shakes running false sein damit dead screen an
					if len(self.shakes) <= 0 and self.deadtimer <= 0:
						self.runninggame = False
				self.snakecollison()
				if self._d.bordercollisions:
					self.bordercollisions(self.snake_posx[0], self.snake_posy[0])

				#update score
				if self._d.scorebefore != self._d.score:
					self._f.createtext("score", [0, -self._d.currentres[1]//2.2], int(self._d.currentres[1]*(100/1080)), str(self._d.score), (187, 187, 187))
					self._d.scorebefore = self._d.score
	
				self.applecollision()
				self.spawnBomb()
				self.bombcollision()
				#render apple
				self._d.surf.blit(self._i.apple, (self.apple_x, self.apple_y))
				self.renderbomb()
				#RENDER snake
				self.renderSnake()

	
	
		self._d.surfblit = pygame.transform.scale(self._d.surf, (self._d.currentres[0], self._d.currentres[1]))

		#surf wird in screenshake auf screen gerendert :)
		#aus dem grund damit alles wackeln kann wenn es muss
		self._f.draw_screenshake(self._d.screen, self._d.surfblit, self._f.shakes)
		self.snakefall()

		if len(self._f.particles) > 0:
			self._f.draw_particles(self._d.screen, self._f.particles, 0.5)
		
		self._f.buttonhandler("backmenuingame", mouse_pos[0], mouse_pos[1], click[0], self._d.screen)
		self._f.buttonhandler("pauseingame", mouse_pos[0], mouse_pos[1], click[0], self._d.screen)
		self._f.texthandler("score", self._d.screen)
		self._f.texthandler("ingamehighscore", self._d.screen)
	

		if not self.runninggame:
			if self._d.score > int(self._d.highscore):
				self._d.highscore = self._d.score
				self._f.createtext("ingamehighscore", [0, -self._d.currentres[1]//2.5], int(self._d.currentres[1]*(20/1080)), "Highscore: "+str(self._d.highscore), (187, 187, 187))
				self._d.writesettings()

			#Print dead screen
			self._f.renderdeadscreen(mouse_pos, click)
			
	def move(self, direction):
		if direction == "up":
			if self.snake_posy[0] <= 0 and not self._d.bordercollisions:
				self.snake_posy.insert(0, 400//16 -1)
				self.snake_posx.insert(0, self.snake_posx[0])
			else:
				self.snake_posy.insert(0, self.snake_posy[0] -1)
				self.snake_posx.insert(0, self.snake_posx[0])
		elif direction == "down":
			if self.snake_posy[0] >= 400//16 -1 and not self._d.bordercollisions:
				self.snake_posy.insert(0, 0)
				self.snake_posx.insert(0, self.snake_posx[0])
			else:
				self.snake_posy.insert(0, self.snake_posy[0] +1)
				self.snake_posx.insert(0, self.snake_posx[0])
		elif direction == "left":
			if self.snake_posx[0] <= 0 and not self._d.bordercollisions:
				self.snake_posy.insert(0, self.snake_posy[0])
				self.snake_posx.insert(0, 400//16 -1)
			else:
				self.snake_posx.insert(0, self.snake_posx[0] -1)
				self.snake_posy.insert(0, self.snake_posy[0])
		elif direction == "right":
			if self.snake_posx[0] >= 400//16 -1 and not self._d.bordercollisions:
				self.snake_posy.insert(0, self.snake_posy[0])
				self.snake_posx.insert(0, 0)
			else:
				self.snake_posx.insert(0, self.snake_posx[0] +1)
				self.snake_posy.insert(0, self.snake_posy[0])
		if not self.eat:
			self.snake_posx.pop((len(self.snake_posx)-1))
			self.snake_posy.pop((len(self.snake_posy)-1))
		else:
			self.eat = False

	def spawnApple(self):
		randx = random.randint(0, 24)
		randy = random.randint(0, 24)

		while (randx in self.snake_posx and randy in self.snake_posy) or (randx in self.bomb_xgrid and randy in self.bomb_ygrid):
			randx = random.randint(0, 24)
			randy = random.randint(0, 24)

		self.apple_xgrid = randx
		self.apple_ygrid = randy
		self.apple_x = ((randx*self.GRIDSIZE) + (self._d.surfsize[0]/2) - (self.GRIDxy/2))
		self.apple_y = ((randy*self.GRIDSIZE) + (self._d.surfsize[1]/2) - (self.GRIDxy/2))

	def snakecollison(self):
		for i in range(len(self.snake_posx)):
			if i > 0 and self.snake_posx[0] == self.snake_posx[i] and self.snake_posy[0] == self.snake_posy[i]:
				if not self.bonk:
					if self._d.soundbool:
						self._s.bonksound.play()
					self._f.shakes.append([[0,0],[random.randint(-30, 30), random.randint(-30, 30)], 0.5, 10, 10])

				self.bonk = True

	def bordercollisions(self, posx, posy):
		if posx < 0 or posx > (self.GRIDxy / self.GRIDSIZE)-1:
			if not self.bonk:
				if self._d.soundbool:
					self._s.bonksound.play()
				self._f.shakes.append([[0,0],[random.randint(-30, 30), random.randint(-30, 30)], 0.5, 10, 10])

			self.bonk = True

		if posy < 0 or posy >= (self.GRIDxy / self.GRIDSIZE):
			if not self.bonk:
				if self._d.soundbool:
					self._s.bonksound.play()
				self._f.shakes.append([[0,0],[random.randint(-30, 30), random.randint(-30, 30)], 0.5, 10, 10])

			self.bonk = True

	def applecollision(self):
		if self.snake_posx[0] == self.apple_xgrid and self.snake_posy[0] == self.apple_ygrid:
			self.eat = True
			for i in range(20):
				self._f.particles.append([[self.apple_x *2 + (self.GRIDSIZE/2), self.apple_y *2 + (self.GRIDSIZE/2)], [random.randint(-10, 10)/10, random.randint(-10, 10)/10 ], random.randint(6, self.GRIDSIZE), (random.randint(117, 181), 0, 0)])
			self._f.shakes.append([[0,0],[random.randint(-5, 5), random.randint(-5, 5)], 1, 5, 5])
			if self._d.soundbool:
				self._s.eatsound.play()
			self._d.score += 1
			self.spawnApple()

	def snakefall(self):
		if self.bonk:
			if self.snakefall_time >= self.snakefall_time_max:
				self.snakefall_time = 0
				for i in range(len(self.snake_posy)):
					self.snake_posy[i] += 2
			self.snakefall_time += random.randint(1, self.snakefall_time_max)

	def spawnBomb(self):
		self.bombspawntimer += 1

		if self.bombspawntimer >= self.bombspawntimermax:
			self.bombspawntimer = 0
			randx = random.randint(0, 24)
			randy = random.randint(0, 24)

			while (randx in self.snake_posx and randy in self.snake_posy) or (randx in self.bomb_xgrid and randy in self.bomb_ygrid) or (randx == self.apple_xgrid and randy == self.apple_ygrid):
				randx = random.randint(0, 24)
				randy = random.randint(0, 24)

			self.bomb_xgrid.append(randx)
			self.bomb_ygrid.append(randy)
			self.bomb_x.append((randx*self.GRIDSIZE) + (self._d.surfsize[0]/2) - (self.GRIDxy/2))
			self.bomb_y.append((randy*self.GRIDSIZE) + (self._d.surfsize[1]/2) - (self.GRIDxy/2))

	def renderbomb(self): 
		if len(self.bomb_x) > 0:
			for i in range(len(self.bomb_x)):
				self._d.surf.blit(self._i.bomb,(self.bomb_x[i], self.bomb_y[i]))

	def bombcollision(self):
		if len(self.bomb_x) > 0:
			for i, v in sorted(enumerate(self.bomb_xgrid), reverse=True):
				if self.snake_posx[0] == self.bomb_xgrid[i] and self.snake_posy[0] == self.bomb_ygrid[i]:
					if self._d.soundbool:
						self._s.boomsound.play()
					self._f.shakes.append([[0,0], [random.randint(-25, 25), random.randint(-25, 25)], 0.2, 5, 5])
					for z in range(random.randint(20, 50)):
						self._f.particles.append([[self.bomb_x[i] *2, self.bomb_y[i] *2], [random.randint(-10, 10)/10, random.randint(-10, 10)/10], random.randint(10, self.GRIDSIZE+20), (255, random.randint(35, 255), 0)])
					self.bomb_xgrid.pop(i)
					self.bomb_ygrid.pop(i)
					self.bomb_x.pop(i)
					self.bomb_y.pop(i)
					if self._d.soundbool:
						self._s.eatsound.play()
					if self._d.bombkill:
						self.bonk = True
					if len(self.snake_posx) > 2 and not self._d.bombkill:
						rnd = random.randint(1, len(self.snake_posx)-2)
						self._d.score -= rnd
						if self._d.score < 0:
							self._d.score = 0
						for x in range(rnd):
							self.snake_posx.pop(-1)
							self.snake_posy.pop(-1)
					else:
						self._d.score = 0

	def renderSnake(self):
		for i in range(len(self.snake_posx)):
			self.snakex = ((self.snake_posx[i]*self.GRIDSIZE) + (self._d.surfsize[0]/2) - (self.GRIDxy/2))
			self.snakey = ((self.snake_posy[i]*self.GRIDSIZE) + (self._d.surfsize[1]/2) - (self.GRIDxy/2))
			if i == 0:
				#snakehead_rect = pygame.Rect(snakex, snakey, GRIDSIZE, GRIDSIZE)
				#pygame.draw.rect(display, (0,126,15), snakehead_rect)
				if not self.eat:
					if self.snake_direction == "up":
						self._d.surf.blit(self._i.snakehead, (self.snakex, self.snakey))
					elif self.snake_direction == "down":
						self._d.surf.blit(pygame.transform.rotate(self._i.snakehead, 180), (self.snakex, self.snakey))
					elif self.snake_direction == "left":
						self._d.surf.blit(pygame.transform.rotate(self._i.snakehead, 90), (self.snakex, self.snakey))
					elif self.snake_direction == "right":
						self._d.surf.blit(pygame.transform.rotate(self._i.snakehead, -90), (self.snakex, self.snakey))
				if self.eat:
					if self.snake_direction == "up":
						self._d.surf.blit(self._i.snakeheadeat, (self.snakex, self.snakey))
					elif self.snake_direction == "down":
						self._d.surf.blit(pygame.transform.rotate(self._i.snakeheadeat, 180), (self.snakex, self.snakey))
					elif  self.snake_direction == "left":
						self._d.surf.blit(pygame.transform.rotate(self._i.snakeheadeat, 90), (self.snakex, self.snakey))
					elif  self.snake_direction == "right":
						self._d.surf.blit(pygame.transform.rotate(self._i.snakeheadeat, -90), (self.snakex, self.snakey))

			elif i == len(self.snake_posx)-1:
				if self.snake_posx[i] < self.snake_posx[i-1]:
					self._d.surf.blit(pygame.transform.rotate(self._i.snakebodytail, -90), (self.snakex, self.snakey))
				elif self.snake_posx[i] > self.snake_posx[i-1]:
					self._d.surf.blit(pygame.transform.rotate(self._i.snakebodytail, 90), (self.snakex, self.snakey))
				elif self.snake_posy[i] < self.snake_posy[i-1]:
					self._d.surf.blit(pygame.transform.rotate(self._i.snakebodytail, 180), (self.snakex, self.snakey))
				elif self.snake_posy[i] > self.snake_posy[i-1]:
					self._d.surf.blit(self._i.snakebodytail, (self.snakex, self.snakey))
			else:
				#snake_rect = pygame.Rect(snakex, snakey, GRIDSIZE, GRIDSIZE)
				#pygame.draw.rect(display, (0,126,15), snake_rect)
				#KÖRPER
				if not self.eat:
					if self.snake_posx[i] < self.snake_posx[i-1]:
						if self.snake_posy[i] < self.snake_posy[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, True, False), (self.snakex, self.snakey))
						elif  self.snake_posy[i] > self.snake_posy[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, True, True), (self.snakex, self.snakey))
						else:
							self._d.surf.blit(pygame.transform.rotate(self._i.snakebody, -90), (self.snakex, self.snakey))
					elif self.snake_posx[i] > self.snake_posx[i-1]:
						if self.snake_posy[i] < self.snake_posy[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, False, False), (self.snakex, self.snakey))
						elif  self.snake_posy[i] > self.snake_posy[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, False, True), (self.snakex, self.snakey))
						else:
							self._d.surf.blit(pygame.transform.rotate(self._i.snakebody, 90), (self.snakex, self.snakey))
					elif self.snake_posy[i] < self.snake_posy[i-1]:
						if self.snake_posx[i] < self.snake_posx[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, True, False), (self.snakex, self.snakey))
						elif self.snake_posx[i] > self.snake_posx[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, False, False), (self.snakex, self.snakey))
						else:
							self._d.surf.blit(pygame.transform.rotate(self._i.snakebody, 180), (self.snakex, self.snakey))
					elif self.snake_posy[i] > self.snake_posy[i-1]:
						if self.snake_posx[i] < self.snake_posx[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, True, True), (self.snakex, self.snakey))
						elif  self.snake_posx[i] > self.snake_posx[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, False, True), (self.snakex, self.snakey))
						else: # normal
							self._d.surf.blit(self._i.snakebody, (self.snakex, self.snakey))
				if self.eat:
					if self.snake_posx[i] < self.snake_posx[i-1]:
						if self.snake_posy[i] < self.snake_posy[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, True, False), (self.snakex, self.snakey))
						elif  self.snake_posy[i] > self.snake_posy[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, True, True), (self.snakex, self.snakey))
						else:
							self._d.surf.blit(pygame.transform.rotate(self._i.snakebodyeat, -90), (self.snakex, self.snakey))
					elif self.snake_posx[i] > self.snake_posx[i-1]:
						if self.snake_posy[i] < self.snake_posy[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, False, False), (self.snakex, self.snakey))
						elif  self.snake_posy[i] > self.snake_posy[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, False, True), (self.snakex, self.snakey))
						else: #normal nach links
							self._d.surf.blit(pygame.transform.rotate(self._i.snakebodyeat, 90), (self.snakex, self.snakey))
					elif self.snake_posy[i] < self.snake_posy[i-1]:
						if self.snake_posx[i] < self.snake_posx[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, True, False), (self.snakex, self.snakey))
						elif  self.snake_posx[i] > self.snake_posx[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, False, False), (self.snakex, self.snakey))
						else:
							self._d.surf.blit(pygame.transform.rotate(self._i.snakebodyeat, 180), (self.snakex, self.snakey))
					elif self.snake_posy[i] > self.snake_posy[i-1]:
						if self.snake_posx[i] < self.snake_posx[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, True, True), (self.snakex, self.snakey))
						elif  self.snake_posx[i] > self.snake_posx[i+1]:
							self._d.surf.blit(pygame.transform.flip(self._i.snakebodyturn, False, True), (self.snakex, self.snakey))
						else:
							self._d.surf.blit(self._i.snakebodyeat, (self.snakex, self.snakey))