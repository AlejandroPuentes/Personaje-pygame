import pygame
from pygame import *



class Character(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.left = None
        self.right = None
        self.down = None
        self.up = None
        self.jump = None
        self.vel = 5
        self.dir = 0
        self.images = None
        self.current = 0
        self.salto = False
        self.delta = 200
    def setLeft(self, left):
        self.left = left

    def setUp(self, up):
        self.up = up

    def setRight(self, right):
        self.right = right

    def setDown(self, down):
        self.down = down

    def setJump(self, jump):
        self.jump = jump

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getDown(self):
        return self.down

    def getJump(self):
        return self.jump

    def setVel(self, velocity):
        self.vel = velocity

    def getSurfaces(self, images):
        surfaces = []
        for image in images:
            surfaces.append(pygame.image.load(image))

        return surfaces

    #i r !
    def loadImages(self):
        self.images = []
        self.images.append(self.getSurfaces(self.right.getImage()))
        self.images.append(self.getSurfaces(self.left.getImage()))
        self.images.append(self.getSurfaces(self.down.getImage()))
        self.images.append(self.getSurfaces(self.up.getImage()))
        self.images.append(self.getSurfaces(self.jump.getImage()))
        self.image = self.images[self.dir][self.current]
        self.rect = self.image.get_rect()

    

    def update(self):       
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.left -= self.vel
            self.dir = 1
        elif keys[K_RIGHT]:
            self.rect.left += self.vel
            self.dir = 0
        if keys[K_UP]:
            self.rect.top -= self.vel
            self.dir = 3
        elif keys[K_DOWN]:
            self.rect.top += self.vel            
            self.dir = 2
        if keys[K_LEFT] or keys[K_RIGHT] or keys[K_UP] or keys[K_DOWN]:
            self.image = self.images[self.dir][self.current]
            self.current += 1
            self.current %= 3
        if self.salto:
            self.rect.top += self.delta
            self.salto = False
            self.dir = 0
        else:
            if keys[K_SPACE]:
                self.rect.top -= self.delta
                self.dir = 4
                self.salto = True


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def place(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def getPos(self):
        return self.rect.x, self.rect.y

