import pygame
import sys
import os


from data.scripts.funks import Funks
from data.scripts.data import Data
from data.scripts.img import Img
from data.scripts.sound import Sound
from data.scripts.main import Main

if __name__ == "__main__":
	pygame.init()
	pygame.display.set_caption('Snake by Hatzi')
	

	SCREENWIDTHFULLSCREEN = 1920
	SCREENHEIGHTFULLSCREEN = 1080

	pygame.display.set_mode((SCREENWIDTHFULLSCREEN, SCREENHEIGHTFULLSCREEN))
	pygame.mouse.set_visible(False)
	clock = pygame.time.Clock()

	_d = Data(SCREENWIDTHFULLSCREEN, SCREENHEIGHTFULLSCREEN) #init data
	_i = Img(_d)	#init imgs
	_s = Sound()	#init sounds
	_f = Funks(_d, _i, _s)	#init funcs
	game = Main(_d, _f, _i, _s) #new game
	
	def exitgame():
		pygame.quit()
		sys.exit()

	pygame.display.set_icon(_i.icon)

	mouse_pos = (0,0)
	mousewheel = [0, 0]
	click = [False, False, False]		#left #middle #right mouse click
	clickhold = [False, False, False]	#holds if mouse btn is hold
	
	while True:

		click = [False, False, False]
		mousewheel = [0, 0]


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					exitgame()
			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_F4 and pygame.key.get_pressed()[pygame.K_LALT] or pygame.key.get_pressed()[pygame.K_RALT]):
					exitgame()
				if event.key == pygame.K_ESCAPE:
					if _d.ingame:
						_s.clicksound.play()
						_d.ingame = False
					if _d.settings:
						_s.clicksound.play()
						_d.settings = False
					#EXITSCREEN DINGS NOCH
				if (event.key == pygame.K_w or event.key == pygame.K_UP) and not _d.pausescreen and not game.bonk and not game.onekey and game.snake_direction != "down":
					game.snake_direction = "up"
					game.w_down = True
					game.onekey = True
				if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and not _d.pausescreen and not game.bonk and not game.onekey and game.snake_direction != "up":
					game.snake_direction = "down"
					game.s_down = True
					game.onekey = True
				if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and not _d.pausescreen and not game.bonk and not game.onekey and game.snake_direction != "right":
					game.snake_direction = "left"
					game.a_down = True
					game.onekey = True
				if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and not _d.pausescreen and not game.bonk and not game.onekey and game.snake_direction != "left":
					game.snake_direction = "right"
					game.d_down = True
					game.onekey = True
				if event.key == pygame.K_SPACE:
					if not game.runninggame:
						game = Main(_d, _f, _i, _s)
					elif game.runninggame and not _d.pausescreen and not game.bonk:
						_d.pausescreen = True
					elif game.runninggame and _d.pausescreen:
						_d.pausescreen = False
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					game.w_down = False
					game.w_down_timer = game.holddowntime
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					game.d_down = False
					game.d_down_timer = game.holddowntime
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					game.s_down = False
					game.s_down_timer = game.holddowntime
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					game.a_down = False
					game.a_down_timer = game.holddowntime
			if event.type == pygame.MOUSEMOTION:
				mouse_pos = event.pos
			if event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					click[0] = True
					clickhold[0] = False
				elif event.button == 3:
					click[2] = True
					clickhold[2] = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					clickhold[0] = True
				elif event.button == 3:
					clickhold[2] = True
			if event.type == pygame.MOUSEWHEEL:
				mousewheel = [event.x, event.y]

		if _d.reloadgame:
			_d.reloadgame = False
			game = Main(_d, _f, _i, _s)

		if _d.ingame and not _d.exitscreen:
			game.gameloop(mouse_pos, click)
		elif _d.settings and not _d.exitscreen:
			_f.rendersettings(mouse_pos, click, clickhold, mousewheel)
		elif _d.menu and not _d.exitscreen:
			_f.menu(mouse_pos, click)

		_f.texthandler("hatzi", _d.screen)
		if _d.exitscreen:
			_f.renderexitscreen(mouse_pos, click)


		if clickhold == [False, False, False]:
			_d.screen.blit(_i.cursor, [mouse_pos[0] -8, mouse_pos[1]])
		elif clickhold[0]:
			_d.screen.blit(_i.cursorpressed, [mouse_pos[0] -8, mouse_pos[1]])
		elif clickhold[2]:
			_d.screen.blit(_i.cursorright, [mouse_pos[0] -8, mouse_pos[1]])


		pygame.display.update()
		clock.tick(60)