import sys, pygame, os, random, time
from PIL import Image
from pygame.locals import *

class HowtoModel():

	def __init__(self):
		self.backgroundColor = (40,40,40)
		self.menu = HowtoGUI()
		self.screenstate = "MenuScreen"	#state of the screen size (default vs fullscreen)
		self.gamestate = "Menuing"	#state of the game (in menu vs in game)
		self.timestart = time.time()

class HowtoItem:
	def __init__(self, text, color, menuWidth, menuHeight, dy = 0):
		self.font = pygame.font.Font('neuropol.ttf',16)
		self.color = color
		self.text = self.font.render(text, True, self.color)
		self.size = self.text.get_size()
		self.width = self.size[0]
		self.height = self.size[1]
		self.x = centerWidth(menuWidth, self.width)
		self.y = centerHeight(menuHeight, self.height) + dy

class menuTitle:
	def __init__(self, text, color, menuWidth, menuHeight, dy = 0):
		self.font = pygame.font.Font('Architect.ttf',80)
		self.color = color
		self.text = self.font.render(text, True, self.color)
		self.size = self.text.get_size()
		self.width = self.size[0]
		self.height = self.size[1]
		self.x = centerWidth(menuWidth, self.width)
		self.y = centerHeight(menuHeight, self.height) + dy

class HowtoGUI:
	def __init__(self, width = 640, height = 480):
		self.width = width
		self.height = height
		self.font = pygame.font.Font('neuropol.ttf',40)
		self.display_resolution = pygame.display.Info()

	def Screen(self):
		"""Encodes the screenstate of 
		"""
		self.width = 640
		self.height = 480

		self.item1= menuTitle("grid",(255,140,0), self.width, self.height-300)
		self.item2 = HowtoItem("grid is a puzzle game.",(250,250,210), self.width, self.height+65)
		self.item3= HowtoItem("The objective is to reach the target image by clicking on the ",(250,250,210), self.width, self.height+65)
		self.item4 = HowtoItem("cells. Each time you click a cell, the color and number of  ",(250,250,210), self.width, self.height+65)
		self.item5 = HowtoItem("that cell and the 4 cells change. You have limited clicks. ",(250,250,210), self.width, self.height+65)
		self.item6 = HowtoItem("Good luck!",(250,250,210), self.width, self.height+65)

class HowtoView:
	def __init__(self, model, controller):
		self.model = model
		self.controller = controller

	def drawMenu(self):	
		"""Draws the main menu
		"""
		os.environ['SDL_VIDEO_CENTERED'] = '1'  #centers the starting postion of the window
		
		self.model.menu.Screen()
		self.screen = pygame.display.set_mode((self.model.menu.width, self.model.menu.height))

		self.screen.fill(model.backgroundColor)

		pygame.display.update()

		if self.model.screenstate == 'Minimized' and self.model.menu.width != 400:
			self.model.menu.Screen()
			self.screen = pygame.display.set_mode((self.model.menu.width, self.model.menu.height))


		self.screen.fill((40,40,40))

		self.screen.blit(self.model.menu.item1.text, (self.model.menu.item1.x, self.model.menu.item1.y))	#creates the menu texts
		self.screen.blit(self.model.menu.item2.text, (self.model.menu.item1.x-200, self.model.menu.item2.y-60))
		self.screen.blit(self.model.menu.item3.text, (self.model.menu.item1.x-200, self.model.menu.item2.y-20))
		self.screen.blit(self.model.menu.item4.text, (self.model.menu.item1.x-200, self.model.menu.item2.y))
		self.screen.blit(self.model.menu.item5.text, (self.model.menu.item1.x-200, self.model.menu.item2.y+20))
		self.screen.blit(self.model.menu.item6.text, (self.model.menu.item1.x-200, self.model.menu.item2.y+60))
		pygame.display.update()

class MenuController:
	def __init__(self,model):
		self.model = model

	def handle_menu_key_event(self, event):
		"""Handles all of the key events while in the main menu
		"""
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()

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


pygame.init()
fpsClock= pygame.time.Clock()
pygame.font.init()

model = HowtoModel()
controller = MenuController(model)
view = HowtoView(model,controller)

running = True

view.drawMenu()
while running:
	while model.gamestate == 'Menuing' and running:
		for event in pygame.event.get():
 			if event.type == pygame.QUIT:
 				running = False
 			if event.type == KEYDOWN:
 				controller.handle_menu_key_event(event)
 				view.drawMenu()