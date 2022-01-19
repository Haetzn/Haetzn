import pygame, sys, random

class Funks:
	def __init__(self, data, img, sound):
		self._d = data
		self._i = img
		self._s = sound

		#ELEMENTE DICTs:
		self.buttons = {}
		self.imgbuttons = {}
		self.anzeigen = {}
		self.texts = {}
		self.sliders = {}
		self.switches = {}
		self.particles = []
		self.shakes = []

		self.initload()

	def initload(self):
		#Menu elemente
		self.buttonsizeX = self._d.currentres[0]//5
		self.buttonsizeY = self._d.currentres[1]//15

		#Pause buttonsize
		self.buttonsizeX_pause = self._d.currentres[0]//4
		self.buttonsizeY_pause = self._d.currentres[1]//15

		#MAIN MENU
		self.createbtn("play", [(self._d.currentres[0]//2) - (self.buttonsizeX//2), (self._d.currentres[1]//2) - (self.buttonsizeY//2)], [self.buttonsizeX, self.buttonsizeY], "PLAY", (187, 187, 187), (31, 31, 31), (31, 31, 31), (187, 187, 187), self.toggleingame)
		self.createbtn("settings", [(self._d.currentres[0]//2) - (self.buttonsizeX//2), (self._d.currentres[1]//2) - (self.buttonsizeY//2) + (self._d.currentres[1]//10)], [self.buttonsizeX, self.buttonsizeY], "SETTINGS", (187, 187, 187), (31, 31, 31), (31, 31, 31), (187, 187, 187), self.togglesettings)
		self.createbtn("quit", [(self._d.currentres[0]//2) - (self.buttonsizeX//2), (self._d.currentres[1]//2) - (self.buttonsizeY//2) + (self._d.currentres[1]//5)], [self.buttonsizeX, self.buttonsizeY], "QUIT", (187, 187, 187), (31, 31, 31), (31, 31, 31), (187, 187, 187), self.toggleexitscreen)
		self.createtext("snake", [0, -int(self._d.currentres[1]*(200/1080))], int(self._d.currentres[1]*(180/1080)), "Snake", (187, 187, 187))
		self.createtext("hatzi", [int(self._d.currentres[0]//2.2), int(self._d.currentres[1]//2.1)], int(self._d.currentres[1]*(40/1080)), "by Hatzi", (236, 123, 16))
		

		#EXITSCREEN
		self.createbtn("resume_surequit", [(self._d.currentres[0]/2) - (self.buttonsizeX_pause/2), (self._d.currentres[1]/2) - (self.buttonsizeY_pause/2)], [self.buttonsizeX_pause, self.buttonsizeY_pause], "RESUME", (187, 187, 187), (31, 31, 31), (31, 31, 31), (187, 187, 187), self.toggleexitscreen)
		self.createbtn("backtomenue_surequit", [(self._d.currentres[0]/2) - (self.buttonsizeX_pause/2), (self._d.currentres[1]/2) - (self.buttonsizeY_pause/2) + (self._d.currentres[1]/10)], [self.buttonsizeX_pause, self.buttonsizeY_pause], "LEAVE", (187, 187, 187), (31, 31, 31), (31, 31, 31), (187, 187, 187), self.exitgame)
		self.createtext("suretoquit_text", [0, -int(self._d.currentres[0]//24 //0.8)], self._d.currentres[0]//24, "Sure to Quit?", (187, 187, 187))
		self.suretoquitdarker = pygame.Surface((self._d.currentres[0], self._d.currentres[1]), pygame.SRCALPHA)
		self.suretoquitdarker.fill((0, 0, 0, 200))
		self.suretoquitbackgroundrect = pygame.Rect(self._d.currentres[0]//2 - self.buttonsizeX_pause//2 - int(self._d.currentres[0]//38.4), self._d.currentres[1]//2 - self.buttonsizeY_pause//2 - self._d.currentres[1]//9, self.buttonsizeX_pause + int(self._d.currentres[0] // 19.2), 2*self.buttonsizeY_pause + int(self._d.currentres[1]//5.4))
		self.suretoquitclicktimer = 10

		#INGAME
		self.createbtn("backmenuingame", [int(self._d.currentres[0]*(20/1920)), int(self._d.currentres[1]*(20/1080))], [self.buttonsizeX//2, self.buttonsizeY//2], "To Menu", (187, 187, 187), (31, 31, 31), (31, 31, 31), (187, 187, 187), self.toggleingame)
		self.createbtn("pauseingame", [int(self._d.currentres[0]*(20/1920)), int(self._d.currentres[1]*(80/1080))], [self.buttonsizeX//2, self.buttonsizeY//2], "PAUSE", (187, 187, 187), (31, 31, 31), (31, 31, 31), (187, 187, 187), self.togglepause)
		self.createtext("score", [0, -self._d.currentres[1]//2.2], int(self._d.currentres[1]*(100/1080)), str(self._d.score), (187, 187, 187))
		self.createtext("ingamehighscore", [0, -self._d.currentres[1]//2.5], int(self._d.currentres[1]*(20/1080)), "Highscore: "+str(self._d.highscore), (187, 187, 187))
		
		#Settings
		self.createtext("settings", [0, -int(self._d.currentres[1]*(300/1080))], int(self._d.currentres[1]*(180/1080)), "Settings", (187, 187, 187))
		self.createbtn("back_settings", [0, ((self._d.currentres[1]//1.1) - (self.buttonsizeY/2))], [self.buttonsizeX//1.5, self.buttonsizeY], "BACK", (187, 187, 187), (31, 31, 31), (31, 31, 31), (187, 187, 187), self.togglesettings)
		self.createbtn("3072x1920_settings", [self._d.currentres[0]//2-self.buttonsizeX//2, self._d.currentres[1]//3], [self.buttonsizeX, self.buttonsizeY], "3072x1920", (187, 187, 187), (31, 31, 31), (31, 31, 31), (187, 187, 187), self.setresolution, 0)
		self.createbtn("1920x1080_settings", [self._d.currentres[0]//2-self.buttonsizeX//2, self._d.currentres[1]//3 + (self._d.currentres[1]//10)], [self.buttonsizeX, self.buttonsizeY], "1920x1080", (187, 187, 187), (31, 31, 31), (31, 31, 31), (187, 187, 187), self.setresolution, 1)
		self.createbtn("960x540_settings", [self._d.currentres[0]//2-self.buttonsizeX//2, self._d.currentres[1]//3 + 2*(self._d.currentres[1]//10)], [self.buttonsizeX, self.buttonsizeY], "960x540", (187, 187, 187), (31, 31, 31), (31, 31, 31), (187, 187, 187), self.setresolution, 2)
		
		self.scrollrect_settings = pygame.Rect(self._d.currentres[0]//2+self.buttonsizeX//2 + (self._d.currentres[1]//10), self._d.currentres[1]//3, self._d.currentres[1]//128, int(self._d.currentres[1]//13.5))
		self.allowscroll = False
		self.settingstextoffsety = self.buttons["1920x1080_settings"][0][1] - self.buttons["1920x1080_settings"][1][2].y

		self.createslider("x", [self._d.currentres[0]//2-self.buttonsizeX//2, self._d.currentres[1]//3 + 2*(self._d.currentres[1]//10)], [self.buttonsizeX, self.buttonsizeY//4], self.buttonsizeY//2, (255, 255, 255), (0, 255, 0), (0, 140, 0))
		self.setsliderwert("x", 100)
		

		#dead screen
		self.deaddarker = pygame.Surface(self._d.currentres, pygame.SRCALPHA)
		self.deaddarker.fill((0, 0, 0, 200))
		self.deadbox = pygame.Rect(self._d.currentres[0]//2 - self.buttonsizeX_pause//2 - int(self._d.currentres[0]//38.4), self._d.currentres[1]//2 - self.buttonsizeY_pause//2 - self._d.currentres[1]//9, self.buttonsizeX_pause + int(self._d.currentres[0] // 19.2), 4*self.buttonsizeY_pause + int(self._d.currentres[1]//5.4))
		self.createtext("retrytext_dead", [0, -int(self._d.currentres[0]//24 //0.8)], self._d.currentres[0]//24, "Retry?", (187, 187, 187))
		self.createbtn("retry_dead", [(self._d.currentres[0]/2) - (self.buttonsizeX_pause/2), (self._d.currentres[1]/2) - (self.buttonsizeY_pause/2)], [self.buttonsizeX_pause, self.buttonsizeY_pause], "RETRY", (187, 187, 187), (31, 31, 31), (31, 31, 31), (187, 187, 187), self.truereloadgame)
		self.createbtn("tomenu_dead", [(self._d.currentres[0]/2) - (self.buttonsizeX_pause/2), (self._d.currentres[1]/2) - (self.buttonsizeY_pause/2) + (self._d.currentres[1]/10)], [self.buttonsizeX_pause, self.buttonsizeY_pause], "TO MENU", (187, 187, 187), (31, 31, 31), (31, 31, 31), (187, 187, 187), self.toggleingame)
		
		self.createswitch("bordercol", [self._d.currentres[0]//2, (self._d.currentres[1]/2) - (self.buttonsizeY_pause) + (self._d.currentres[1]/5)], "Bordercollision", (187, 187, 187), int(self._d.currentres[1]*(86/1080)),"./data/imgs/switch_on.png", "./data/imgs/switch_off.png", self.togglebordercol,self._d.bordercollisions)
		self.createswitch("bombkill", [self._d.currentres[0]//2, (self._d.currentres[1]/2) + (self._d.currentres[1]/5)], "Bombkill", (187, 187, 187), int(self._d.currentres[1]*(86/1080)),"./data/imgs/switch_on.png", "./data/imgs/switch_off.png", self.togglebombkill,self._d.bombkill)
		
		self.deadclicktimer = 10

	#################################################################################################################################################################
	#################################################################################################################################################################
	###########################################FUNKTIONEN############################################################################################################
	#################################################################################################################################################################
	#################################################################################################################################################################

	#Normale Buttons
	def createbtn(self, name, pos, size, text, colorbtn, colorbtnpressed, colortext, colortextpressed, funktionname, funktionübergame = ""): 
		rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
		font = pygame.font.Font("data/fonts/Montserrat-Bold.ttf", size[1])

		textobj = font.render(text, 1, colortext)
		textobj1 = font.render(text, 1, colortextpressed)
		textrect = textobj.get_rect(center=(pos[0] + size[0]/2, pos[1] + size[1]/2))
		i = 1
		while textrect.width > size[0]:
			i += 1
			font = pygame.font.Font("data/fonts/Montserrat-Bold.ttf", size[1]-i)
			textobj = font.render(text, 1, colortext)
			textobj1 = font.render(text, 1, colortextpressed)
			textrect = textobj.get_rect(center=(pos[0] + size[0]/2, pos[1] + size[1]/2))

		self.buttons[name] = [rect, [textobj, textobj1, textrect], False, colorbtn, colorbtnpressed, colortext, colortextpressed, funktionname, 0, funktionübergame] #btn rect, text zeug, hover, colorbtn, color2btn, colortext, color2text, funktion -> machblabla(), sound timer
		
	
	def buttonhandler(self, name, mx, my, click, screen): 
		if self.buttons[name][0].collidepoint((mx, my)):
			pygame.draw.rect(screen, self.buttons[name][4], self.buttons[name][0])
			screen.blit(self.buttons[name][1][1], self.buttons[name][1][2])
			if not self.buttons[name][2]:
				if self.buttons[name][8] == 30:
					self.buttons[name][8] = 0
				if self.buttons[name][8] == 0:
					if self._d.soundbool:
						self._s.hoversound.play()
				self.buttons[name][2] = True
				self.buttons[name][8] += 1
			if click:
				if self._d.soundbool:
					self._s.clicksound.play()
				if self.buttons[name][9] == "":
					self.buttons[name][7]()
				else: 
					self.buttons[name][7](self.buttons[name][9])
		else:
			self.buttons[name][2] = False
			self.buttons[name][8] = 0
			pygame.draw.rect(screen, self.buttons[name][3], self.buttons[name][0])
			screen.blit(self.buttons[name][1][0], self.buttons[name][1][2])

	def checkallowrender(self, name, posxmin, posxmax, posymin, posymax, checkX, checkY, mx, my, click, screen):
		if checkX and checkY:
			if self.buttons[name][0].x >= posxmin and self.buttons[name][0].x <= posxmax and self.buttons[name][0].y >= posymin and self.buttons[name][0].y <= posymax:
				self.buttonhandler(name, mx, my, click, screen)
				pass
		elif checkX and not checkY:
			if self.buttons[name][0].x >= posxmin and self.buttons[name][0].x <= posxmax:
				self.buttonhandler(name, mx, my, click, screen)
				pass
		else:
			if self.buttons[name][0].y >= posymin and self.buttons[name][0].y <= posymax:
				self.buttonhandler(name, mx, my, click, screen)
				pass

	def checksliderallowrender(self, name, posxmin, posxmax, posymin, posymax, checkX, checkY, mouse, clickhold, screen):
		if checkX and checkY:
			if self.sliders[name][1][0].x >= posxmin and self.sliders[name][1][0].x <= posxmax and self.sliders[name][1][0].y >= posymin and self.sliders[name][1][0].y <= posymax:
				self.sliderhandler(name, screen, clickhold, mouse)
				pass
		elif checkX and not checkY:
			if self.sliders[name][1][0].x >= posxmin and self.sliders[name][1][0].x <= posxmax:
				self.sliderhandler(name, screen, clickhold, mouse)
				pass
		else:
			if self.sliders[name][1][0].y >= posymin and self.sliders[name][1][0].y <= posymax:
				self.sliderhandler(name, screen, clickhold, mouse)
				pass
		

	def recentertext(self, name):
		self.buttons[name][1][2] = self.buttons[name][1][0].get_rect(center=(self.buttons[name][0].x + self.buttons[name][0].width/2, self.buttons[name][0].y + self.buttons[name][0].height/2))

	def changetext(self, name, text):
		font = pygame.font.Font("data/fonts/Montserrat-Bold.ttf", self.buttons[name][0].height)

		textobj = font.render(text, 1, self.buttons[name][5])
		textobj1 = font.render(text, 1, self.buttons[name][6])
		textrect = textobj.get_rect(center=(self.buttons[name][0].x + self.buttons[name][0].width/2, self.buttons[name][0].y + self.buttons[name][0].height/2))
		i = 1
		while textrect.width > self.buttons[name][0].width:
			i += 1
			font = pygame.font.Font("data/fonts/Montserrat-Bold.ttf", self.buttons[name][0].height-i)
			textobj = font.render(text, 1, self.buttons[name][5])
			textobj1 = font.render(text, 1, self.buttons[name][6])
			textrect = textobj.get_rect(center=(self.buttons[name][0].x + self.buttons[name][0].width/2, self.buttons[name][0].y + self.buttons[name][0].height/2))

		self.buttons[name][1][0] = textobj
		self.buttons[name][1][1] = textobj1
		self.buttons[name][1][2] = textrect 

	#Img buttons
	def createimgbtn(self, name, pos, img, imgpressed, scale, funktionname): 
		self.imgbuttons[name] = [pos, [img, imgpressed], scale, 0, False, funktionname] #pos, image, scale, sound timer, hover, funktion
	
	def flipimgbuttonimg(self, name):
		img = self.imgbuttons[name][1][0]
		img2 = self.imgbuttons[name][1][1]

		self.imgbuttons[name][1][0] = img2
		self.imgbuttons[name][1][1] = img

	def changeimgbuttonimg(self, name, img1, img2):
		self.imgbuttons[name][1][0] = img1
		self.imgbuttons[name][1][1] = img2
	
	def imgbuttonhandler(self, name, mx, my, click, screen, colorkey = (255, 255, 255)): 
		img = self.imgbuttons[name][1][0]
		img2 = self.imgbuttons[name][1][1]
		img.set_colorkey(colorkey)
		img2.set_colorkey(colorkey)
		if self.imgbuttons[name][2] != [0, 0]:
			img = pygame.transform.scale(img, self.imgbuttons[name][2])
			img2 = pygame.transform.scale(img2, self.imgbuttons[name][2])
		img = img.convert_alpha()
		img2 = img2.convert_alpha()
		rect = img.get_rect()
		rect.x = self.imgbuttons[name][0][0]
		rect.y = self.imgbuttons[name][0][1]
		if rect.collidepoint((mx, my)):
			screen.blit(img2, self.imgbuttons[name][0])
			if not self.imgbuttons[name][4]:
				if self.imgbuttons[name][3] == 30:
					self.imgbuttons[name][3] = 0
				if self.imgbuttons[name][3] == 0:
					if self._d.soundbool:
						self._s.hoversound.play()
				self.imgbuttons[name][4] = True
				self.imgbuttons[name][3] += 1
			if click:
				if self._d.soundbool:
					self._s.clicksound.play()
				self.imgbuttons[name][5]()
		else:
			self.imgbuttons[name][4] = False
			self.imgbuttons[name][3] = 0
			screen.blit(img, self.imgbuttons[name][0])

	
	def createanzeige(self, name, pos, img, scale, wert, textcolor, colorkey = (255, 255, 255)):
		if scale != [0, 0]:
			img = pygame.transform.scale(img, scale)
		img.set_colorkey(colorkey)
		img = img.convert_alpha()
		font = pygame.font.Font("data/fonts/Montserrat-Bold.ttf", int(img.get_rect().height //1.2))
		textobj = font.render(str(wert), 1, textcolor)
		textrect = textobj.get_rect(center = (pos[0], pos[1] + img.get_rect().height //2))
		textrect.right = pos[0]
		wert_before = wert
		self.anzeigen[name] = [pos, img, [wert, textobj, textrect, textcolor], wert_before]

	def anzeigenhandler(self, name, screen, wert):
		self.anzeigen[name][2][0] = wert
		if self.anzeigen[name][3] != self.anzeigen[name][2][0]:
			self.anzeigen[name][3] = self.anzeigen[name][2][0]
			self.changeanzeige(name, self.anzeigen[name][2][0])

		screen.blit(self.anzeigen[name][2][1], self.anzeigen[name][2][2])
		screen.blit(self.anzeigen[name][1], [self.anzeigen[name][0][0], self.anzeigen[name][0][1]])

	def changeanzeige(self, name, changewert):
		font = pygame.font.Font("data/fonts/Montserrat-Bold.ttf", int(self.anzeigen[name][1].get_rect().height //1.2))
		self.anzeigen[name][2][1] = font.render(str(self.anzeigen[name][2][0]), 1, self.anzeigen[name][2][3])
		
		self.anzeigen[name][2][2] = self.anzeigen[name][2][1].get_rect(center = (self.anzeigen[name][0][0], self.anzeigen[name][0][1] + self.anzeigen[name][1].get_rect().height //2))
		self.anzeigen[name][2][2].right = self.anzeigen[name][0][0]

	#TEXT FUNKTION (TEXT ALLWAYS CENTER ON SCREEN, MOVE WITH OFFSET)
	def createtext(self, name, offset, size, text, textcolor):
		font = pygame.font.Font("data/fonts/Montserrat-Bold.ttf", size)
		textobj = font.render(text, 1, textcolor)
		textrect = textobj.get_rect(center = (self._d.currentres[0]//2 + offset[0], self._d.currentres[1]//2 + offset[1]))
		self.texts[name] = [textobj, textrect]

	def texthandler(self, name, screen):
		screen.blit(self.texts[name][0], self.texts[name][1])

	def createslider(self, name, pos, barsize, radius, colorbar, colorslider, colorsliderpress):
		bar_rect = pygame.Rect(pos[0], pos[1], barsize[0], barsize[1])
		slider_circlerect = pygame.Rect(pos[0], pos[1] - radius//4, radius, radius)
		self.sliders[name] = [pos, [bar_rect, slider_circlerect], colorbar, colorslider, colorsliderpress, 0, False]

	def sliderhandler(self, name, screen, clickhold, mouse):
		pygame.draw.rect(screen, self.sliders[name][2], self.sliders[name][1][0])
		
		if clickhold[0]:
			if self.sliders[name][1][0].collidepoint(mouse):
				self.sliders[name][1][1].x = mouse[0] - self.sliders[name][1][1].width//2 + 2
				self.sliders[name][6] = True
			elif self.sliders[name][1][1].collidepoint(mouse):
				self.sliders[name][6] = True
			else:
				self.sliders[name][6] = False
		else:
			self.sliders[name][6] = False

		if self.sliders[name][6]:
			self.sliders[name][1][1].x = mouse[0] - self.sliders[name][1][1].width//2 + 2
			if self.sliders[name][1][1].x < self.sliders[name][1][0].x - self.sliders[name][1][1].width//2:
				self.sliders[name][1][1].x = self.sliders[name][1][0].x - self.sliders[name][1][1].width//2
			elif self.sliders[name][1][1].x > self.sliders[name][1][0].x + self.sliders[name][1][0].width - self.sliders[name][1][1].width//2:
				self.sliders[name][1][1].x = self.sliders[name][1][0].x + self.sliders[name][1][0].width - self.sliders[name][1][1].width//2

			pygame.draw.circle(screen, self.sliders[name][4], [self.sliders[name][1][1].x + self.sliders[name][1][1].width//2, self.sliders[name][1][0].y + self.sliders[name][1][1].height//4], self.sliders[name][1][1].width//2)
		else:
			if self.sliders[name][1][1].x < self.sliders[name][1][0].x - self.sliders[name][1][1].width//2:
				self.sliders[name][1][1].x = self.sliders[name][1][0].x - self.sliders[name][1][1].width//2
			elif self.sliders[name][1][1].x > self.sliders[name][1][0].x + self.sliders[name][1][0].width - self.sliders[name][1][1].width//2:
				self.sliders[name][1][1].x = self.sliders[name][1][0].x + self.sliders[name][1][0].width - self.sliders[name][1][1].width//2
			pygame.draw.circle(screen, self.sliders[name][3], [self.sliders[name][1][1].x + self.sliders[name][1][1].width//2, self.sliders[name][1][0].y + self.sliders[name][1][1].height//4], self.sliders[name][1][1].width//2)
			
	def setsliderwert(self, name, wert):
		self.sliders[name][5] = wert
		self.sliders[name][1][1].x = (wert*self.sliders[name][1][0].width - wert*self.sliders[name][1][1].width)*100 - self.sliders[name][1][1].width//4 + self.sliders[name][1][0].x

	def getsliderwert(self, name):
		return self.sliders[name][5]

	def draw_screenshake(self, screen, surf, shakes):
		 #[[locx, locy], [ax, ay], timetick, time, starttime]
		if len(self.shakes) > 0:
			for i, shake in sorted(enumerate(self.shakes), reverse=True):
				if random.randint(0,1) == 0:
					shake[0][0] += (shake[1][0]/random.randint(1,2))
					shake[0][1] += (shake[1][1]/random.randint(1,2))
				else:
					shake[0][0] -= (shake[1][0]/random.randint(1,2))
					shake[0][1] -= (shake[1][1]/random.randint(1,2))

				shake[3] -= shake[2]
				screen.blit(surf, (shake[0][0], shake[0][1]))
				if shake[3] < 0:
					self.shakes.pop(i)
		else:
			screen.blit(surf, (0, 0))
		


	def draw_particles(self, screen, particles, timetick):
		#[[locx, locy], [ax, ay], t]
		for i, particle in sorted(enumerate(self.particles), reverse=True):
			particle[0][0] += particle[1][0]
			particle[0][1] += particle[1][1]
			particle[2] -= timetick
			pygame.draw.circle(screen, particle[3], particle[0], particle[2])
			if particle[2] <= 0:
				self.particles.pop(i)


	def schachmuster(self, GRIDxy, GRIDSIZE, color1, color2): # (187,187,187) (31, 31, 31)
		board = pygame.Surface((GRIDxy, GRIDxy))
		board.fill(color1)
		for x in range(0, int(GRIDxy/GRIDSIZE), 2):
			for y in range(0, int(GRIDxy/GRIDSIZE), 2):
				pygame.draw.rect(board, color2, (x*GRIDSIZE, y*GRIDSIZE, GRIDSIZE, GRIDSIZE))
		for i in range(1, int(GRIDxy/GRIDSIZE), 2):
			for j in range(1, int(GRIDxy/GRIDSIZE), 2):
				pygame.draw.rect(board, color2, (i*GRIDSIZE, j*GRIDSIZE, GRIDSIZE, GRIDSIZE))
		return board

	def createswitch(self, name, pos, text, textcolor, size, img1, img2, func, state):
		on_img = pygame.image.load(img1).convert()
		on_img = pygame.transform.scale(on_img, (size, size))
		on_img.set_colorkey((255, 255, 255))
		off_img = pygame.image.load(img2).convert()
		off_img = pygame.transform.scale(off_img, (size, size))
		off_img.set_colorkey((255, 255, 255))
		font = pygame.font.Font("data/fonts/Montserrat-Bold.ttf", int(on_img.get_rect().height //2))
		textobj = font.render(text, 1, textcolor)
		textrect = textobj.get_rect(center = (pos[0] - size//2, pos[1] + on_img.get_rect().height //2))
		switchpos = (pos[0] + textrect.width//2 - size//2, pos[1])
		swtichrect = pygame.Rect(pos[0] + textrect.width//2 - size//2, switchpos[1], size, size)
		self.switches[name] = [pos, textobj, textrect, on_img, off_img, switchpos, swtichrect, func, state]


	def switchcheckallowrender(self, name, posxmin, posxmax, posymin, posymax, checkX, checkY, mouse_pos, click, screen):
		if checkX and checkY:
			if self.switches[name][0][0] >= posxmin and self.switches[name][0][0] <= posxmax and self.switches[name][0][1] >= posymin and self.switches[name][0][1]<= posymax:
				self.switchhandler(name, mouse_pos, click, screen)
				pass
		elif checkX and not checkY:
			if self.switches[name][0][0] >= posxmin and self.switches[name][0][0] <= posxmax:
				self.switchhandler(name, mouse_pos, click, screen)
				pass
		else:
			if self.switches[name][0][1] >= posymin and self.switches[name][0][1] <= posymax:
				self.switchhandler(name, mouse_pos, click, screen)
				pass

	def switchhandler(self, name, mouse_pos, click, screen):
		if self.switches[name][6].collidepoint(mouse_pos):
			if click:
				if self._d.soundbool:
					self._s.clicksound.play()
				if self.switches[name][7] == None:
					self.flipswitchstate(name)
				else:
					self.switches[name][7]()
					self.flipswitchstate(name)
					

		if self.switches[name][-1]:
			screen.blit(self.switches[name][3], self.switches[name][5])
			screen.blit(self.switches[name][1], self.switches[name][2])
		else:
			screen.blit(self.switches[name][4], self.switches[name][5])
			screen.blit(self.switches[name][1], self.switches[name][2])

	def flipswitchstate(self, name):
		self.switches[name][-1] = not self.switches[name][-1]
	#################################################################################################################################################################
	#################################################################################################################################################################
	###########################################DEFS############################################################################################################
	#################################################################################################################################################################
	#################################################################################################################################################################

	def nodef(self):
		pass

	def exitgame(self):
		pygame.quit()
		sys.exit()

	def toggleexitscreen(self):
		self.suretoquitclicktimer = 10
		self._d.exitscreen = not self._d.exitscreen

	def togglebordercol(self):
		self._d.bordercollisions = not self._d.bordercollisions
		self._d.writesettings()

	def togglebombkill(self):
		self._d.bombkill = not self._d.bombkill
		self._d.writesettings()

	def togglesettings(self):
		self._d.settings = not self._d.settings
		#self._d.soundvol = self.sliders
		self._d.writesettings()

	def toggleingame(self):
		self.truereloadgame()
		self._d.ingame = not self._d.ingame

	def togglepause(self):
		self._d.pausescreen = not self._d.pausescreen

	def truereloadgame(self):
		self._d.reloadgame = True

	def togglemusic(self):
		self._d.musicbool = not self._d.musicbool

	def togglesound(self):
		self._d.soundbool = not self._d.soundbool

	def setresolution(self, x):
		self._d.currentres = self._d.possibleresolutions[x]
		if self._d.fullscreen:
			self._d.screen = pygame.display.set_mode(self._d.currentres, pygame.FULLSCREEN)
		else:
			self._d.screen = pygame.display.set_mode(self._d.currentres, pygame.RESIZABLE)
		self._d.writesettings()
		self._d.loadsettings(self._d.Fullscreenwidth, self._d.Fullscreenheight)
		self.initload()
		self._i.loadimgs()
		self._d.reloadgame = True

	def togglefullscreen(self):
		self._d.fullscreen = not self._d.fullscreen
		if self._d.fullscreen:
			self._d.screen = pygame.display.set_mode(self._d.currentres, pygame.FULLSCREEN)
		else:
			self._d.screen = pygame.display.set_mode(self._d.currentres, pygame.RESIZABLE)
		self._d.writesettings()
		self._d.loadsettings(self._d.Fullscreenwidth, self._d.Fullscreenheight)
		self.initload()
		self._i.loadimgs()
		self._d.reloadgame = True

	#################################################################################################################################################################
	#################################################################################################################################################################
	###########################################FUNKTIONEN############################################################################################################
	#################################################################################################################################################################
	#################################################################################################################################################################


	def menu(self, mouse_pos, click):
		self._d.screen.fill((31, 31, 31))
		self.texthandler("snake", self._d.screen)
		#self.texthandler("hatzi", self._d.screen)
		self.buttonhandler("play", mouse_pos[0], mouse_pos[1], click[0], self._d.screen)
		self.buttonhandler("settings", mouse_pos[0], mouse_pos[1], click[0], self._d.screen)
		self.buttonhandler("quit", mouse_pos[0], mouse_pos[1], click[0], self._d.screen)
		

	def renderexitscreen(self, mouse_pos, click):
		self._d.screen.blit(self.suretoquitdarker, (0, 0))
		pygame.draw.rect(self._d.screen, (31, 31, 31), self.suretoquitbackgroundrect)
		self.buttonhandler("resume_surequit", mouse_pos[0], mouse_pos[1], click[0], self._d.screen)
		self.buttonhandler("backtomenue_surequit", mouse_pos[0], mouse_pos[1], click[0], self._d.screen)
		self.texthandler("suretoquit_text", self._d.screen)
		self.suretoquitclicktimer -= 1
		if click[0]:
			if not self.suretoquitbackgroundrect.collidepoint(mouse_pos):
				if self.suretoquitclicktimer <= 0:
					self.suretoquitclicktimer = 10
					self.toggleexitscreen()

	def renderdeadscreen(self, mouse_pos, click):
		self._d.screen.blit(self.deaddarker, (0, 0))
		pygame.draw.rect(self._d.screen, (31, 31, 31), self.deadbox)
		self.buttonhandler("retry_dead", mouse_pos[0], mouse_pos[1], click[0], self._d.screen)
		self.buttonhandler("tomenu_dead", mouse_pos[0], mouse_pos[1], click[0], self._d.screen)
		self.texthandler("retrytext_dead", self._d.screen)
		self.switchhandler("bordercol", mouse_pos, click[0], self._d.screen)
		self.switchhandler("bombkill", mouse_pos, click[0], self._d.screen)
		self.suretoquitclicktimer -= 1
		if click[0]:
			if not self.suretoquitbackgroundrect.collidepoint(mouse_pos):
				if self.deadclicktimer <= 0:
					self.deadclicktimer = 10
					self.truereloadgame()



	def rendersettings(self, mouse_pos, click, clickhold, mousewheel):
		self._d.screen.fill((31, 31, 31))

		if clickhold[0]:
			if self.scrollrect_settings.collidepoint(mouse_pos):
				self.allowscroll = True
		else:
			self.allowscroll = False

		if self.allowscroll:
			self.scrollrect_settings.y = mouse_pos[1] - self.scrollrect_settings.height//2
			if self.scrollrect_settings.y < self._d.currentres[1]//3:
				self.scrollrect_settings.y = self._d.currentres[1]//3
			elif self.scrollrect_settings.y > self._d.currentres[1] - 2* self.scrollrect_settings.height:
				self.scrollrect_settings.y = self._d.currentres[1] - 2* self.scrollrect_settings.height

			pygame.draw.rect(self._d.screen, (140, 140, 140), self.scrollrect_settings)
		else:
			pygame.draw.rect(self._d.screen, (240, 240, 240), self.scrollrect_settings)

		if mousewheel[1] != 0:
			self.scrollrect_settings.y -= mousewheel[1]*60
			mousewheel[1] = 0
			if self.scrollrect_settings.y <  self._d.currentres[1]//3:
				self.scrollrect_settings.y =  self._d.currentres[1]//3
			elif self.scrollrect_settings.y >  self._d.currentres[1] - 2* self.scrollrect_settings.height:
				self.scrollrect_settings.y =  self._d.currentres[1] - 2* self.scrollrect_settings.height


		#textobj.get_rect(center=(pos[0] + size[0]/2, pos[1] + size[1]/2))
		#[rect, [textobj, textobj1, textrect], False, colorbtn, colorbtnpressed, colortext, colortextpressed, funktionname, 0, funktionübergame]
		
		offsety =  self.scrollrect_settings.y - self._d.currentres[1]//3 #allg offset bei scroll

		self.buttons["3072x1920_settings"][0][1] = self._d.currentres[1]//3 - offsety
		self.recentertext("3072x1920_settings")

		self.buttons["1920x1080_settings"][0][1] =  self._d.currentres[1]//3 + self._d.currentres[1]//10 - offsety
		self.recentertext("1920x1080_settings")
		
		self.buttons["960x540_settings"][0][1] =  self._d.currentres[1]//3 + 2*self._d.currentres[1]//10 - offsety
		self.recentertext("960x540_settings")

		self.createswitch("fullscreen_settings", [self._d.currentres[0]//2, self._d.currentres[1]//3 + 3* self._d.currentres[1]//10 - offsety], "Fullscreen", (187, 187, 187), int(self._d.currentres[1]*(86/1080)), "./data/imgs/switch_on.png", "./data/imgs/switch_off.png", self.togglefullscreen, self._d.fullscreen)
		
		self.createswitch("musicon_settings", [self._d.currentres[0]//2, self._d.currentres[1]//3 + 4* self._d.currentres[1]//10 - offsety], "Music", (187, 187, 187), int(self._d.currentres[1]*(86/1080)), "./data/imgs/switch_on.png", "./data/imgs/switch_off.png", self.togglemusic, self._d.musicbool)

		self.createswitch("soundon_settings" ,[self._d.currentres[0]//2, self._d.currentres[1]//3 + 5* self._d.currentres[1]//10 - offsety], "Sound", (187, 187, 187), int(self._d.currentres[1]*(86/1080)), "./data/imgs/switch_on.png", "./data/imgs/switch_off.png", self.togglesound, self._d.soundbool)
		
		self.sliders["x"][1][0].y =  self._d.currentres[1]//3 + 6* self._d.currentres[1]//10 - offsety
		


		#checkallowrender(self, name, posxmin, posxmax, posymin, posymax, checkX, checkY, mx, my, click, screen)
		self.buttonhandler("back_settings", mouse_pos[0], mouse_pos[1], click[0], self._d.screen)
		self.checkallowrender("3072x1920_settings", 0, 0,  self._d.currentres[1]//3,  self._d.currentres[1]//0.8, False, True, mouse_pos[0], mouse_pos[1], click[0], self._d.screen)
		self.checkallowrender("1920x1080_settings", 0, 0,  self._d.currentres[1]//3,  self._d.currentres[1]//0.8, False, True, mouse_pos[0], mouse_pos[1], click[0], self._d.screen)
		self.checkallowrender("960x540_settings", 0, 0,  self._d.currentres[1]//3,  self._d.currentres[1]//0.8, False, True, mouse_pos[0], mouse_pos[1], click[0], self._d.screen)
		self.switchcheckallowrender("fullscreen_settings", 0, 0,  self._d.currentres[1]//3,  self._d.currentres[1]//0.8, False, True, mouse_pos, click[0], self._d.screen)
		self.switchcheckallowrender("musicon_settings", 0, 0,  self._d.currentres[1]//3,  self._d.currentres[1]//0.8, False, True, mouse_pos, click[0], self._d.screen)
		self.switchcheckallowrender("soundon_settings", 0, 0,  self._d.currentres[1]//3,  self._d.currentres[1]//0.8, False, True, mouse_pos, click[0], self._d.screen)
		self.checksliderallowrender("x", 0, 0,  self._d.currentres[1]//3,  self._d.currentres[1]//0.8, False, True, mouse_pos, clickhold, self._d.screen)


