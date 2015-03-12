import sys, pygame, os, random, time
from PIL import Image
from pygame.locals import *
from base_view import BaseView


class HowtoItem:
	def __init__(self, text, color, menuWidth, menuHeight, dy = 0):
		self.font = pygame.font.SysFont('Arial',16)
		self.color = color
		self.text = self.font.render(text, True, self.color)
		self.size = self.text.get_size()
		self.width = self.size[0]
		self.height = self.size[1]
		self.x = centerWidth(menuWidth, self.width)
		self.y = centerHeight(menuHeight, self.height) + dy

class menuTitle:
	def __init__(self, text, color, menuWidth, menuHeight, dy = 0):
		self.font = pygame.font.SysFont('Arial',80)
		self.color = color
		self.text = self.font.render(text, True, self.color)
		self.size = self.text.get_size()
		self.width = self.size[0]
		self.height = self.size[1]
		self.x = centerWidth(menuWidth, self.width)
		self.y = centerHeight(menuHeight, self.height) + dy

class HowtoView(BaseView):

	def draw(self, puzzleGame):	
		"""Draws the howto menu
		"""

		self.width=puzzleGame.surface.get_width()
		self.height=puzzleGame.surface.get_height()

		self.item1= menuTitle("grid",(255,140,0), self.width, self.height-300)
		self.item2 = HowtoItem("grid is a puzzle game.",(250,250,210), self.width, self.height+65)
		self.item3= HowtoItem("The objective is to reach the target image by clicking on the ",(250,250,210), self.width, self.height+65)
		self.item4 = HowtoItem("cells. Each time you click a cell, the color and number of  ",(250,250,210), self.width, self.height+65)
		self.item5 = HowtoItem("that cell and the 4 cells change. You have limited clicks. ",(250,250,210), self.width, self.height+65)
		self.item6 = HowtoItem("Good luck!",(250,250,210), self.width, self.height+65)
		os.environ['SDL_VIDEO_CENTERED'] = '1'  #centers the starting postion of the window
		
		puzzleGame.surface.fill((40,40,40))

		pygame.display.update()

		puzzleGame.surface.blit(self.item1.text, (self.item1.x, self.item1.y))	#creates the menu texts
		puzzleGame.surface.blit(self.item2.text, (self.item1.x-200, self.item2.y-60))
		puzzleGame.surface.blit(self.item3.text, (self.item1.x-200, self.item2.y-20))
		puzzleGame.surface.blit(self.item4.text, (self.item1.x-200, self.item2.y))
		puzzleGame.surface.blit(self.item5.text, (self.item1.x-200, self.item2.y+20))
		puzzleGame.surface.blit(self.item6.text, (self.item1.x-200, self.item2.y+60))
		pygame.display.update()

	def handleClick(self, controller, puzzleGame, x, y):
		pass

def centerWidth(widthOuter, widthInner):
	"""Returns the x location of the upper left corner of the item you want to center horizontally in a larger item
	"""
	return widthOuter/2 - widthInner/2

def centerHeight(heightOuter, heightInner):
	"""Returns the y location of the upper left corner of the item you want to center vertically in a larger item
	"""
	return heightOuter/2 - heightInner/2

def find_center(width, height):
	"""Finds the center of an object with a width and height
	"""
	originx = width/2
	originy = height/2
	return [originx,originy]

def centerObject(width_outter, height_outter, width_inner, height_inner):
	"""Returns the (x,y) location of the upper left corner of the item you want to center in a larger box
	"""
	center_outter = find_center(width_outter, height_outter)
	center_inner = find_center(width_inner, height_inner)
	upper_left_corner = [center_outter[0] - center_inner[0], center_outter[1] - center_inner[1]]
	return upper_left_corner


# pygame.init()
# fpsClock= pygame.time.Clock()
# pygame.font.init()

# controller = MenuController
# view = HowtoView()

# running = True

# view.draw()
# while running:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			running = False
# 		if event.type == KEYDOWN:
# 			controller.handle_menu_key_event(event)
# 			view.draw()