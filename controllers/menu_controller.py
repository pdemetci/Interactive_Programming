import pygame
from pygame.locals import *
import howto_key_controller

class MenuController:
	def __init__(self, puzzleGame):
		self.puzzleGame=puzzleGame

	def handleEvent(self, event):
		if event.type == KEYDOWN:
			if event.key == K_1:
				self.puzzleGame.switchView(self.puzzleGame.gameView)

			if event.key == K_2:
				pass

			if event.key == K_3 or K_ESCAPE:
				pygame.quit()