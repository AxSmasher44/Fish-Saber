import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
import random
pygame.mixer.init()
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
collision_sound = pygame.mixer.Sound("illu.wav")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("fishie.png")
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.surf.set_colorkey((179, 204, 245), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -20)
            collision_sound.play()

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 20)
            collision_sound.play()

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-20, 0)
            collision_sound.play()

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(20, 0)
            collision_sound.play()

            # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("lightsaber.png")
        self.surf = pygame.transform.scale(self.surf, (70, 70))
        self.surf.set_colorkey((179, 204, 245), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_HEIGHT+20, SCREEN_WIDTH+100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(10, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("cloud.png")
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.surf.set_colorkey((179, 204, 245), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_HEIGHT + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = 1

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


