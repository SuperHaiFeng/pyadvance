import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
	"""显示得分信息的类"""

	def __init__(self, ai_settings, screen, stats):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		#显示得分信息时使用的字体设置
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_ships(self):
		"""显示剩余多少飞船"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)

	def prep_level(self):
		"""将等级转换为一副渲染的图像"""
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.scroe_rect.right
		self.level_rect.top = self.scroe_rect.bottom + 10

	def prep_score(self):
		"""将得分转换为一副渲染的图像"""
		# 将得分取圆整
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score) 
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

		self.scroe_rect = self.score_image.get_rect()
		self.scroe_rect.right = self.screen_rect.right - 20
		self.scroe_rect.top = 20

	def prep_high_score(self):
		#将最高分转换为渲染的图像
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

		#将最高分放在屏幕顶部中间
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.scroe_rect.top

	def show_score(self):
		# 在屏幕上显示得分
		self.screen.blit(self.score_image, self.scroe_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)

