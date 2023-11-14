import pygame

class Button():
	"""
	A class to represent a button in a Pygame GUI.

	Attributes:
		x (int): The x-coordinate of the button's center.
		y (int): The y-coordinate of the button's center.
		image (str): The filepath to the image to be displayed on the button.
		image_hover (str): The filepath to the image to be displayed on the button when the mouse hovers over it.
		clicked (bool): Whether or not the button has been clicked.

	Methods:
		draw(surface): Draws the button on the given Pygame surface and returns whether or not the button has been clicked.
	"""
	def __init__(self, x, y, image, image_hover):
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.image_hover = pygame.image.load(image_hover)
		self.rect_hover = self.image_hover.get_rect()
		self.rect_hover.center = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		surface.blit(self.image, (self.rect.x, self.rect.y))
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			surface.blit(self.image_hover, (self.rect_hover.x, self.rect_hover.y))
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return action
