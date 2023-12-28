import json
import pygame

class Settings():
    """ НАСТОЙКИ """
    def __init__(self):
        """ НАСТОЙКИ """
        with open('main-dictionary.txt') as md:
            file = md.read()

        with open(file) as f:
            self.main_dictionary = json.load(f)

        pygame.init()
        info = pygame.display.Info()

        self.screen_width = info.current_w
        self.screen_height = info.current_h

        self.bgcolor = (0,0,0)

        self.form = 1