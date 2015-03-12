print "In MenuView"
import sys, pygame, os
from pygame.locals import *
from base_view import BaseView

class menuItem:
	""" Class that defines the title and the options in the main view such as 'start', 'how-to', and 'quit' """
	def __init__(self, text, textsize, color, menuWidth, menuHeight):
		self.font = pygame.font.SysFont('Arial',textsize)
		self.color = color
		self.text = self.font.render(text, True, self.color)
		self.size = self.text.get_size()
		self.width = self.size[0]
		self.height = self.size[1]
		#To make the positioning process easier, centers each item on the screen first. They will be moved up/down while drawing.
		self.x = centerWidth(menuWidth, self.width) 
		self.y = centerHeight(menuHeight, self.height)

class MenuView(BaseView):
	""" Class to create the GUI view of the Menu. Inherits from BaseView and therefore has 2 methods"""
		
	def draw(self, puzzleGame):	
		""" draws the items on the screen in menu """
		#Getting the width of the screen. Will be used to position the options.
		self.width=puzzleGame.surface.get_width() 
		self.height=puzzleGame.surface.get_height()
		
		#Defining the items using menuItem.
		self.item1= menuItem("grid", 80, (255,140,0), self.width, self.height-300)
		self.item2 = menuItem("how-to",40, (250,250,210), self.width, self.height+65)
		self.item2_1= menuItem("2",40, (255,255,0), self.width-300, self.height+65)
		self.item3 = menuItem("start",40, (250,250,210), self.width, self.height - 2*self.item2.height+65)
		self.item3_2= menuItem("1",40, (124,252,0), self.width-300, self.height+65)
		self.item4 = menuItem("quit",40, (250,250,210),self.width, self.height + 2*self.item2.height+65)
		self.item4_3= menuItem("3", 40, (255,97,3), self.width-300, self.height+65)	

		#drawing the items defined above on the surface created by puzzleGame.
		os.environ['SDL_VIDEO_CENTERED'] = '1'  #centers the starting postion of the window
		pygame.display.update()
		puzzleGame.surface.fill((40,40,40))
		puzzleGame.surface.blit(self.item1.text, (self.item1.x, self.item1.y))	
		puzzleGame.surface.blit(self.item2.text, (self.item1.x, self.item2.y))
		puzzleGame.surface.blit(self.item3.text, (self.item1.x, self.item3.y))
		puzzleGame.surface.blit(self.item4.text, (self.item1.x, self.item4.y))
		puzzleGame.surface.blit(self.item2_1.text, (self.item2_1.x, self.item2.y))
		puzzleGame.surface.blit(self.item3_2.text, (self.item3_2.x, self.item3.y))
		puzzleGame.surface.blit(self.item4_3.text, (self.item4_3.x, self.item4.y))
		pygame.display.update()

	def handleClick(self, controller, puzzleGame, x, y):
		""" A method inherited from BaseView. Since menu is controlled by keyboard and no mouse is used, it does not do anything for menuView. """
		pass

def centerWidth(widthOuter, widthInner):
	"""Returns the x location of the upper left corner of the item you want to center horizontally"""
	return widthOuter/2 - widthInner/2

def centerHeight(heightOuter, heightInner):
	"""Returns the y location of the upper left corner of the item you want to center vertically"""
	return heightOuter/2 - heightInner/2
