'''
https://www.youtube.com/watch?v=W92RjjptAsM
'''

import pygame
from pygame.locals import *

import sys
import random
from time import sleep


WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640

CR_BLACK = (0,0,0)
CR_WHITE = (255,255,255)
CR_YELLOW = (250,250,50)
CR_RED = (250,50,50)

FPS = 60

PATH_RES = '../../../../다운로드/Game_res/PyShooting/'

class Fighter(pygame.sprite.Sprite):
    def __init__(self):
        super(Fighter, self).__init__()
        self.image = pygame.image.load(PATH_RES + 'fighter.png')
        self.rect = self.image.get_rect()
        self.rect.x = int(WINDOW_WIDTH / 2)
        self.rect.y = WINDOW_HEIGHT - self.rect.height
        self.dx = 0
        self.dy = 0

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.x < 0 or self.rect.x + self.rect.width > WINDOW_WIDTH:
            self.rect.x -= self.dx

        if self.rect.y < 0 or self.rect.y + self.rect.height > WINDOW_HEIGHT:
            self.rect.y -= self.dy

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite


class Missile(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Missile, self).__init__()
        self.image = pygame.image.load(PATH_RES + 'missile.png')
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
        self.sound = pygame.mixer.Sound(PATH_RES + 'missile.wav')

    def launch(self):
        self.sound.play()

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y + self.rect.height < 0:  #미사일이 화면 밖으로 나갔으면
            self.kill()

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite   # 충돌난 거 반환


class Rock(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Rock, self).__init__()
        rock_images = ('rock01.png', 'rock02.png', 'rock03.png', 'rock04.png', 'rock05.png', \
                       'rock06.png', 'rock07.png', 'rock08.png', 'rock09.png', 'rock10.png', \
                       'rock11.png', 'rock12.png', 'rock13.png', 'rock14.png', 'rock15.png', \
                       'rock16.png', 'rock17.png', 'rock18.png', 'rock19.png', 'rock20.png', \
                       'rock21.png', 'rock22.png', 'rock23.png', 'rock24.png', 'rock25.png', \
                       'rock26.png', 'rock27.png', 'rock28.png', 'rock29.png', 'rock30.png')

        #self.image = pygame.image.load(random.choice(rock_images))
        rock_img = PATH_RES + random.choice(rock_images)
        self.image = pygame.image.load(rock_img)
        
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def out_of_screen(self):
        if self.rect.y > WINDOW_HEIGHT:
            return True



def draw_text(text, font, surface, x, y, main_color):
    text_obj = font.render(text, True, main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)


def occur_explosion(surface, x, y):
    explosion_image = pygame.image.load(PATH_RES + 'explosion.png')
    explosion_rect = explosion_image.get_rect()
    explosion_rect.x = x
    explosion_rect.y = y
    surface.blit(explosion_image, explosion_rect)

    explosion_sounds = (PATH_RES + 'explosion01.wav', PATH_RES + 'explosion02.wav', PATH_RES + 'explosion03.wav')
    explosion_sound = pygame.mixer.Sound(random.choice(explosion_sounds))
    explosion_sound.play()


def game_loop():
    default_font = pygame.font.Font(PATH_RES + 'NanumGothic.ttf', 28)
    background_image = pygame.image.load(PATH_RES + 'background.png')
    gameover_sound = pygame.mixer.Sound(PATH_RES + 'gameover.wav')
    pygame.mixer.music.load(PATH_RES + 'music.wav')
    pygame.mixer.music.play(-1) #무한반복:-1
    fps_clock = pygame.time.Clock()

    fighter = Fighter()
    missiles = pygame.sprite.Group()    # 여러 객체
    rocks = pygame.sprite.Group()   # 여러 객체

    occur_prob = 40
    shot_count = 0
    count_missed = 0

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    fighter.dx -= 5
                elif event.key == pygame.K_RIGHT:
                    fighter.dx += 5
                elif event.key == pygame.K_UP:
                    fighter.dy -= 5
                elif event.key == pygame.K_DOWN:
                    fighter.dy += 5
                elif event.key == pygame.K_SPACE:
                    missile = Missile(fighter.rect.centerx, fighter.rect.y, 10)
                    missile.launch()
                    missiles.add(missile)
                elif event.key == pygame.K_ESCAPE:
                    done = True
                    break

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighter.dx = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    fighter.dy = 0
                    
        screen.blit(background_image, background_image.get_rect())

        occur_of_rocks = 1 + int(shot_count / 300)  # 많이 맞추면 운석을 많아지게
        min_rock_speed = 1 + int(shot_count / 200)  # 
        max_rock_speed = 1 + int(shot_count / 100)  # 운석 100개 맞추면 speed는 1 올린다

        if random.randint(1, occur_prob) == 1:
            for i in range(occur_of_rocks):
                speed = random.randint(min_rock_speed, max_rock_speed)
                rock = Rock(random.randint(0, WINDOW_HEIGHT - 30), 0, speed)
                rocks.add(rock)

        draw_text('파괴된 운석: {}'.format(shot_count), default_font, screen, 100, 20, CR_YELLOW)
        draw_text('놓친: 운석: {}'.format(count_missed), default_font, screen, 400, 20, CR_RED)

        for missile in missiles:
            rock = missile.collide(rocks)   # 미사일과 충돌난 rock 을 리턴해줌
            if rock:
                missile.kill()
                rock.kill()
                occur_explosion(screen, rock.rect.x, rock.rect.y)
                shot_count += 1

        for rock in rocks:
            if rock.out_of_screen():
                rock.kill()
                count_missed += 1

        rocks.update()
        rocks.draw(screen)
        missiles.update()
        missiles.draw(screen)
        fighter.update()
        fighter.draw(screen)
        pygame.display.flip()   # 전체 반영

        if fighter.collide(rocks) or count_missed >= 3:
            pygame.mixer_music.stop()
            occur_explosion(screen, fighter.rect.x, fighter.rect.y)
            pygame.display.update()
            gameover_sound.play()
            sleep(1)
            done = True

        fps_clock.tick(FPS)

    return 'game_menu'


def game_menu():
    start_image = pygame.image.load(PATH_RES + 'background.png')
    screen.blit(start_image, [0, 0])
    draw_x = int(WINDOW_WIDTH / 2)
    draw_y = int(WINDOW_HEIGHT / 4)
    font_70 = pygame.font.Font(PATH_RES + 'NanumGothic.ttf', 70)
    font_40 = pygame.font.Font(PATH_RES + 'NanumGothic.ttf', 40)
    
    draw_text('지구를 지켜라!', font_70, screen, draw_x, draw_y, CR_YELLOW)
    draw_text('엔터 키를 누르면', font_40, screen, draw_x, draw_y + 200, CR_WHITE)
    draw_text('게임이 시작됩니다.', font_40, screen, draw_x, draw_y + 250, CR_WHITE)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return 'play'
            if event.key == pygame.K_ESCAPE:
                return 'quit'
        if event.type == QUIT:
            return 'quit'

    return 'game_menu'


def main():
    global screen

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('PyShooting')
    
    action = 'game_menu'
    while action != 'quit':
        if action =='game_menu':
            action = game_menu()
        elif action == 'play':
            action = game_loop()

    pygame.quit()


if __name__ == "__main__":
    main()
    