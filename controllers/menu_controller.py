import sys
sys.path.append("/home/pinar/Interactive_Programming/")
import setup
import pygame
from pygame.locals import *
from menu_view import MenuView
from howto_view import HowtoView

class MenuController:
	def __init__(self, puzzleGame):
		self.puzzleGame=puzzleGame

	def handleEvent(self, event):
		if type(self.puzzleGame.activeView) == MenuView:
			if event.type == KEYDOWN:
				if event.key == K_1:
					self.puzzleGame.switchView(self.puzzleGame.gameView)
					self.puzzleGame.drawGame()

				elif event.key == K_2:
					self.puzzleGame.switchView(self.puzzleGame.howtoView)
					self.puzzleGame.drawGame()

				elif event.key == K_3 or event.key== K_ESCAPE:
					self.puzzleGame.stop()

		elif type(self.puzzleGame.activeView) == HowtoView:
			if event.type == KEYDOWN:
				if event.key== K_ESCAPE:
					self.puzzleGame.switchView(self.puzzleGame.menuView)
					self.puzzleGame.drawGame()
