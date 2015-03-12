import sys, pygame, os
from pygame.locals import *
from base_view import BaseView
from menu_view import menuItem, centerWidth, centerHeight

class HowtoView(BaseView):
	""" Class to create the GUI view of the 'How-to' page. Inherits from BaseView and therefore has these 2 methods: draw & handleClick """
	def draw(self, puzzleGame):	
		"""Draws the items on 'How-to' page """

		self.width=puzzleGame.surface.get_width()
		self.height=puzzleGame.surface.get_height()

		# '\n' didn't seem to work properly for some reason. That's why to 
		self.item1= menuItem("grid", 80, (255,140,0), self.width, self.height-300)
		self.item2 = menuItem("grid is a puzzle game.",20, (250,250,210), self.width, self.height)
		self.item3= menuItem("The objective is to reach the target image by clicking on the ",20, (250,250,210), self.width, self.height)
		self.item4 = menuItem("cells. Each time you click a cell, the color and number of  ", 20, (250,250,210), self.width, self.height)
		self.item5 = menuItem("that cell and the 4 cells change. You have limited clicks. ", 20, (250,250,210), self.width, self.height)
		self.item6 = menuItem("Press ESC to go back to the main menu", 20, (250,250,210), self.width, self.height)
		self.item7 = menuItem("Good luck!",20, (250,250,210), self.width, self.height)

		os.environ['SDL_VIDEO_CENTERED'] = '1'  #centers the starting postion of the window
		puzzleGame.surface.fill((40,40,40)) #Fills the surface with the background color
		pygame.display.update()

		#draws the items on the surface
		puzzleGame.surface.blit(self.item1.text, (self.item1.x, self.item1.y))	
		puzzleGame.surface.blit(self.item2.text, (self.item1.x-200, self.item2.y-60))
		puzzleGame.surface.blit(self.item3.text, (self.item1.x-200, self.item2.y-20))
		puzzleGame.surface.blit(self.item4.text, (self.item1.x-200, self.item2.y))
		puzzleGame.surface.blit(self.item5.text, (self.item1.x-200, self.item2.y+20))
		puzzleGame.surface.blit(self.item6.text, (self.item1.x-200, self.item2.y+60))
		puzzleGame.surface.blit(self.item7.text, (self.item1.x-200, self.item2.y+100))
		#updates the display to show the items drawn and the background color.
		pygame.display.update()

	def handleClick(self, controller, puzzleGame, x, y):
		""" A method inherited from BaseView. Since how-to page is controlled by keyboard and no mouse is used, it does not do anything for HowtoView. """
		pass