import pygame
from pygame.locals import *
from menu_view import MenuView
from howto_view import HowtoView

class MenuController:
	""" Class defined for handling keyboard events in the menu"""
	def __init__(self, puzzleGame):
		self.puzzleGame=puzzleGame #Since all views are run from puzzleGame, takes that in as an attribute.

	def handleEvent(self, event):
		if type(self.puzzleGame.activeView) == MenuView: #If the user is in the Main Menu, follows these instructions. 
			if event.type == KEYDOWN: #If a key is pressed:
				if event.key == K_1: #If the user presses '1', starts the game.
					self.puzzleGame.switchView(self.puzzleGame.gameView)
					self.puzzleGame.drawGame()

				elif event.key == K_2: #If the user presses '2', goes to the 'How-to' page
					self.puzzleGame.switchView(self.puzzleGame.howtoView)
					self.puzzleGame.drawGame()

				elif event.key == K_3 or event.key== K_ESCAPE: #If the user presses '3' or 'ESC', quits the game altogether while in the main menu.
					self.puzzleGame.stop()

		elif type(self.puzzleGame.activeView) == HowtoView: #If the user is in the How-to page, follows these instructions. 
			if event.type == KEYDOWN:
				if event.key== K_ESCAPE: #Returns back to the main menu after the user reads the 'How-to' page.
					self.puzzleGame.switchView(self.puzzleGame.menuView)
					self.puzzleGame.drawGame()
