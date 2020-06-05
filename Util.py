import pygame

def loadImages(images):
        surfaces = []
        for image in images:
            surfaces.append(pygame.image.load(image))

        return surfaces