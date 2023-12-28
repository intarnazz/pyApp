import pygame

class Media():
    """ ПОДКЛЮЧЕНИЕ ЗВУКОВЫХ КАНАЛОВ """
    def __init__(self) -> None:
        pygame.mixer.init()

        pygame.mixer.Channel(0).play(pygame.mixer.Sound('mp\main-menu.mp3'), loops=-1)
        #pygame.mixer.Channel(0).set_volume(0.0)
        # ОСНОВНАЯ ТЕМА
        #pygame.mixer.Channel(1).play(pygame.mixer.Sound('other\DAGOTHWAVE.mp3'))
    
    def cursor_move(self):
        """ ЗВУК ПЕРЕКЛЮЧЕНИЯ ЧЕГО-ЛИБО """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('mp\CURSOL_MOVE.wav.mp3'))

    def event_start_screen(self):
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('mp\klic.mp3'))

    def get_volume(self, n):
        if n == 0:
            return pygame.mixer.Channel(0).get_volume()
