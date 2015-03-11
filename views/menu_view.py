import sys, pygame, os
from pygame.locals import *
from base_view import BaseView
from menu_key_controller import MenuController

class menuOption:
	def __init__(self, text, color, menuWidth, menuHeight):
		self.font = pygame.font.SysFont('Arial',40)
		self.color = color
		self.text = self.font.render(text, True, self.color)
		self.size = self.text.get_size()
		self.width = self.size[0]
		self.height = self.size[1]
		self.x = centerWidth(menuWidth, self.width)
		self.y = centerHeight(menuHeight, self.height)

class menuTitle:
	def __init__(self, text, color, menuWidth, menuHeight):
		self.font = pygame.font.SysFont('Arial',80)
		self.color = color
		self.text = self.font.render(text, True, self.color)
		self.size = self.text.get_size()
		self.width = self.size[0]
		self.height = self.size[1]
		self.x = centerWidth(menuWidth, self.width)
		self.y = centerHeight(menuHeight, self.height)

class MenuView(BaseView):
	def __init__(self):
		self.background = (40,40,40)
		self.width= 640
		self.height = 480

	def Screen(self):
		self.item1= menuTitle("grid",(255,140,0), self.width, self.height-300)
		self.item2 = menuOption("how-to",(250,250,210), self.width, self.height+65)
		self.item2_1= menuOption("2",(255,255,0), self.width-300, self.height+65)
		self.item3 = menuOption("start",(250,250,210), self.width, self.height - 2*self.item2.height+65)
		self.item3_2= menuOption("1",(124,252,0), self.width-300, self.height+65)
		self.item4 = menuOption("quit", (250,250,210),self.width, self.height + 2*self.item2.height+65)
		self.item4_3= menuOption("3",(255,97,3), self.width-300, self.height+65)		
		
	def draw(self, puzzleGame):	
		os.environ['SDL_VIDEO_CENTERED'] = '1'  #centers the starting postion of the window
		self.Screen()
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.update()
		self.Screen()
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.screen.fill((40,40,40))
		self.screen.blit(self.item1.text, (self.item1.x, self.item1.y))	
		self.screen.blit(self.item2.text, (self.item1.x, self.item2.y))
		self.screen.blit(self.item3.text, (self.item1.x, self.item3.y))
		self.screen.blit(self.item4.text, (self.item1.x, self.item4.y))
		self.screen.blit(self.item2_1.text, (self.item2_1.x, self.item2.y))
		self.screen.blit(self.item3_2.text, (self.item3_2.x, self.item3.y))
		self.screen.blit(self.item4_3.text, (self.item4_3.x, self.item4.y))
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
# pygame.font.init()
# controller = MenuController()
# view = MenuView(controller)

# running = True

# view.draw()
# while running:
# 	for event in pygame.event.get():
#  		if event.type == pygame.QUIT:
#  			running = False
#  		if event.type == KEYDOWN:
#  			controller.handle_menu_key_event(event)
#  			view.draw()
