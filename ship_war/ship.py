import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

	def __init__(self, ai_settings, screen):
		"""初始化飞船并设置其位置"""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# 加载飞船图像
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#在飞船的属性center中存储最小值
		self.center = float(self.rect.centerx)
		#移动标志
		self.moveing_right = False
		self.moveing_left = False

	def update(self):
		"""根据移动标志调整飞船的位置"""
		if self.moveing_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
			
		if self.moveing_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		self.center = self.screen_rect.centerx
