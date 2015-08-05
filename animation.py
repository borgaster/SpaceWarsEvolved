import os

from loader import *
import pygame
from pygame.locals import *


class AnimatedSprite(pygame.sprite.Sprite):
		def __init__(self, images,x,y):
			pygame.sprite.Sprite.__init__(self)
			self._images 			= images
			# Track the time we started, and the time between updates.
			# Then we can figure out when we have to switch the image.
			self._start 			= pygame.time.get_ticks()
			fps=20
                        self._delay 			= 1000 / fps
			self._last_update = 0
			self._frame 			= 0
			self.image 				= self._images[self._frame]
			# coordenadas onde a animacao vai estar
                        #vai dar jeito receber o 'w' e o 'h' como argumentos
                        self.check = 0
			self.w = x
                        self.h = y
			self.location 		= (self.w,self.h)

		def update(self, t):
			# Note that this doesn't work if it's been more that self._delay
			# time between calls to update(); we only update the image once
			# then, but it really should be updated twice.
			if t - self._last_update > self._delay and self._frame < len(self._images):
                            self.image = self._images[self._frame]
                            self._frame += 1

			    # Animation Finished, choosing a new location
                            #Faz o loop da animacao voltando ao 0 do array

                            if self._frame >= len(self._images):
                                self._frame = 0
                                self.check = 1
				x, y = self.image.get_size()
				self.location 		= (self.w,self.h)

                            self._last_update = t

                            
                            
                def move(self,x,y):
                    self.w = x
                    self.h = y
                    self.location = (x,y)

                        
		def render(self, screen, loop):
                        #   if self._frame <= len(self._images):
                        #self.image = rotate(self.image, 90)
                        if loop is False:
                            if self.check != 1:
                                self.update(pygame.time.get_ticks())
                                screen.blit(self.image, self.location)
                        else:
                            self.update(pygame.time.get_ticks())
                            screen.blit(self.image, self.location)
            




def load_sliced_sprites(w, h, filename):
    '''
    Specs :
    	Master can be any height.
    	Sprites frames width must be the same width
    	Master width must be len(frames)*frame.width
    '''
    images = []
    #master_image = pygame.image.load(os.path.join('img', filename)).convert_alpha()
    #
    master_image, master_rect = load_image(filename,-1)
    #
    master_width, master_height = master_image.get_size()
    for i in xrange(int(master_width/w)):
    	images.append(master_image.subsurface((i*w,0,w,h)))
    return images

