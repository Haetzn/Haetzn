
import pygame
import os



class Data:
	def __init__(self, Fullscreenwidth, Fullscreenheight):
		self.loadsettings(Fullscreenwidth, Fullscreenheight)

	def loadsettings(self, Fullscreenwidth, Fullscreenheight):
		#save max res
		self.Fullscreenwidth = Fullscreenwidth
		self.Fullscreenheight = Fullscreenheight
		self.settingsfile = "./data/settings.txt"

		self.standardsettings = "0 1980 1920 0 0 0 0 1 0 0"

		self.soundvol = 0
		self.musicvol = 0
		self.fullscreen = False
		self.currentres = (3072, 1920)
		self.bombkill = False
		self.bordercollisions = False
		self.musicbool = False
		self.soundbool = False
		self.highscore = 0

		self.screen = pygame.display.set_mode(self.currentres)
		
		self.translator = {0: False, 1: True}
		self.reversetranslator = {False : 0, True : 1}
		
		self.readtovars()
		
		#settings
		self.score = 0
		self.scorebefore = self.score
		self.surfsize = (self.currentres[0] //2, self.currentres[1] //2)
		self.surf = pygame.Surface(self.surfsize)
		self.surfblit = self.surf

		self.reloadgame = False

		self.possibleresolutions = {0: (self.Fullscreenwidth, self.Fullscreenheight), 1: (1920, 1080), 2:(960, 540)}

		self.pausescreen = False
		self.exitscreen = False

		self.ingame = False
		self.menu = True
		self.settings = False

	def readtovars(self):
		data = self.checkfileorcreate(self.settingsfile)

		if(len(data) >= 10):
			self.fullscreen = self.translator[int(data[0])]
			self.currentres = (int(data[1]), int(data[2]))
			self.bombkill = self.translator[int(data[3])]
			self.bordercollisions = self.translator[int(data[4])]
			self.musicbool = self.translator[int(data[5])]
			self.musicvol = int(data[6])
			self.soundbool = self.translator[int(data[7])]
			self.soundvol = int(data[8])
			self.highscore = int(data[9])

			if self.fullscreen:
				self.screen = pygame.display.set_mode(self.currentres, pygame.FULLSCREEN)
			else:
				self.screen = pygame.display.set_mode(self.currentres, pygame.RESIZABLE)

		print(self.fullscreen)
		print(self.currentres)
		print(self.bombkill)
		print(self.bordercollisions)
		print(self.musicbool)
		print(self.musicvol)
		print(self.soundbool)
		print(self.soundvol)
		print(self.highscore)


	def checkfileorcreate(self, path):
		if(self.checkfile(path)):
			print("File excisting")
			data = self.readfile(path)
			print(f"{path}: {data}")
			
			return data

		else:
			print(f"{path} not found, creating file")
			self.new_file(path)
			if self.checkfile(path):
				print(f"{path} created successfully")
				data = self.readfile(path)
				print(f"{path}: {data}")
			
				return data
			else:
				print(f"Error while creating file at {path}")
				return [""]
		

	def writesettings(self):
		data = [str(self.reversetranslator[self.fullscreen]), str(self.currentres[0]), str(self.currentres[1]), str(self.reversetranslator[self.bombkill]), str(self.reversetranslator[self.bordercollisions]),
			 str(self.reversetranslator[self.musicbool]), str(self.musicvol), str(self.reversetranslator[self.soundbool]), str(self.soundvol), str(self.highscore)]

		self.writetofile(self.settingsfile, data)
		
		self.reloadgame = True

	def checkfile(self, path):
		return os.path.exists(path)

	def new_file(self, path):
		f = open(path, "w")
		f.close()

	def readfile(self, path):
		returner = []
		f = open(path, "r")
		for line in f:
			returner.append(line.replace("\n", ""))
		
		f.close()
		return returner

	def writetofile(self, path, data):
		stringdata = ""
		for d in data:
			stringdata += str(d)+"\n"

		f = open(path, "w")
		f.write(stringdata)
		f.close()


			