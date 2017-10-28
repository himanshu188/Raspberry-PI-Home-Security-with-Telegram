import pygame, sys
from pygame.locals import *
import pygame.camera
SIZE = (1280,960)
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0],SIZE)
cam.start()
image= cam.get_image()
pygame.image.save(image,'img.jpg')
cam.stop()
