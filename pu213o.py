import pygame
import Stuff
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,

    K_ESCAPE,
    KEYDOWN,
    QUIT
)

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
crashed = False

pygame.mixer.music.load("USSR.mp3")
pygame.mixer.music.play(loops=-1)
collision_sound = pygame.mixer.Sound("illu.wav")


my_font = pygame.font.SysFont("monospace", 100)
score = 0
score_text = my_font.render(f"{score}", True, (0, 0, 0))
INCREMENT_SCORE = pygame.USEREVENT + 3
pygame.time.set_timer(INCREMENT_SCORE, 2000)
# Create a custom event for adding a new enemy
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 500)

ADD_CLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_CLOUD, 1750)

player = Stuff.Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
clouds = pygame.sprite.Group()
clock = pygame.time.Clock()

while not crashed:
    for event in pygame.event.get():
        if event.type == QUIT:
            crashed = True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                crashed = True
        elif event.type == ADD_ENEMY:
            new_enemy = Stuff.Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADD_CLOUD:
            new_cloud = Stuff.Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
        elif event.type == INCREMENT_SCORE:
            score += 1
            score_text = my_font.render(f"{score}", True, (0, 0, 0))

    screen.fill((56, 179, 255))
    screen.blit(score_text, (400, 10))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        collision_sound.play()
        crashed = True
        print("Loser Loser LOSER!")
    pygame.display.flip()
    clock.tick(30)
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    clouds.update()
    enemies.update()
pygame.mixer.music.stop()
pygame.mixer.quit()
