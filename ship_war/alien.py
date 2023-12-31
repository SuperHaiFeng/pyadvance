import pygame
from pygame.sprite import Sprite

import pkg_resources

class Alien(Sprite):
	"""表示单个飞船的类"""

	def __init__(self, ai_settings, screen):
		"""初始化飞船并设置起始位置"""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		image_path = pkg_resources.resource_filename(__name__, 'images/alien.bmp')
		self.image = pygame.image.load(image_path)
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	def blitme(self):
		"""在指定位置绘制"""
		self.screen.blit(self.image, self.rect)


	def update(self):
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
