import pygame

class Button():
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