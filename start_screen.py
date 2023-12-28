import pygame
import sys
import os
from media import *
from settings import *

class StartScreen():
    """ ЭКРАН ГЛАВНОГО МЕНЮ """
    def __init__(self, screen, form, screen_width, screen_height) -> None:
        """ ИНИЦИАЛИЗАЦИЯ """
        pygame.init()
        self.settings = Settings()
        self.media = Media()
        self.language_menu = False
        self.form = form 
        # 'form' припас для маштобирования, пока не использовал (и не буду использовать)
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.settings_menu = False
        self.text_button_init()

        #============================
        #print(pygame.font.get_fonts()) 
        # СПИСОК ШРИФТОВ
        #============================

        #////////////////////// ТЕКСТ КНОПОК ////////////////////////////////
    def text_button_init(self):
        #===================================================================
        #===================================================================
        self.font = pygame.font.SysFont('cambria', int(self.screen_height/43.2)) # ШРИФТ ГЛАВНОГО МЕНЮ
        #===================================================================
        #======= music volume ====================================
        music_volume = f"Music volume: '{int(self.media.get_volume(0) * 100)}'"
        self.image_music_volume = self.font.render(music_volume, True,
            (255, 255, 255), None
            )
        self.rect_music_volume = self.image_music_volume.get_rect()
        self.rect_music_volume.center = self.screen_rect.center
        #print(self.screen_height/1,6875)
        self.rect_music_volume.y = int(self.screen_height/1.6875) #640
        #======= //music volume// ====================================
        #======= RUS ====================================
        rus = "Русский"
        self.image_rus = self.font.render(rus, True,
            (255, 255, 255), None
            )
        self.rect_rus = self.image_rus.get_rect()
        self.rect_rus.center = self.screen_rect.center
        #print(self.screen_height/1,6875)
        self.rect_rus.y = int(self.screen_height/1.6875) #640
        #======= //RUS// ====================================
        #======= New game ====================================
        self.NewGame_image = self.font.render(self.settings.main_dictionary['New game'], True,
            (255, 255, 255), None
            )
        self.NewGame_rect = self.NewGame_image.get_rect()
        self.NewGame_rect.center = self.screen_rect.center
        #print(self.screen_height/1,6875)
        self.NewGame_rect.y = int(self.screen_height/1.6875) #640
        #======= //New game// ====================================
        #======= Quit game ====================================
        self.QuitGame_image = self.font.render(self.settings.main_dictionary["Quit game"], True,
            (255, 255, 255), None
            )
        self.QuitGame_rect = self.QuitGame_image.get_rect()
        self.QuitGame_rect.center = self.screen_rect.center
        self.QuitGame_rect.y = int(self.screen_height/1.421) #760
        #======= //Quit game// ====================================
        #======= Settings ====================================
        self.Settings_image = self.font.render(self.settings.main_dictionary["Settings"], True,
            (255, 255, 255), None
            )
        self.Settings_rect = self.Settings_image.get_rect()
        self.Settings_rect.center = self.screen_rect.center
        self.Settings_rect.y = int(self.screen_height/1.5428571) #700
        #======= //Settings// ====================================
        #======= English ====================================
        english = "English"
        self.image_english = self.font.render(english, True,
            (255, 255, 255), None
            )
        self.rect_english = self.image_english.get_rect()
        self.rect_english.center = self.screen_rect.center
        self.rect_english.y = int(self.screen_height/1.5428571) #700
        #======= //English// ====================================
        #======= Settings menu ====================================
        self.Settings_image_menu = self.font.render(self.settings.main_dictionary["Settings"], True,
            (255, 255, 255), None
            )
        self.Settings_rect_menu = self.Settings_image_menu.get_rect()

        self.Settings_rect_menu.center = self.screen_rect.center
        self.Settings_rect_menu.y = 580 #!!!
        #======= //Settings menu// ====================================
        #======= language ====================================
        self.image_language = self.font.render(self.settings.main_dictionary["Language"], True,
            (255, 255, 255), None
            )
        self.rect_language = self.image_language.get_rect()

        self.rect_language.center = self.screen_rect.center
        self.rect_language.y = 640 #!!!
        #======= //language// ====================================
        #======= language menu ====================================
        self.rect_language_menu = self.image_language.get_rect()
        self.rect_language_menu.center = self.screen_rect.center
        self.rect_language_menu.y = 580 #!!!
        #======= //language menu// ====================================
        #======= screen resolution ====================================
        self.image_screen_resolution = self.font.render(self.settings.main_dictionary["Screen resolution"], True,
            (255, 255, 255), None
            )
        self.rect_screen_resolution = self.image_screen_resolution.get_rect()

        self.rect_screen_resolution.center = self.screen_rect.center
        self.rect_screen_resolution.y = 700 #!!!
        #======= //screen resolution// ====================================
        #======= sound ====================================
        self.image_sound = self.font.render(self.settings.main_dictionary["Sound"], True,
            (255, 255, 255), None
            )
        self.rect_sound = self.image_sound.get_rect()

        self.rect_sound.center = self.screen_rect.center
        self.rect_sound.y = 760 #!!!
        #======= //sound// ====================================
        
        #////////////////////// ТЕКСТ КНОПОК ////////////////////////////////
        #========== линия ===========================================================
        self.image_line = pygame.image.load('img\\1920_1080\\line.png')
        self.image_line = pygame.transform.scale(self.image_line,
            (552*(self.screen_width/1920), 2*(self.screen_height/1080))
        )

        self.rect_line = self.image_line.get_rect()
        self.rect_line.center = self.screen_rect.center
        self.rect_line.y = self.Settings_rect_menu.y + 36 #!!!
        #========== //линия// ===========================================================
        #========== BG - это фоновая картинка ===========================================================
        self.image_main_menu = pygame.image.load('img\\1920_1080\\main_memu0.png')
        self.image_main_menu = pygame.transform.scale(self.image_main_menu,
            (self.screen_width, self.screen_height)
            )

        self.rect_main_menu = self.image_main_menu.get_rect()
        #========== //BG// ===========================================================
        # ============================================================
        # В СПИСКЕ ДОЛЖНЫ РАСПОЛОГАТЬСЯ ВСЕ КНОПКИ ГЛАВНОГО МЕНЮ ========================  СПИСОК
        triger_plus = int(self.screen_height/53) #22 - `не актуален`
        self.menu_nutton = [
            self.NewGame_rect.y - triger_plus,
            self.Settings_rect.y - triger_plus,
            self.QuitGame_rect.y - triger_plus
        ]# В СПИСКЕ ДОЛЖНЫ РАСПОЛОГАТЬСЯ ВСЕ КНОПКИ ГЛАВНОГО МЕНЮ
        # ============================================================


        self.n = 0 # id скнопки в списке
        #========== TRIGER =========================================================== 1,6595
        self.image_menu_triger = pygame.image.load('img\\1920_1080\\menu_triger.png')
        self.image_menu_triger = pygame.transform.scale(self.image_menu_triger,
            (279*(self.screen_width/1920), 69*(self.screen_height/1080))
            )

        self.rect_menu_triger = self.image_menu_triger.get_rect()
        self.rect_menu_triger.center = self.screen_rect.center
        self.rect_menu_triger.y = self.menu_nutton[self.n]   #604
        #========== //TRIGER// ===========================================================
    
    def menu_event(self,button):
        if button == 0: # Enter
            """ СОБЫТИЯ КНОПОК ГЛАВНОГО МЕНЮ """
            if self.n == len(self.menu_nutton) - 1:
                if self.settings_menu == True:
                    pass
                else:
                    sys.exit() # ВЫХОД
            elif self.n == len(self.menu_nutton) - 2:
                if self.language_menu:
                    self.media.event_start_screen()
                    with open('main-dictionary.txt', 'w') as f:
                        f.write('dictionary-english.json')
                    
                    self.language_menu = False
                    self.settings_menu = True
                    self.settings = Settings()
                    self.text_button_init()
                    
                else:
                    self.media.event_start_screen()
                    self.settings_menu = True

            elif self.n == len(self.menu_nutton) - 3:
                if self.settings_menu == True:
                    self.media.event_start_screen()
                    self.language_menu = True
                    self.settings_menu = False
                elif self.language_menu:
                    self.media.event_start_screen()
                    with open('main-dictionary.txt', 'w') as f:
                        f.write('dictionary-rus.json')
                    
                    self.language_menu = False
                    self.settings_menu = True
                    self.settings = Settings()
                    self.text_button_init()
                else:
                    pass
        elif button == 1: # Esc
            if self.settings_menu == True:
                self.media.event_start_screen()
                self.settings_menu = False
            elif self.language_menu == True:
                self.media.event_start_screen()
                self.language_menu = False
                self.settings_menu = True



    def update(self, num):
        """ обновление положения тригера """
        if num == 1:
            if self.n == 0:
                self.n = len(self.menu_nutton) - 1 
                self.rect_menu_triger.y = self.menu_nutton[self.n]
            else:
                self.n = self.n - 1
                self.rect_menu_triger.y = self.menu_nutton[self.n]
        elif num == -1:
            if self.n >= len(self.menu_nutton) - 1:
                self.n = 0
                self.rect_menu_triger.y = self.menu_nutton[self.n]
            else:
                self.n = self.n + 1
                self.rect_menu_triger.y = self.menu_nutton[self.n]

    def main_screen(self):
        """ ОТРЕСОВКА ТЕКСТА КНОПОК И ОТОБРАЖЕНИЕ ТРИГЕРА НА ЭКРАНЕ """
        self.screen.blit(self.image_main_menu, self.rect_main_menu)
        self.screen.blit(self.image_menu_triger, self.rect_menu_triger)
        if self.language_menu:
            self.screen.blit(self.image_line, self.rect_line)
            self.screen.blit(self.image_language, self.rect_language_menu)
            self.screen.blit(self.image_rus, self.rect_rus)
            self.screen.blit(self.image_english, self.rect_english)
            

        elif self.settings_menu:
            self.screen.blit(self.Settings_image_menu, self.Settings_rect_menu)
            self.screen.blit(self.image_line, self.rect_line)
            self.screen.blit(self.image_language, self.rect_language)
            self.screen.blit(self.image_screen_resolution, self.rect_screen_resolution)
            self.screen.blit(self.image_sound, self.rect_sound)
        else:
            self.screen.blit(self.NewGame_image, self.NewGame_rect)
            self.screen.blit(self.Settings_image, self.Settings_rect)
            self.screen.blit(self.QuitGame_image, self.QuitGame_rect)

            


