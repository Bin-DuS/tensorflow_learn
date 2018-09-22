import sys
import random
import pygame
from pygame.locals import *
WIDTH = 800
HEIGHT = 600
SPEED = [15, 30]
SIZE = [5, 30]
LEN = [1,8]
#random color
def randomColor():
	return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
#random speed
def randomSpeed():
	return random.randint(SPEED[0],SPEED[1])
#random Size
def randomSize():
	#return random.randint(SIZE(0),SIZE[1])
	return random.randint(15,30)
#random Len
def randomLen():
	return random.randint(LEN[0],LEN[1])
#random Pos
def randomPos():
	return (random.randint(0,WIDTH),-20)
#random Code
def randomCode():
	return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-+=*/")
class Code(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#self.font = pygame.font.Font("./font.ttf",randomSize())
		self.font = pygame.font.SysFont("arial",16)
		self.speed = randomSpeed()
		self.code = self.getCode()
		self.image = self.font.render(self.code,True,randomColor())
		self.imgae = pygame.transform.rotate(self.image,random.randint(87,93))
		self.rect = self.image.get_rect()
		self.rect.topleft = randomPos()
	def getCode(self):
		length = randomLen()
		code = ''
		for i in range(length):
			code += randomCode()
		return code
	def update(self):
		self.rect = self.rect.move(0,self.speed)
		if self.rect.top > HEIGHT:
			self.kill()
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Bin.DuS:847379962@qq.com')
clock = pygame.time.Clock()
codesGroup = pygame.sprite.Group()
while True:
	clock.tick(24)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit(0)
	screen.fill((1,1,1))
	codeobject = Code()
	codesGroup.add(codeobject)
	codesGroup.update()
	codesGroup.draw(screen)
	pygame.display.update()