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


class Dictionary():
    def __init__(self) -> None:
        english = {
            'New game':'New game',
            "Quit game":"Quit game",
            "Settings":"Settings",
            "Language":"Language",
            "Screen resolution":"Screen resolution",
            "Sound":"Sound",
        }
        with open('dictionary-english.json', 'w') as f:
            json.dump(english, f)

        rus = {
            'New game':'Новая игра',
            "Quit game":"Выход из игры",
            "Settings":"Настройки",
            "Language":"Язык",
            "Screen resolution":"Расширение экрана",
            "Sound":"Звук",
        }
        with open('dictionary-rus.json', 'w') as f:
            json.dump(rus, f)

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
        # В СЛОВАРЕ ДОЛЖНЫ РАСПОЛОГАТЬСЯ ВСЕ КНОПКИ ГЛАВНОГО МЕНЮ
        triger_plus = int(self.screen_height/30) #36
        self.menu_nutton = [
            self.NewGame_rect.y - triger_plus,
            self.Settings_rect.y - triger_plus,
            self.QuitGame_rect.y - triger_plus
        ]# В СЛОВАРЕ ДОЛЖНЫ РАСПОЛОГАТЬСЯ ВСЕ КНОПКИ ГЛАВНОГО МЕНЮ
        # ============================================================


        self.n = 0 # id скнопки в списке
        #========== TRIGER ===========================================================
        self.image_menu_triger = pygame.image.load('img\\1920_1080\\menu_triger.png')
        self.image_menu_triger = pygame.transform.scale(self.image_menu_triger,
            (463*(self.screen_width/1920), 115*(self.screen_height/1080))
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



if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    pg_game = ProgectLavel()
    pg_game.run_game() 