
pygame.init()
fpsClock= pygame.time.Clock()
pygame.mixer.init(channels = 8)
pygame.font.init()

model = EvoSnakeModel()
controller = EvoSnakeController(model)
view = EvoSnakeView(model,controller)

running = True
