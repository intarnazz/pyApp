import pygame
import sys
from settings import *
from start_screen import *
from media import *
from dictionary import *
class ProgectLavel():

    def __init__(self):

        self.dictionary = Dictionary()
        
        self.settings = Settings()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            ) # РАСШИРЕНИЕ
        self.screen_rect = self.screen.get_rect()
        self.A = 0 # АЛЬФА КАНАЛ ЭКРАНА ЗАГРУЗКИ
        #=================== ЭКРАН ЗАГРУЗКИ =================================
        self.image_load_screen = pygame.image.load('img\\1920_1080\\load_screen.png')
        self.image_load_screen = pygame.transform.scale(self.image_load_screen,
            (self.settings.screen_width, self.settings.screen_height)
            )

        self.rect_load_screen = self.image_load_screen.get_rect()
        self.rect_load_screen.center = self.screen_rect.center
        #=================== //ЭКРАН ЗАГРУЗКИ// =================================
        self.start_stop = False
        self.s_c = False
        self.start = False

        self.start_screen = StartScreen(
            self.screen, 
            self.settings.form, 
            self.settings.screen_width,
            self.settings.screen_height 
            )
        self.media = Media()
        pygame.mouse.set_visible(False)



    def run_game(self):
        """ ОСНОВНОЙ ЦИКЛ """
        while True:
            self._check_events()
            self._update_screen()
#/////////////////////////////////////////////////////////////// ДАЛЕЕ МОДУЛИ "RUN_GAME" //////////////////////////////////////////
    #================= ИВЕНТЫ КНОПКИ ============================
    def _check_events(self):
        """ Проверка ивентов """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_events_KEYDOWN(event)
            elif event.type == pygame.KEYUP:
                self._check_events_KEYUP(event)

    def _check_events_KEYDOWN(self, event):# === НАЖАТИЕ КНОПКИ ===
        if event.key == pygame.K_ESCAPE:
            self.start_screen.menu_event(1)
        elif event.key == pygame.K_RETURN:
            self.start_screen.menu_event(0)
        elif event.key == pygame.K_DOWN:
            self.media.cursor_move()
            self.start_screen.update(-1)
        elif event.key == pygame.K_UP:
            self.media.cursor_move()
            self.start_screen.update(1)

    def _check_events_KEYUP(self, event):# === ОТПУСКАНИЕ КНОПКИ ===
        pass
    #================= //НАЖАТИЕ КНОПКИ// ============================
#/////////////////////////////////////////////////////////////// КОНЕЦ "RUN_GAME" //////////////////////////////////////////

    def _update_screen(self):
        """ ОТРИСОВКА ЭКРАНА """
        if self.start_stop: # ГЛАВНОЕ МЕНЮ
            self.screen.fill(self.settings.bgcolor)
            self.start_screen.main_screen()
            self.screen.blit(self.image_load_screen, self.rect_load_screen)
            pygame.display.flip()
            self.clock.tick(60)  # limits FPS to 60
        else:
            self.screen.fill(self.settings.bgcolor)
            if self.s_c:
                self.start_screen.main_screen()
            #=================== ЭКРАН ЗАГРУЗКИ =================================
            if self.start_stop == False:
                self.image_load_screen.set_alpha(self.A)
            if self.start == False:
                self.A = self.A + 1
                if self.A == 255:
                    self.s_c = True
                    self.start = True
            if self.start == True and self.start_stop == False:
                self.A = self.A - 4
                if self.A == 0:
                    self.start_stop = True
            #self.image_load_screen = pygame.transform.scale()
            if self.start_stop == False:
                self.screen.blit(self.image_load_screen, self.rect_load_screen)
            #=================== //ЭКРАН ЗАГРУЗКИ// =================================
            # Отображение полследнего прорисованого экрана
            pygame.display.flip()
            self.clock.tick(60)  # limits FPS to 60


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    pg_game = ProgectLavel()
    pg_game.run_game() 